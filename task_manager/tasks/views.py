from task_manager.mixins import AuthRequiredMixin  # DeleteProtectionMixin
from django.views.generic import ListView, CreateView, UpdateView  # DeleteView
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.users.models import User


class TasksListView(AuthRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks')
    }


class TaskAddView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')
    extra_context = {
        'title': _('Task change'),
        'button_text': _('Change'),
    }
