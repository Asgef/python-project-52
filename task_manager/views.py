from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = _('Hello from Hexlet!')
        context['description'] = _('Practical programming courses')
        context['invitation_button'] = _('Learn more')
        return context
