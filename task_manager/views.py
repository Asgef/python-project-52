from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages


class HomePageView(TemplateView):

    template_name = "index.html"
    extra_context = {
        'title': _('Task Manager Hexlet'),
        'greeting': _('Hello from Hexlet!'),
        'description': _('Practical programming courses'),
        'invitation_button': _('Learn more')
    }


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'layouts/form.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home_page')
    success_message = _('You are logged in')
    extra_context = {
        'title': _('Login'),
        'button_text': _('Enter'),
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
