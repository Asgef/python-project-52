from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from .models import Task
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.forms import CheckboxInput


class TaskFilter(FilterSet):

    status = ModelChoiceFilter(
        label=_('Status'), queryset=Status.objects.all()
    )
    executor = ModelChoiceFilter(
        label=_('Executor'), queryset=User.objects.all()
    )
    label = ModelChoiceFilter(
        label=_('Label'), queryset=Label.objects.all()
    )
    self_tasks = BooleanFilter(
        label=_('Only self tasks'), widget=CheckboxInput,
        method='get_self_tasks'
    )

    def get_self_tasks(self, queryset, field_name, value):
        if value:
            user = self.request.user.id
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']
