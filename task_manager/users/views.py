from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import SignupForm, UpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import RedirectToLoginMixin
from .mixins import SelfUserCheckMixin
from django.utils.translation import gettext as _


class UsersIndex(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UsersCreate(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = SignupForm
    success_message = _('User signed up successfully')


class UsersUpdate(SuccessMessageMixin, RedirectToLoginMixin,
                  SelfUserCheckMixin, UpdateView):
    template_name = 'users/update.html'
    model = User
    success_url = reverse_lazy('users_index')
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    form_class = UpdateForm
    success_message = _('User updated successfully')
    denied_message = _("You're cannot update this user")


class UsersDelete(SuccessMessageMixin, RedirectToLoginMixin,
                  SelfUserCheckMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users_index')
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    success_message = _('User deleted successfully')
    denied_message = _("You're cannot delete this user")
