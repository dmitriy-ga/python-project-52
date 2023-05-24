from django.contrib.auth.views import LoginView
from django.shortcuts import render
from task_manager.users.forms import LoginForm


def index(request):
    return render(request, 'index.html')


class ViewForLogin(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
