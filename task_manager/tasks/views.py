from .models import Task
from .forms import TaskForm
from .filters import TaskFilter
from django.urls import reverse_lazy
from task_manager.users.models import User
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)


class TasksListView(AuthRequiredMixin, FilterView, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show')
    }


class TaskShowView(AuthRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_show.html'
    context_object_name = 'task'
    extra_context = {
        'title': _('View a task')
    }


class TaskAddView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'layouts/form.html'
    form_class = TaskForm
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
    model = Task
    template_name = 'layouts/form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')
    extra_context = {
        'title': _('Task change'),
        'button_text': _('Change'),
    }


class TaskDeleteView(
    AuthRequiredMixin, AuthorDeletionMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = 'layouts/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully delete')
    author_message = _('The task can be deleted only by its author')
    author_url = reverse_lazy('tasks')
    extra_context = {
        'title': _('Delete task'),
        'button_text': _('Yes, delete'),
    }
