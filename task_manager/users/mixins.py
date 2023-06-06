from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SelfUserCheckMixin(LoginRequiredMixin):
    denied_message = 'Action denied'

    def dispatch(self, request, *args, **kwargs):
        if all((request.user.is_authenticated,
                request.user.id != self.get_object().id)):
            messages.error(self.request, self.denied_message)
            return redirect(reverse_lazy('users_index'))
        return super().dispatch(request, *args, **kwargs)
