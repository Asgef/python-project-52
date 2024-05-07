from django.urls import path
from task_manager.statuses.views import index


urlpatterns = [
    path('', index)
]
