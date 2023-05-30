from django.db import models
from django.utils.translation import gettext_lazy as _


class LabelModel(models.Model):
    # objects = models.Manager()
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=_('name'))

    def __str__(self):
        return self.name
