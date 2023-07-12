from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import RedirectToLoginMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import TaskModel
from .filters import TasksFilter
from django.utils.translation import gettext as _


class TasksIndex(RedirectToLoginMixin, FilterView):
    template_name = 'manage/index/tasks_index.html'
    filterset_class = TasksFilter
    context_object_name = 'tasks'


class TasksShow(RedirectToLoginMixin, DetailView):
    template_name = 'manage/show_task.html'
    model = TaskModel
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class TasksCreate(SuccessMessageMixin, RedirectToLoginMixin, CreateView):
    template_name = 'manage/create.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'status', 'executor', 'labels']
    success_message = _('Task created successfully')
    extra_context = {
        'page_title': _('Create task'),
        'url_path': 'tasks_create',
    }

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class TasksUpdate(SuccessMessageMixin, RedirectToLoginMixin, UpdateView):
    template_name = 'manage/update.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'status', 'executor', 'labels']
    context_object_name = 'current_object'
    pk_url_kwarg = 'task_id'
    success_message = _('Task updated successfully')
    extra_context = {
        'page_title': _('Update task'),
        'url_path': 'tasks_update',
    }


class TasksDelete(SuccessMessageMixin, RedirectToLoginMixin, DeleteView):
    template_name = 'manage/delete.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    context_object_name = 'current_object'
    pk_url_kwarg = 'task_id'
    success_message = _('Task deleted successfully')
    extra_context = {
        'object_group': _('Task')
    }

    def dispatch(self, request, *args, **kwargs):
        # Only author can delete task
        if request.user.id != self.get_object().author.id:
            messages.error(self.request, _('Only author can delete this task'))
            return redirect(reverse_lazy('tasks_index'))
        return super().dispatch(request, *args, **kwargs)
