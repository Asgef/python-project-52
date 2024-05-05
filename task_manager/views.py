from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class HomePageView(TemplateView):

    template_name = "index.html"
    extra_context = {
        'title': _('Task Manager Hexlet'),
        'greeting': _('Hello from Hexlet!'),
        'description': _('Practical programming courses'),
        'invitation_button': _('Learn more')
    }


# class UserRegisterView(SuccessMessageMixin, CreateView):
#     template_name = 'users/user_form.html'
#     form_class = UserForm
#     model = User
#     success_url = reverse_lazy('home_page')
#     success_message = 'User is successfully registered'
#     extra_context = {
#         'title': 'Registration',
#         'button_text': 'Register',
#     }