from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import StatusModel


class TaskModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200)

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='author')

    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='executor')

    status = models.ForeignKey(StatusModel, on_delete=models.PROTECT,
                               related_name='status')

    def __str__(self):
        return self.name
