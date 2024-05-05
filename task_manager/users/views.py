from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from .models import User
from django.urls import reverse_lazy


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
    success_url = reverse_lazy('home_page')
    success_message = 'User is successfully registered'
    extra_context = {
        'title': 'Registration',
        'button_text': 'Register',
    }


class UserEditView(SuccessMessageMixin, CreateView):
    template_name = 'users/user_form.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('home_page')
    success_message = 'User is successfully update'
    extra_context = {
        'title': 'Edit user',
        'button_text': 'Edit',
    }


class UserDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('home_page')
    success_message = 'User is successfully delete'
    extra_context = {
        'title': 'Delete user',
        'button_text': 'Yes, delete',
    }
