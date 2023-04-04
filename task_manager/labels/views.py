from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import LabelModel


class LabelsIndex(ListView):
    template_name = 'labels/index.html'
    model = LabelModel
    context_object_name = 'labels'


class LabelsCreate(CreateView):
    template_name = 'labels/create.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]


class LabelsUpdate(UpdateView):
    template_name = 'labels/update.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    context_object_name = 'label'
    pk_url_kwarg = 'label_id'


class LabelsDelete(DeleteView):
    template_name = 'labels/delete.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    context_object_name = 'label'
    pk_url_kwarg = 'label_id'
