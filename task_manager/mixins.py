from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class RedirectToLoginMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request, _("You're not logged in, please login")
            )
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class ProtectedObjectCheckMixin:

    protected_redirect_to = ''
    protected_message = 'Protected object'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request, self.protected_message)
            return redirect(self.protected_redirect_to)
