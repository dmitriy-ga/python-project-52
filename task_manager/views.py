from django.contrib.auth.views import LoginView
from django.shortcuts import render
from task_manager.users.forms import LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'index.html')


class ViewForLogin(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_message = _('You are logged in')
