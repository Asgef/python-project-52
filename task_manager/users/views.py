from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from .forms import UserForm
from .models import User
from django.urls import reverse_lazy
from task_manager.mixins import AuthRequiredMixin
from .mixins import UserPermissionMixin


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'layouts/form.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register'),
    }


class UserEditView(
    AuthRequiredMixin, UserPermissionMixin, SuccessMessageMixin, UpdateView
):
    template_name = 'layouts/form.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully update')
    extra_context = {
        'title': _('Edit user'),
        'button_text': _('Edit'),
    }


class UserDeleteView(
    AuthRequiredMixin, UserPermissionMixin, SuccessMessageMixin, DeleteView
):
    template_name = 'layouts/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully delete')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }
