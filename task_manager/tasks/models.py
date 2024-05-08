from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author'
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='executor'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
