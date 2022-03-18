import csv
from datetime import datetime
from lib2to3.pytree import Base
from django.core.management import BaseCommand

from una_health_app.models import GlucoseValue, User

class Command(BaseCommand):

    help = "Loads CSV Data for user"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            header = []
            header = next(data)
            new_user = User(user_id=header[4])
            User.save(new_user)
            for i in range(2):
                next(data)
            all_levels=[]
            for row in data:
                device = row[0]
                serial_number = row[1]
                datetime_obj = datetime.strptime(row[2], "%d-%m-%Y %H:%M")
                recording_type = row[3] if row[3] is not '' else 0
                glucose_history = row[4] if row[4] is not '' else 0
                new_glucose_value = GlucoseValue(device = device, serial_number = serial_number, time_stamp= datetime_obj, recording_type = recording_type, glucose_history = glucose_history, user = new_user)
                print(glucose_history)
                all_levels.append(new_glucose_value)
        GlucoseValue.objects.bulk_create(all_levels)
               