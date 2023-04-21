from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.utils import RedirectToLoginMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import TaskModel
from .filters import TasksFilter


class TasksIndex(RedirectToLoginMixin, FilterView):
    template_name = 'tasks/index.html'
    filterset_class = TasksFilter
    context_object_name = 'tasks'


class TasksShow(RedirectToLoginMixin, DetailView):
    template_name = 'tasks/show.html'
    model = TaskModel
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class TasksCreate(SuccessMessageMixin, RedirectToLoginMixin, CreateView):
    template_name = 'tasks/create.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'executor', 'status', 'labels']
    success_message = 'Task created successfully'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class TasksUpdate(SuccessMessageMixin, RedirectToLoginMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'executor', 'status', 'labels']
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    success_message = 'Task updated successfully'


class TasksDelete(SuccessMessageMixin, RedirectToLoginMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    success_message = 'Task deleted successfully'

    def dispatch(self, request, *args, **kwargs):
        # Only author can delete task
        if request.user.id != self.get_object().author.id:
            messages.error(self.request, 'Only author can delete this task')
            return redirect(reverse_lazy('tasks_index'))
        return super().dispatch(request, *args, **kwargs)
