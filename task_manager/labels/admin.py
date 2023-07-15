from django.contrib import admin
from .models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
