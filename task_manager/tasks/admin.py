from django.contrib import admin
from .models import TaskModel


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
