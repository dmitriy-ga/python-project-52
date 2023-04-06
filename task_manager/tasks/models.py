from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import StatusModel
from task_manager.labels.models import LabelModel


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

    labels = models.ManyToManyField(LabelModel, through='LabelsThrough',
                                    through_fields=('task', 'label'),
                                    blank=True)

    def __str__(self):
        return self.name


class LabelsThrough(models.Model):
    label = models.ForeignKey(LabelModel, on_delete=models.PROTECT)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
