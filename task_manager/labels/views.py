from .models import Label
from .forms import LabelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class LabelListView(AuthRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    extra_context = {
        'title': _('Labels')
    }


class LabelAddView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    template_name = 'layouts/form.html'
    form_class = LabelForm
    success_message = _('Label successfully created')
    success_url = reverse_lazy('labels')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'layouts/form.html'
    form_class = LabelForm
    success_message = _('Label successfully changed')
    success_url = reverse_lazy('labels')
    extra_context = {
        'title': _('Change label'),
        'button_text': _('Change'),
    }


class LabelDeleteView(
    AuthRequiredMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView
):
    model = Label
    template_name = 'layouts/delete.html'
    success_message = _('Label successfully delete')
    success_url = reverse_lazy('labels')
    protected_message = _(
        'It is not possible to delete a label because it is in use'
    )
    protected_url = reverse_lazy('labels')
    extra_context = {
        'title': _('Delete label'),
        'button_text': _('Yes, delete'),
    }
