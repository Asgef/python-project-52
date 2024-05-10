from task_manager.users.models import User
from django.urls import reverse_lazy
from django.test import TestCase
from task_manager.labels.models import Label


class LabelTestCase(TestCase):
    fixtures = ['labels.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)


class TestAddLabel(LabelTestCase):

    def test_open_without_login(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 302)

    def test_create_label(self):
        initial_count = Label.objects.count()
        response = self.client.post(
            reverse_lazy('label_add'), {'name': 'New Label'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), initial_count + 1)
        new_status = Label.objects.latest('id')
        self.assertEqual(new_status.name, 'New Label')


# class TestUpdateLabel(LabelTestCase):
#
#     def test_update_without_login(self):
#         self.client.logout()
#         response = self.client.get(
#             reverse_lazy(
#                 'label_update', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#
#     def test_update_label(self):
#         response = self.client.get(
#             reverse_lazy('label_update', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post(
#             reverse_lazy(
#                 'label_update', kwargs={'pk': 1}), {'name': 'Updated Label'}
#         )
#         self.assertEqual(response.status_code, 302)
#         updated_status = Label.objects.get(pk=1)
#         self.assertEqual(updated_status.name, 'Updated Label')
#
#
# class TestDeleteLabel(LabelTestCase):
#
#     def test_delete_without_login(self):
#         self.client.logout()
#         response = self.client.get(
#             reverse_lazy('label_delete', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#
#     def test_delete_label(self):
#         initial_count = Label.objects.count()
#         response = self.client.post(
#             reverse_lazy('label_delete', kwargs={'pk': 1})
#         )
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Label.objects.count(), initial_count - 1)
