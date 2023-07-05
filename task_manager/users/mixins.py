from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


class SelfUserCheckMixin(UserPassesTestMixin):
    denied_message = 'Action denied'

    def test_func(self):
        return all((self.request.user.is_authenticated,
                    self.request.user.id == self.get_object().id))

    def handle_no_permission(self):
        messages.error(self.request, self.denied_message)
        return redirect(reverse_lazy('users_index'))
