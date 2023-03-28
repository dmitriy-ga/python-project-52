from django.contrib import admin
from .models import StatusModel


@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
