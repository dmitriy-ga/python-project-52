from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import LabelModel
from task_manager.mixins import RedirectToLoginMixin, ProtectedObjectCheckMixin
from django.utils.translation import gettext as _


class LabelsIndex(RedirectToLoginMixin, ListView):
    template_name = 'manage/index/labels_index.html'
    model = LabelModel
    context_object_name = 'labels'


class LabelsCreate(SuccessMessageMixin, RedirectToLoginMixin, CreateView):
    template_name = 'manage/create.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    success_message = _('Label created successfully')
    extra_context = {
        'page_title': _('Create label'),
        'url_path': 'labels_create',
        'button_text': _('Create'),
    }


class LabelsUpdate(SuccessMessageMixin, RedirectToLoginMixin, UpdateView):
    template_name = 'manage/update.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    fields = ['name', ]
    context_object_name = 'current_object'
    pk_url_kwarg = 'label_id'
    success_message = _('Label updated successfully')
    extra_context = {
        'page_title': _('Update label'),
        'url_path': 'labels_update',
    }


class LabelsDelete(SuccessMessageMixin, RedirectToLoginMixin,
                   ProtectedObjectCheckMixin, DeleteView):
    template_name = 'manage/delete.html'
    model = LabelModel
    success_url = reverse_lazy('labels_index')
    context_object_name = 'current_object'
    pk_url_kwarg = 'label_id'
    success_message = _('Label deleted successfully')
    protected_redirect_to = reverse_lazy('labels_index')
    protected_message = _("Can't delete label in use")
    extra_context = {
        'object_group': _('Label')
    }
