from django.urls import reverse
from task_manager.users.models import User
from .tests_tasks import TaskTestCase


class TestFilterTasks(TaskTestCase):

    def test_filter_by_status(self):
        response = self.client.get(reverse('tasks'), {'status': 1})
        self.assertEqual(response.status_code, 200)
        task_names = [task.name for task in response.context['tasks']]
        expected_names = ['Initial Task', 'Third Task']

        self.assertEqual(sorted(task_names), sorted(expected_names))

    def test_filter_by_executor(self):
        response = self.client.get(reverse('tasks'), {'executor': 1})
        self.assertEqual(response.status_code, 200)
        task_names = [task.name for task in response.context['tasks']]
        expected_names = ['Second Task', 'Third Task']

        self.assertEqual(sorted(task_names), sorted(expected_names))

    def test_filter_by_label(self):
        response = self.client.get(reverse('tasks'), {'label': 3})
        self.assertEqual(response.status_code, 200)
        task_names = [task.name for task in response.context['tasks']]
        expected_names = ['Second Task', 'Third Task']
        self.assertEqual(sorted(task_names), sorted(expected_names))

    def test_filter_only_self_tasks(self):
        response = self.client.get(reverse('tasks'), {'self_tasks': True})
        self.assertEqual(response.status_code, 200)
        task_names = [task.name for task in response.context['tasks']]
        expected_names = ['Initial Task', 'Second Task']

        self.assertEqual(sorted(task_names), sorted(expected_names))


