from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from .models import Label
from .forms import LabelForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User


class LabelListView(AuthRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    extra_context = {
        'title': _('Labels')
    }
