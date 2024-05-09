from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class StatusesListView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses')
    }


class StatusAddView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }


class StatusUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/status_form.html'
    form_class = StatusForm
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully changed')
    extra_context = {
        'title': _('Status change'),
        'button_text': _('Change'),
    }


class StatusDeleteView(
    AuthRequiredMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView
):
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully delete')
    extra_context = {
        'title': _('Delete status'),
        'button_text': _('Yes, delete'),
    }
