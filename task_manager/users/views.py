from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import SignupForm, UpdateForm


class UsersIndex(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UsersCreate(CreateView):
    template_name = 'users/create.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = SignupForm


class UsersUpdate(UpdateView):
    template_name = 'users/update.html'
    model = User
    success_url = reverse_lazy('users_index')
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    form_class = UpdateForm

    def dispatch(self, request, *args, **kwargs):
        # Only self user can update
        if request.user.id != self.get_object().id:
            return redirect(reverse_lazy('users_index'))
        return super().dispatch(request, *args, **kwargs)


class UsersDelete(DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users_index')
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'

    def dispatch(self, request, *args, **kwargs):
        # Only self user can delete
        if request.user.id != self.get_object().id:
            return redirect(reverse_lazy('users_index'))
        return super().dispatch(request, *args, **kwargs)
