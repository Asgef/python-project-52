from task_manager.mixins import AuthRequiredMixin
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm


class StatusesListView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses')
    }
