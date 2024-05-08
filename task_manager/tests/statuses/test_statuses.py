# from task_manager.users.models import User
# from django.urls import reverse_lazy
# from django.test import TestCase
# from task_manager.statuses.models import Status
#
#
# class Create(TestCase):
#     fixtures = ['status.json']
#
#     def test_open_without_login(self):
#         response = self.client.get(reverse_lazy('status_add'))
#         self.assertEqual(response.status_code, 302)
#
#     def test_create_status(self):
#         user = User.objects.get(pk=1)
#         self.client.force_login(user=user)
#         statuses = Status.objects.all()
#         response = self.client.get(reverse_lazy('status_add'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(statuses), 1)
#         response = self.client.post(
#             reverse_lazy('status_add'),
#             {'name': 'test'}
#         )
#         statuses_2 = Status.objects.all()
#         self.assertEqual(len(statuses_2), 2)
#         status_added = statuses_2[1]
#         self.assertEqual(status_added.name, 'test')
#
#
# class UpdateStatus(TestCase):
#     fixtures = ['status.json']
#
#     def test_update_without_login(self):
#         response = self.client.get(
#             reverse_lazy('status_update', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#
#     def test_update_status(self):
#         user = User.objects.get(pk=1)
#         self.client.force_login(user=user)
#         response = self.client.get(
#             reverse_lazy('status_update', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post(
#             reverse_lazy('status_update', kwargs={'pk': 1}), {'name': 'test'}
#         )
#         status = Status.objects.get(pk=1)
#         self.assertEqual(status.name, 'test')
#
#
# class DeleteStatus(TestCase):
#     fixtures = ['status.json']
#
#     def test_delete_without_login(self):
#         response = self.client.get(
#             reverse_lazy('status_delete', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#
#     def test_delete_status(self):
#         user = User.objects.get(pk=1)
#         self.client.force_login(user=user)
#         response = self.client.get(
#             reverse_lazy('status_delete', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post(
#             reverse_lazy('status_delete', kwargs={'pk': 1})
#         )
#         statuses = Status.objects.all()
#         self.assertEqual(len(statuses), 0)
