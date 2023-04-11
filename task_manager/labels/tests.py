from django.test import TestCase
from .models import LabelModel
from task_manager.users.models import User


class TestLabel(TestCase):
    def test_label(self):
        # Create user and login
        params = {
            'username': 'author_user',
            'first_name': 'Somename2',
            'last_name': 'Somesurname2',
            'password1': 'somelongpassword',
            'password2': 'somelongpassword',
        }
        response = self.client.post('/users/create/', data=params)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(User.objects.get(username='author_user'))

        # Index
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 200)

        # Create
        response = self.client.get('/labels/create/')
        self.assertEqual(response.status_code, 200)
        params = {'name': 'labelname', }
        response = self.client.post('/labels/create/', data=params)
        self.assertEqual(response.status_code, 302)
        created_label = LabelModel.objects.get(name='labelname')
        self.assertEqual(created_label.name, params['name'])

        # Update
        response = self.client.get('/labels/1/update/')
        self.assertEqual(response.status_code, 200)
        params = {'name': 'labelname2', }
        response = self.client.post('/labels/1/update/', data=params)
        self.assertEqual(response.status_code, 302)
        updated_label = LabelModel.objects.get(name='labelname2')
        self.assertEqual(updated_label.name, params['name'])

        # Delete
        response = self.client.get('/labels/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/labels/1/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/labels/')
        self.assertNotContains(response, params['name'])
