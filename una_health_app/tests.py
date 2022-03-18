from django.test import TestCase
from una_health_app.models import *


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(user_id = "aaa")
        self.glucose_value = GlucoseValue.objects.create(device = "FreeStyle LibreLink", serial_number = "1D48A10E-DDFB-4888-8158-026F08814832",time_stamp = "2001-12-03 10:57", recording_type = 0, glucose_history = 77, user = self.user )
    
    def test_user_saved(self):
        self.assertGreater(self.user.pk, 0)
    
    def test_glucose_level_saved(self):
        self.assertGreater(self.glucose_value.pk, 0)
    
    def test_glucose_level_fk(self):
        self.assertEqual(self.glucose_value.user.pk, self.user.pk)
