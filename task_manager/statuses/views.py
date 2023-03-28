from django.shortcuts import render, redirect
from django.views import View
from .models import StatusModel
from .forms import StatusForm


class StatusesIndex(View):

    def get(self, request, *args, **kwargs):
        statuses = StatusModel.objects.all()
        return render(request, 'statuses/index.html',
                      context={'statuses': statuses})


class StatusesCreate(View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'statuses/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('statuses_index')
        return render(request, 'statuses/create.html', context={'form': form})


class StatusesUpdate(View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('status_id')
        status = StatusModel.objects.get(id=status_id)
        form = StatusForm(instance=status)
        context = {'form': form, 'status_id': status_id}
        return render(request, 'statuses/update.html', context)

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('status_id')
        status = StatusModel.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('statuses_index')
        context = {'form': form, 'status_id': status_id}
        return render(request, 'statuses/update.html', context)


class StatusesDelete(View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('status_id')
        status = StatusModel.objects.get(id=status_id)
        return render(request, 'statuses/delete.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('status_id')
        status = StatusModel.objects.get(id=status_id)
        if status:
            status.delete()
        return redirect('statuses_index')
