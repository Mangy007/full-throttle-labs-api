from django.test import TestCase

from core.models import User, ActivityPeriod
from core.views import get_user_data_by_id, get_all_user_data, get_user_activity_details


class UserTestCase(TestCase):

    def test_user(self):
        with self.assertRaises(User.DoesNotExist):
            user_1 = User.objects.get(id="W07QCRPA4")
            user_1_expected_output = '{"id": "W07QCRPA4", "real_name": "Glinda Southgood", "tz": "Asia/Kolkata"}'
            self.assertEquals(user_1.__str__(), user_1_expected_output)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id="W07QCSQA6")


class ViewTestCase(TestCase):

    def test_get_user_data_by_id(self):
        user_1_id = "W07QCSQA6"
        self.assertEquals(get_user_data_by_id(user_1_id), None)

    def test_get_all(self):
        user_1_id = "W07QCSQA6"
        self.assertEquals(get_all_user_data(), None)

    def test_get_user_activity_details(self):
        user_1 = None
        self.assertEquals(get_user_activity_details(user_1), [])
