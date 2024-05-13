from django.urls import path
from task_manager.tasks.views import (
    TasksListView, TaskAddView, TaskUpdateView, TaskDeleteView, TaskShowView
)


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', TaskAddView.as_view(), name='task_add'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/', TaskShowView.as_view(), name='task_show'),
]
