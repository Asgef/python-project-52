from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class TasksListView(AuthRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks')
    }
