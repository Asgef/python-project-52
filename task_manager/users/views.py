from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from .forms import UserForm
from .models import User
from django.urls import reverse_lazy, reverse
from django.contrib import messages


class UsersListView(ListView):
    model = User
    paginate_by = 20
    template_name = 'users/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user_form.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register'),
    }


class UserEditView(SuccessMessageMixin, CreateView):
    template_name = 'users/user_form.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully update')
    extra_context = {
        'title': _('Edit user'),
        'button_text': _('Edit'),
    }

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user == request.user:
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, _(
            "You do not have permission to change another user."
        ))
        return HttpResponseRedirect(reverse('users'))


class UserDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('home_page')
    success_message = _('User is successfully delete')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user == request.user:
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, _(
            "You do not have permission to change another user."
        ))
        return HttpResponseRedirect(reverse('users'))
