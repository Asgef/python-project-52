from task_manager.users.models import User
from django.urls import reverse_lazy
from django.test import TestCase
from task_manager.tasks.models import Task


class TaskTestCase(TestCase):
    fixtures = ['task.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)


class TestAddTask(TaskTestCase):

    data = {
        'name': "New test task",
        'description': 'Description new test task',
        'status': 1,
        'executor': 1
    }

    def test_open_without_login(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 302)

    def test_create_status(self):
        initial_count = Task.objects.count()
        response = self.client.post(
            reverse_lazy('task_add'), self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), initial_count + 1)

        new_status = Task.objects.latest('id')
        self.assertEqual(new_status.name, self.data['name'])
        self.assertEqual(new_status.description, self.data['description'])


class TestUpdateTasks(TaskTestCase):

    data = {
        'name': "Updated test task",
        'description': 'Description updated test task',
        'status': 1,
        'executor': 1
    }

    def test_update_without_login(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy(
                'task_update', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_update_status(self):
        response = self.client.get(
            reverse_lazy('task_update', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse_lazy(
                'task_update', kwargs={'pk': 1}), self.data
        )
        self.assertEqual(response.status_code, 302)

        updated_status = Task.objects.get(pk=1)
        self.assertEqual(updated_status.name, self.data['name'])
        self.assertEqual(updated_status.description, self.data['description'])


class TestDeleteTask(TaskTestCase):

    def test_delete_without_login(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_status(self):
        initial_count = Task.objects.count()
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), initial_count - 1)
