from django.test import TestCase
from .models import User


class TestUsers(TestCase):
    def test_users(self):
        # Index
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

        # Create
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)
        params = {
            'username': 'tester_app',
            'first_name': 'Somename',
            'last_name': 'Somesurname',
            'password1': 'somelongpassword',
            'password2': 'somelongpassword',
        }
        response = self.client.post('/users/create/', data=params)
        self.assertEqual(response.status_code, 302)
        created_user = User.objects.get(first_name='Somename')
        self.assertEqual(created_user.first_name, params['first_name'])

        # Update
        response = self.client.get('/users/1/update/')
        self.assertEqual(response.status_code, 200)
        params = {
            'username': 'tester_app',
            'first_name': 'Somename2',
            'last_name': 'Somesurname2',
            'password1': 'somelongpassword2',
            'password2': 'somelongpassword2',
        }
        response = self.client.post('/users/1/update/', data=params)
        self.assertEqual(response.status_code, 302)
        updated_user = User.objects.get(first_name='Somename2')
        self.assertEqual(updated_user.first_name, params['first_name'])

        # Delete
        response = self.client.get('/users/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/users/1/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/users/')
        self.assertNotContains(response, params['first_name'])
