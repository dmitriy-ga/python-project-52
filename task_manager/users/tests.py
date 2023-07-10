import json
from django.test import TestCase
from .models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestUsers(TestCase):
    fixtures = ['fixture_all.json', ]

    def setUp(self):
        with open('task_manager/fixtures/user_after.json') as f:
            self.user_after = json.load(f)

    def test_users_index(self):
        user_index_url = reverse_lazy('users_index')
        response = self.client.get(user_index_url)
        self.assertEqual(response.status_code, 200)

    def test_users_create(self):
        success_message = _('User signed up successfully')
        user_create_url = reverse_lazy('users_create')
        response = self.client.get(user_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(user_create_url,
                                    data=self.user_after, follow=True)
        self.assertContains(response, success_message)

        created_user = User.objects.get(username=self.user_after['username'])
        self.assertEqual(created_user.username, self.user_after['username'])

    def test_users_update(self):
        success_message = _('User updated successfully')
        denied_message = _("You're cannot update this user")

        current_user = User.objects.get(id=1)
        other_user = User.objects.get(id=4)

        user_index_url = reverse_lazy('users_index')
        current_user_update_url = reverse_lazy('users_update', args=[1])
        other_user_update_url = reverse_lazy('users_update', args=[4])
        self.client.force_login(current_user)

        # Checking non-self update
        response = self.client.get(other_user_update_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(other_user_update_url, follow=True)
        self.assertContains(response, denied_message)

        response = self.client.get(user_index_url)
        self.assertContains(response, other_user.username)

        # Checking self update
        response = self.client.get(current_user_update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(current_user_update_url,
                                    data=self.user_after, follow=True)
        self.assertContains(response, success_message)

        updated_user = User.objects.get(username=self.user_after['username'])
        self.assertEqual(updated_user.username, self.user_after['username'])

    def test_users_delete(self):
        success_message = _('User deleted successfully')
        denied_message = _("You're cannot delete this user")

        current_user = User.objects.get(id=1)
        other_user = User.objects.get(id=4)

        user_index_url = reverse_lazy('users_index')
        current_user_delete_url = reverse_lazy('users_delete', args=[1])
        other_user_delete_url = reverse_lazy('users_delete', args=[4])
        self.client.force_login(current_user)

        # Checking non-self delete
        response = self.client.get(other_user_delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(other_user_delete_url, follow=True)
        self.assertContains(response, denied_message)

        response = self.client.get(user_index_url)
        self.assertContains(response, other_user.username)

        # Checking self delete
        response = self.client.get(current_user_delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(current_user_delete_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(user_index_url)
        self.assertNotContains(response, current_user.username)
