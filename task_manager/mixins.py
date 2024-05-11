from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError


class AuthRequiredMixin(LoginRequiredMixin):

    auth_message = _('You are not logged in! Please log in.')
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class UserPermissionMixin(UserPassesTestMixin):

    permission_message = None
    permission_url = None

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)


class AuthorDeletionMixin(UserPermissionMixin):

    author_massage = None
    author_url = None

    def test_func(self):
        return self.get_object().author.id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, self.author_message)
        return redirect(self.author_url)
