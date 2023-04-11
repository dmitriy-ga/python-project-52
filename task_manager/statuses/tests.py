from django.test import TestCase
from .models import StatusModel
from task_manager.users.models import User


class TestStatuses(TestCase):
    def test_statuses(self):
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
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)

        # Create
        response = self.client.get('/statuses/create/')
        self.assertEqual(response.status_code, 200)
        params = {'name': 'statusname', }
        response = self.client.post('/statuses/create/', data=params)
        self.assertEqual(response.status_code, 302)
        created_status = StatusModel.objects.get(name='statusname')
        self.assertEqual(created_status.name, params['name'])

        # Update
        response = self.client.get('/statuses/1/update/')
        self.assertEqual(response.status_code, 200)
        params = {'name': 'statusname2', }
        response = self.client.post('/statuses/1/update/', data=params)
        self.assertEqual(response.status_code, 302)
        updated_status = StatusModel.objects.get(name='statusname2')
        self.assertEqual(updated_status.name, params['name'])

        # Delete
        response = self.client.get('/statuses/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/statuses/1/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/statuses/')
        self.assertNotContains(response, params['name'])
