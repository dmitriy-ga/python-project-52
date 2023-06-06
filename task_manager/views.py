from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from task_manager.users.forms import LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class ViewForLogin(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_message = _('You are logged in')


class ViewForLogout(LogoutView):

    def get(self, request, *args, **kwargs):
        messages.success(self.request, _('You are logged out'))
        return super().get(request, *args, **kwargs)
