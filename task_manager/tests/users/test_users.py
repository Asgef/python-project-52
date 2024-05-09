from task_manager.users.models import User
from django.urls import reverse_lazy
from django.test import TestCase


class UserTestCase(TestCase):
    fixtures = ['user.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)


class TestCreateUser(UserTestCase):
    data = {
        'username': 'test_user',
        'password1': 'testpassword123',
        'password2': 'testpassword123',
        'first_name': 'Test',
        'last_name': 'User',
    }

    def test_open_without_login(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)

    def test_create_status(self):
        initial_count = User.objects.count()
        response = self.client.post(
            reverse_lazy('create'), self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), initial_count + 1)

        new_user = User.objects.latest('id')
        self.assertEqual(new_user.username, 'test_user')
        self.assertEqual(new_user.first_name, 'Test')
        self.assertEqual(new_user.last_name, 'User')


class TestUpdateUser(UserTestCase):
    data = {
        'username': 'test_user',
        'password1': 'testpassword123',
        'password2': 'testpassword123',
        'first_name': 'Test',
        'last_name': 'User',
    }

    def test_update_without_login(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy(
                'user_edit', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_update_status(self):
        response = self.client.get(
            reverse_lazy('user_edit', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse_lazy(
                'user_edit', kwargs={'pk': 1}), self.data
        )
        self.assertEqual(response.status_code, 302)

        updated_user = User.objects.get(pk=1)
        self.assertEqual(updated_user.username, 'test_user')
        self.assertEqual(updated_user.first_name, 'Test')
        self.assertEqual(updated_user.last_name, 'User')


class TestDeleteUser(UserTestCase):

    def test_delete_without_login(self):
        self.client.logout()
        response = self.client.get(
          reverse_lazy('status_delete', kwargs={'pk': 1})
          )
        self.assertEqual(response.status_code, 302)

    def test_delete_status(self):
        initial_count = User.objects.count()
        response = self.client.post(
          reverse_lazy('user_delete', kwargs={'pk': 1})
          )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), initial_count - 1)
