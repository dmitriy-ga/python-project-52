from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
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
