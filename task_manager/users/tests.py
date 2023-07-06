import json
from django.test import TestCase
from .models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestUsers(TestCase):
    fixtures = ['fixture_all.json', ]

    with open('task_manager/fixtures/user_after.json') as f:
        user_after = json.load(f)

    def setUp(self):
        self.user_in_fixture = User.objects.get(id=1)

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
        user_update_1_url = reverse_lazy('users_update', args=[1])
        self.client.force_login(self.user_in_fixture)

        response = self.client.get(user_update_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(user_update_1_url,
                                    data=self.user_after, follow=True)
        self.assertContains(response, success_message)

        updated_user = User.objects.get(username=self.user_after['username'])
        self.assertEqual(updated_user.username, self.user_after['username'])

    def test_users_delete(self):
        success_message = _('User deleted successfully')
        user_index_url = reverse_lazy('users_index')
        user_delete_1_url = reverse_lazy('users_delete', args=[1])
        self.client.force_login(self.user_in_fixture)

        response = self.client.get(user_delete_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(user_delete_1_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(user_index_url)
        self.assertNotContains(response, self.user_in_fixture.username)
