from django.test import TestCase
from .models import User


class TestUsers(TestCase):
    def setUp(self):
        self.params = {
            'username': 'tester_app',
            'first_name': 'Somename',
            'last_name': 'Somesurname',
            'password1': 'somelongpassword',
            'password2': 'somelongpassword',
        }
        self.params_for_updated = {
            'username': 'created_user',
            'first_name': 'Somename2',
            'last_name': 'Somesurname2',
            'password1': 'somelongpassword2',
            'password2': 'somelongpassword2',
        }
        User.objects.create(username='created_user',
                            first_name='created_name',
                            last_name='anothersurname')

    def test_users_index(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_users_create(self):
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/users/create/', data=self.params)
        self.assertEqual(response.status_code, 302)

        created_user = User.objects.get(first_name='Somename')
        self.assertEqual(created_user.first_name, self.params['first_name'])

    def test_users_update(self):
        self.client.force_login(User.objects.get(username='created_user'))
        response = self.client.get('/users/1/update/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/users/1/update/',
                                    data=self.params_for_updated)
        self.assertEqual(response.status_code, 302)

        updated_user = User.objects.get(first_name='Somename2')
        self.assertEqual(updated_user.first_name,
                         self.params_for_updated['first_name'])

    def test_users_delete(self):
        self.client.force_login(User.objects.get(username='created_user'))
        response = self.client.get('/users/1/delete/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/users/1/delete/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/users/')
        self.assertNotContains(response, self.params_for_updated['first_name'])
