from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import TaskModel


class TasksIndex(ListView):
    template_name = 'tasks/index.html'
    model = TaskModel
    context_object_name = 'tasks'


class TasksShow(DetailView):
    template_name = 'tasks/show.html'
    model = TaskModel
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class TasksCreate(CreateView):
    template_name = 'tasks/create.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'executor', 'status']

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)


class TasksUpdate(UpdateView):
    template_name = 'tasks/update.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    fields = ['name', 'description', 'executor', 'status']
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'


class TasksDelete(DeleteView):
    template_name = 'tasks/delete.html'
    model = TaskModel
    success_url = reverse_lazy('tasks_index')
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
