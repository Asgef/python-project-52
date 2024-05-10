# from task_manager.users.models import User
# from django.urls import reverse_lazy
# from django.test import TestCase
# from task_manager.statuses.models import Status
#
#
# class StatusTestCase(TestCase):
#     fixtures = ['status.json']
#
#     def setUp(self):
#         self.user = User.objects.get(pk=1)
#         self.client.force_login(self.user)
#
#
# class TestAddStatus(StatusTestCase):
#
#     def test_open_without_login(self):
#         self.client.logout()
#         response = self.client.get(reverse_lazy('statuses'))
#         self.assertEqual(response.status_code, 302)
#
#     def test_create_status(self):
#         initial_count = Status.objects.count()
#         response = self.client.post(
#             reverse_lazy('status_add'), {'name': 'New Status'}
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Status.objects.count(), initial_count + 1)
#         new_status = Status.objects.latest('id')
#         self.assertEqual(new_status.name, 'New Status')
#
#
# class TestUpdateStatus(StatusTestCase):
#
#     def test_update_without_login(self):
#         self.client.logout()
#         response = self.client.get(
#             reverse_lazy(
#                 'status_update', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#
#     def test_update_status(self):
#         response = self.client.get(
#             reverse_lazy('status_update', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post(
#             reverse_lazy(
#                 'status_update', kwargs={'pk': 1}), {'name': 'Updated Status'}
#         )
#         self.assertEqual(response.status_code, 302)
#         updated_status = Status.objects.get(pk=1)
#         self.assertEqual(updated_status.name, 'Updated Status')
#
#
# class TestDeleteStatus(StatusTestCase):
#
#     def test_delete_without_login(self):
#         self.client.logout()
#         response = self.client.get(
#             reverse_lazy('status_delete', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#
#     def test_delete_status(self):
#         initial_count = Status.objects.count()
#         response = self.client.post(
#             reverse_lazy('status_delete', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Status.objects.count(), initial_count - 1)
