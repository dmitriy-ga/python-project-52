from django.test import TestCase
from .models import User
import os.path


class TestUsers(TestCase):
    fixtures = ['fixture_all.json', ]

    user_index_url = os.path.join('/', 'users', '')
    user_create_url = os.path.join(user_index_url, 'create', '')
    user_update_1_url = os.path.join(user_index_url, '1', 'update', '')
    user_delete_1_url = os.path.join(user_index_url, '1', 'delete', '')

    user_after = {
        'username': 'tester_app',
        'first_name': 'Somename',
        'last_name': 'Somesurname',
        'password1': 'somelongpassword',
        'password2': 'somelongpassword',
    }

    def setUp(self):
        self.user_in_fixture = User.objects.get(id=1)

    def test_users_index(self):
        response = self.client.get(self.user_index_url)
        self.assertEqual(response.status_code, 200)

    def test_users_create(self):
        success_message = 'Пользователь успешно зарегистрирован'
        response = self.client.get(self.user_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.user_create_url,
                                    data=self.user_after, follow=True)
        self.assertContains(response, success_message)

        created_user = User.objects.get(username=self.user_after['username'])
        self.assertEqual(created_user.username, self.user_after['username'])

    def test_users_update(self):
        success_message = 'Пользователь успешно изменен'
        self.client.force_login(self.user_in_fixture)

        response = self.client.get(self.user_update_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.user_update_1_url,
                                    data=self.user_after, follow=True)
        self.assertContains(response, success_message)

        updated_user = User.objects.get(username=self.user_after['username'])
        self.assertEqual(updated_user.username, self.user_after['username'])

    def test_users_delete(self):
        success_message = 'Пользователь успешно удален'
        self.client.force_login(self.user_in_fixture)

        response = self.client.get(self.user_delete_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.user_delete_1_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(self.user_index_url)
        self.assertNotContains(response, self.user_in_fixture.username)
