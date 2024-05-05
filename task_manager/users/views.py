from django.views.generic.list import ListView
from django.contrib.auth.models import User


class UsersListView(ListView):
    model = User
    paginate_by = 20
    template_name = 'users/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
