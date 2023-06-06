from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import StatusModel
from task_manager.mixins import RedirectToLoginMixin
from django.utils.translation import gettext as _


class StatusesIndex(RedirectToLoginMixin, ListView):
    template_name = 'statuses/index.html'
    model = StatusModel
    context_object_name = 'statuses'


class StatusesCreate(SuccessMessageMixin, RedirectToLoginMixin, CreateView):
    template_name = 'statuses/create.html'
    model = StatusModel
    success_url = reverse_lazy('statuses_index')
    fields = ['name', ]
    success_message = _('Status created successfully')


class StatusesUpdate(SuccessMessageMixin, RedirectToLoginMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = StatusModel
    success_url = reverse_lazy('statuses_index')
    fields = ['name', ]
    context_object_name = 'status'
    pk_url_kwarg = 'status_id'
    success_message = _('Status updated successfully')


class StatusesDelete(SuccessMessageMixin, RedirectToLoginMixin, DeleteView):
    template_name = 'statuses/delete.html'
    model = StatusModel
    success_url = reverse_lazy('statuses_index')
    context_object_name = 'status'
    pk_url_kwarg = 'status_id'
    success_message = _('Status deleted successfully')
