from django.urls import path
from task_manager.labels.views import (
    LabelListView, LabelAddView, LabelUpdateView, LabelDeleteView
)

urlpatterns = [
    path('', LabelListView.as_view(), name='labels'),
    path('create/', LabelAddView.as_view(), name='label_add'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
]
