from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import LabelModel
from task_manager.mixins import RedirectToLoginMixin, ProtectedObjectCheckMixin
from django.utils.translation import gettext as _


class LabelsIndex(RedirectToLoginMixin, ListView):
    template_name = 'labels/index.html'
    model = LabelModel
    context_object_name = 'labels'


class LabelsCreate(SuccessMessageMixin, RedirectToLoginMixin, CreateView):
    template_name = 'labels/create.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    success_message = _('Label created successfully')


class LabelsUpdate(SuccessMessageMixin, RedirectToLoginMixin, UpdateView):
    template_name = 'labels/update.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    context_object_name = 'label'
    pk_url_kwarg = 'label_id'
    success_message = _('Label updated successfully')


class LabelsDelete(SuccessMessageMixin, RedirectToLoginMixin,
                   ProtectedObjectCheckMixin, DeleteView):
    template_name = 'labels/delete.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    context_object_name = 'label'
    pk_url_kwarg = 'label_id'
    success_message = _('Label deleted successfully')
    protected_redirect_to = reverse_lazy('labels_index')
    protected_message = _("Can't delete label in use")
