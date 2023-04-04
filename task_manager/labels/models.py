from django.db import models


class LabelModel(models.Model):
    # objects = models.Manager()
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
