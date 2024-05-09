from django.urls import path
from task_manager.tasks.views import TasksListView, TaskAddView


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', TaskAddView.as_view(), name='task_add'),
]
