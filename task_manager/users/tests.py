from django.test import TestCase
from django.urls import reverse


class TestUser(TestCase):
    def test_registration_user(self):
        data = {
            'first_name': 'First_name_user',
            'last_name': 'Last_name_user',
            'username': 'Username_user',
            'password1': '12345tgb',
            'password2': '12345tgb',
        }
        url = reverse('create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
