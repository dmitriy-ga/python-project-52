from django.forms import ModelForm
from .models import StatusModel
from django import forms


class StatusForm(ModelForm):
    name = forms.CharField(max_length=200, required=True)

    class Meta:
        model = StatusModel
        fields = ['name', ]
