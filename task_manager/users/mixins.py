from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


class SelfUserCheckMixin(UserPassesTestMixin):
    self_delete_error_message = 'Action denied'

    def test_func(self):
        return self.request.user.id == self.get_object().id

    def handle_no_permission(self):
        messages.error(self.request, self.self_delete_error_message)
        return redirect(reverse_lazy('users_index'))
