from django.test import TestCase
from .models import StatusModel
from task_manager.users.models import User


class TestStatuses(TestCase):
    def setUp(self):
        # Example statuses for CRUD
        self.status_example_UD = {'name': 'status_example_UD', }
        self.status_example_C = {'name': 'status_example_C', }

        User.objects.create(username='status_tester',
                            first_name='statuser_name',
                            last_name='teststatus')
        self.client.force_login(User.objects.get(username='status_tester'))
        self.client.post('/statuses/create/', data=self.status_example_UD)

    def test_status_index(self):
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)

    def test_status_create(self):
        response = self.client.get('/statuses/create/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/statuses/create/',
                                    data=self.status_example_C)
        self.assertEqual(response.status_code, 302)

        created_status = StatusModel.objects.get(name='status_example_C')
        self.assertEqual(created_status.name, self.status_example_C['name'])

    def test_status_update(self):
        response = self.client.get('/statuses/1/update/')
        self.assertEqual(response.status_code, 200)

        status_new = {'name': 'statusname2', }
        response = self.client.post('/statuses/1/update/', data=status_new)
        self.assertEqual(response.status_code, 302)

        updated_status = StatusModel.objects.get(name='statusname2')
        self.assertEqual(updated_status.name, status_new['name'])

    def test_status_delete(self):
        response = self.client.get('/statuses/1/delete/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/statuses/1/delete/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/statuses/')
        self.assertNotContains(response, self.status_example_UD['name'])
