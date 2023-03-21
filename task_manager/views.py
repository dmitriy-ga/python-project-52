from django.contrib.auth.views import LoginView
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class ViewForLogin(LoginView):
    template_name = 'login.html'
