from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Status
from task_manager.mixins import RedirectToLoginMixin, ProtectedObjectCheckMixin
from django.utils.translation import gettext as _


class StatusesIndex(RedirectToLoginMixin, ListView):
    template_name = 'manage/index/statuses_index.html'
    model = Status
    context_object_name = 'statuses'


class StatusesCreate(SuccessMessageMixin, RedirectToLoginMixin, CreateView):
    template_name = 'manage/create.html'
    model = Status
    success_url = reverse_lazy('statuses_index')
    fields = ['name', ]
    success_message = _('Status created successfully')
    extra_context = {
        'page_title': _('Create status'),
        'url_path': 'statuses_create',
        'button_text': _('Create'),
    }


class StatusesUpdate(SuccessMessageMixin, RedirectToLoginMixin, UpdateView):
    template_name = 'manage/update.html'
    model = Status
    success_url = reverse_lazy('statuses_index')
    fields = ['name', ]
    context_object_name = 'current_object'
    pk_url_kwarg = 'status_id'
    success_message = _('Status updated successfully')
    extra_context = {
        'page_title': _('Update status'),
        'url_path': 'statuses_update',
    }


class StatusesDelete(SuccessMessageMixin, RedirectToLoginMixin,
                     ProtectedObjectCheckMixin, DeleteView):
    template_name = 'manage/delete.html'
    model = Status
    success_url = reverse_lazy('statuses_index')
    context_object_name = 'current_object'
    pk_url_kwarg = 'status_id'
    success_message = _('Status deleted successfully')
    protected_redirect_to = reverse_lazy('statuses_index')
    protected_message = _("Can't delete status in use")
    extra_context = {
        'object_group': _('Status')
    }
