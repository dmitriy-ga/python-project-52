from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.models import User
from task_manager.users.forms import SignupForm


class UsersIndex(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={'users': users})


class UsersCreate(View):

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return render(request, 'users/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'users/create.html', context={'form': form})


class UsersUpdate(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.get(id=user_id)
        form = SignupForm(instance=user)
        context = {'form': form, 'user_id': user_id}
        return render(request, 'users/update.html', context)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.get(id=user_id)
        form = SignupForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_index')
        context = {'form': form, 'user_id': user_id}
        return render(request, 'users/update.html', context)


class UsersDelete(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users_index')
