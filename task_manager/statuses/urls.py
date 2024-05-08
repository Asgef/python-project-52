from django.urls import path
from task_manager.statuses.views import StatusesListView, StatusAddView


urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses'),
    path('create', StatusAddView.as_view(), name='status_add')
]
