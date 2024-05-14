import os
import json
from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.tasks.models import Task


class TaskTestCase(TestCase):
    fixtures = ['task.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        fixture = os.path.join(
            os.path.dirname(__file__), os.path.pardir,
            'fixtures', 'task_data.json'
        )
        with open(fixture, 'r') as file:
            cls.task_data = json.load(file)

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)


class TestAddTask(TaskTestCase):

    def test_open_without_login(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 302)

    def test_create_status(self):
        initial_count = Task.objects.count()
        response = self.client.post(
            reverse_lazy('task_add'), self.task_data[0]
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), initial_count + 1)

        new_status = Task.objects.latest('id')
        self.assertEqual(new_status.name, self.task_data[0]['name'])
        self.assertEqual(
            new_status.description, self.task_data[0]['description']
        )


class TestUpdateTasks(TaskTestCase):

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
                'task_update', kwargs={'pk': 1}), self.task_data[1]
        )
        self.assertEqual(response.status_code, 302)

        updated_status = Task.objects.get(pk=1)
        self.assertEqual(updated_status.name, self.task_data[1]['name'])
        self.assertEqual(
            updated_status.description, self.task_data[1]['description']
        )


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
