from django.test import TestCase, Client
from django.urls import reverse_lazy
from .models import User


class UserTestCase(TestCase):
    fixtures = ['user.json']

    def setUp(self):
        self.client = Client()
        self.user_1 = User.objects.get(pk=1)
        self.client.force_login(self.user_1)


class TestCreateUser(TestCase):
    data = {
        'username': 'test_user',
        'password1': 'testpassword123',
        'password2': 'testpassword123',
        'first_name': 'Test',
        'last_name': 'User',
    }

    def test_registration_user(self):
        url = reverse_lazy('create')
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(
            response_get, template_name='users/user_form.html'
        )

        response_post = self.client.post(url, self.data)

        self.assertRedirects(
            response_post, reverse_lazy('login'),
            status_code=302, target_status_code=200
        )

        created_user = User.objects.get(username='test_user')
        self.assertIsNotNone(created_user)


class TestUpdateUser(UserTestCase):
    def test_update_user(self):
        url = reverse_lazy('user_edit', kwargs={'pk': self.user_1.pk})
        new_data = {
            'username': 'test_username',
            'password1': '12345tgb',
            'password2': '12345tgb',
            'first_name': 'Test_first_name',
            'last_name': 'Test_last_name',
        }

        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(
            response_get, template_name='users/user_form.html'
        )

        response_post = self.client.post(url, new_data)

        self.assertRedirects(
            response_post, reverse_lazy('users'),
            status_code=302, target_status_code=200
        )

        updated_user = User.objects.get(pk=self.user_1.pk)

        self.assertEqual(updated_user.username, 'test_username')
        self.assertEqual(updated_user.first_name, 'Test_first_name')
        self.assertEqual(updated_user.last_name, 'Test_last_name')


class TestDeleteUser(UserTestCase):
    def test_delete_user(self):
        user_count_before_delete = User.objects.count()
        url = reverse_lazy('user_delete', kwargs={'pk': self.user_1.pk})

        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, template_name='users/delete.html')

        response_post = self.client.post(url)

        self.assertRedirects(
            response_post, reverse_lazy('users'),
            status_code=302, target_status_code=200
        )

        user_count_after_delete = User.objects.count()
        self.assertEqual(user_count_before_delete - 1, user_count_after_delete)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user_1.pk)
