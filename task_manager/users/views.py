from .models import User
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from task_manager.mixins import (
    AuthRequiredMixin, UserPermissionMixin, DeleteProtectionMixin
)


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    extra_context = {
        'title': _('Users')
    }


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'layouts/form.html'
    form_class = UserForm
    success_message = _('User is successfully registered')
    success_url = reverse_lazy('login')
    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register'),
    }


class UserEditView(
    AuthRequiredMixin, UserPermissionMixin, SuccessMessageMixin, UpdateView
):
    model = User
    template_name = 'layouts/form.html'
    form_class = UserForm
    success_message = _('User is successfully update')
    success_url = reverse_lazy('users')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    extra_context = {
        'title': _('Edit user'),
        'button_text': _('Edit'),
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.user = form.save()
        login(
            self.request, self.request.user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return response


class UserDeleteView(AuthRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'layouts/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User is successfully delete')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }
