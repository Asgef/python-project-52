from django.urls import path
from task_manager.statuses.views import (
    StatusesListView, StatusAddView, StatusUpdateView, StatusDeleteView
)


urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses'),
    path('create/', StatusAddView.as_view(), name='status_add'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
