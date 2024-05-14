from django.urls import path
from task_manager.users.views import (
    UsersListView, UserRegisterView,
    UserEditView, UserDeleteView
)


urlpatterns = [
    path('', UsersListView.as_view(), name='users'),
    path('create/', UserRegisterView.as_view(), name='create'),
    path('<int:pk>/update/', UserEditView.as_view(), name='user_edit'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
