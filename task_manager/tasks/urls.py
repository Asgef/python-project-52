from django.urls import path
from task_manager.tasks.views import index


urlpatterns = [
    path('', index),
]
