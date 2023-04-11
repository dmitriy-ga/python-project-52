from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import StatusModel


class StatusesIndex(LoginRequiredMixin, ListView):
    template_name = 'statuses/index.html'
    model = StatusModel
    context_object_name = 'statuses'


class StatusesCreate(LoginRequiredMixin, CreateView):
    template_name = 'statuses/create.html'
    model = StatusModel
    success_url = reverse_lazy('statuses_index')
    fields = ['name', ]


class StatusesUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = StatusModel
    success_url = reverse_lazy('statuses_index')
    fields = ['name', ]
    context_object_name = 'status'
    pk_url_kwarg = 'status_id'


class StatusesDelete(LoginRequiredMixin, DeleteView):
    template_name = 'statuses/delete.html'
    model = StatusModel
    success_url = reverse_lazy('statuses_index')
    context_object_name = 'status'
    pk_url_kwarg = 'status_id'
