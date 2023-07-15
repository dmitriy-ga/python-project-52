from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=_('name'))
    description = models.TextField(max_length=200,
                                   verbose_name=_('description'))

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='author', verbose_name=_('author'))

    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 related_name='executor',
                                 verbose_name=_('executor'))

    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               related_name='status', verbose_name=_('status'))

    labels = models.ManyToManyField(Label, through='LabelsThrough',
                                    through_fields=('task', 'label'),
                                    blank=True, verbose_name=_('labels'))

    def __str__(self):
        return self.name


class LabelsThrough(models.Model):
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
