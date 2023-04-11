from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import TaskModel
from .filters import TasksFilter


class TasksIndex(LoginRequiredMixin, FilterView):
    template_name = 'tasks/index.html'
    filterset_class = TasksFilter
    context_object_name = 'tasks'


class TasksShow(LoginRequiredMixin, DetailView):
    template_name = 'tasks/show.html'
    model = TaskModel
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class TasksCreate(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'executor', 'status', 'labels']

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class TasksUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'executor', 'status', 'labels']
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class TasksDelete(LoginRequiredMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def dispatch(self, request, *args, **kwargs):
        # Only author can delete task
        if request.user.id != self.get_object().author.id:
            return redirect(reverse_lazy('tasks_index'))
        return super().dispatch(request, *args, **kwargs)
