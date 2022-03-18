from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id

class GlucoseValue(models.Model):
    device = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    time_stamp = models.DateTimeField()
    recording_type = models.IntegerField()
    glucose_history = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
