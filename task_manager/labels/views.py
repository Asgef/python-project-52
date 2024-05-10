from task_manager.mixins import AuthRequiredMixin  # AuthorDeletionMixin
from django.views.generic import ListView, CreateView, UpdateView  # DeleteView
from django.utils.translation import gettext_lazy as _
from .models import Label
from .forms import LabelForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from task_manager.users.models import User


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
