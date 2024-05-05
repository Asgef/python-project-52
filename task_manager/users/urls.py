from django.urls import path
from task_manager.users.views import UsersListView, UserRegisterView


urlpatterns = [
    path('', UsersListView.as_view(), name='users'),
    path('create/', UserRegisterView.as_view(), name='create')
]
