from django_filters import FilterSet, BooleanFilter, ChoiceFilter
from django import forms
from .models import Task
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class TasksFilter(FilterSet):
    labels_choices = Label.objects.values_list('id', 'name')
    labels = ChoiceFilter(label=_('Label'), choices=labels_choices)

    self_task = BooleanFilter(widget=forms.CheckboxInput(),
                              label=_('Self tasks only'),
                              method='get_self_tasks')

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'self_task']

    def get_self_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset
