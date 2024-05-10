from django.urls import path
from task_manager.labels.views import LabelListView, LabelAddView

urlpatterns = [
    path('', LabelListView.as_view(), name='labels'),
    path('create', LabelAddView.as_view(), name='label_add')
]
