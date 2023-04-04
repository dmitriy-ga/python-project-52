from django.test import TestCase
from .models import LabelModel


class TestLabel(TestCase):
    def test_label(self):
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
