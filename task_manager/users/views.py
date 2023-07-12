from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import SignupForm, UpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import RedirectToLoginMixin, ProtectedObjectCheckMixin
from .mixins import SelfUserCheckMixin
from django.utils.translation import gettext as _


class UsersIndex(ListView):
    template_name = 'manage/index/users_index.html'
    model = User
    context_object_name = 'users'


class UsersCreate(SuccessMessageMixin, CreateView):
    template_name = 'manage/create.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = SignupForm
    success_message = _('User signed up successfully')
    extra_context = {
        'page_title': _('Create user'),
        'url_path': 'users_create',
    }


class UsersUpdate(SuccessMessageMixin, RedirectToLoginMixin,
                  SelfUserCheckMixin, UpdateView):
    template_name = 'manage/update.html'
    model = User
    success_url = reverse_lazy('users_index')
    context_object_name = 'current_object'
    pk_url_kwarg = 'user_id'
    form_class = UpdateForm
    success_message = _('User updated successfully')
    self_delete_error_message = _("You're cannot update this user")
    extra_context = {
        'page_title': _('Update user'),
        'url_path': 'users_update',
    }


class UsersDelete(SuccessMessageMixin, RedirectToLoginMixin,
                  SelfUserCheckMixin, ProtectedObjectCheckMixin, DeleteView):
    template_name = 'manage/delete.html'
    model = User
    success_url = reverse_lazy('users_index')
    context_object_name = 'current_object'
    pk_url_kwarg = 'user_id'
    success_message = _('User deleted successfully')
    self_delete_error_message = _("You're cannot delete this user")
    protected_redirect_to = reverse_lazy('users_index')
    protected_message = _("Can't delete assigned user")
    extra_context = {
        'object_group': _('User')
    }
