from django_filters import FilterSet, BooleanFilter
from django import forms
from .models import TaskModel
from django.utils.translation import gettext as _


class TasksFilter(FilterSet):
    self_task = BooleanFilter(widget=forms.CheckboxInput(),
                              label=_('Self tasks only'),
                              method='get_self_tasks')

    class Meta:
        model = TaskModel
        fields = ['status', 'executor', 'labels', 'self_task']

    def get_self_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset
