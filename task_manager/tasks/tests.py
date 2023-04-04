from django.test import TestCase
from django.contrib.auth import get_user

from task_manager.tasks.models import TaskModel


class TestTasks(TestCase):
    def test_tasks(self):
        # Prepare users
        params = {
            'username': 'executer_user',
            'first_name': 'Somename1',
            'last_name': 'Somesurname1',
            'password1': 'somelongpassword',
            'password2': 'somelongpassword',
        }
        response = self.client.post('/users/create/', data=params)
        self.assertEqual(response.status_code, 302)

        params = {
            'username': 'author_user',
            'first_name': 'Somename2',
            'last_name': 'Somesurname2',
            'password1': 'somelongpassword',
            'password2': 'somelongpassword',
        }
        response = self.client.post('/users/create/', data=params)
        self.assertEqual(response.status_code, 302)

        # Login
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.login(username="author_user", password="somelongpassword")
        self.assertTrue(get_user(self.client).is_authenticated)

        # Prepare status
        params = {'name': 'statusname', }
        response = self.client.post('/statuses/create/', data=params)
        self.assertEqual(response.status_code, 302)

        # Index
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

        # Create
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 200)
        params = {
            'name': 'TestTask',
            'description': 'This testing task',
            'executor': '1',
            'status': '1',
        }
        response = self.client.post('/tasks/create/', data=params)
        self.assertEqual(response.status_code, 302)
        created_task = TaskModel.objects.get(name='TestTask')
        self.assertEqual(created_task.name, params['name'])

        # Update
        response = self.client.get('/tasks/1/update/')
        self.assertEqual(response.status_code, 200)
        params = {
            'name': 'TestTask2',
            'description': 'This testing task, updated',
            'executor': '1',
            'status': '1',
        }
        response = self.client.post('/tasks/1/update/', data=params)
        self.assertEqual(response.status_code, 302)
        updated_task = TaskModel.objects.get(name='TestTask2')
        self.assertEqual(updated_task.name, params['name'])

        # Delete
        response = self.client.get('/tasks/1/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/tasks/1/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/tasks/')
        self.assertNotContains(response, params['name'])
