from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class RedirectToLoginMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        messages.error(self.request, "You're not logged in, please login")
        return redirect(reverse_lazy('login'))
