from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import LabelModel


class LabelsIndex(LoginRequiredMixin, ListView):
    template_name = 'labels/index.html'
    model = LabelModel
    context_object_name = 'labels'
    permission_denied_message = "You're not logged in, please login"
    # This message not showing


class LabelsCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'labels/create.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    success_message = 'Label created successfully'
    permission_denied_message = "You're not logged in, please login"
    # This message not showing


class LabelsUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'labels/update.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    context_object_name = 'label'
    pk_url_kwarg = 'label_id'
    success_message = 'Label updated successfully'
    permission_denied_message = "You're not logged in, please login"
    # This message not showing


class LabelsDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'labels/delete.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    context_object_name = 'label'
    pk_url_kwarg = 'label_id'
    success_message = 'Label deleted successfully'
    permission_denied_message = "You're not logged in, please login"
    # This message not showing
