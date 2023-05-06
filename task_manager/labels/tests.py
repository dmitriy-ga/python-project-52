from django.test import TestCase
from .models import LabelModel
from task_manager.users.models import User


class TestLabel(TestCase):
    def setUp(self):
        # Example labels for CRUD
        self.label_example_UD = {'name': 'label_example_UD', }
        self.label_example_C = {'name': 'label_example_C', }

        User.objects.create(username='label_tester',
                            first_name='labeler_name',
                            last_name='testlabel')
        self.client.force_login(User.objects.get(username='label_tester'))
        self.client.post('/labels/create/', data=self.label_example_UD)

    def test_label_index(self):
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 200)

    def test_label_create(self):
        response = self.client.get('/labels/create/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/labels/create/',
                                    data=self.label_example_C)
        self.assertEqual(response.status_code, 302)

        created_label = LabelModel.objects.get(name='label_example_C')
        self.assertEqual(created_label.name, self.label_example_C['name'])

    def test_label_update(self):
        response = self.client.get('/labels/1/update/')
        self.assertEqual(response.status_code, 200)

        label_new = {'name': 'labelname2', }
        response = self.client.post('/labels/1/update/', data=label_new)
        self.assertEqual(response.status_code, 302)

        updated_label = LabelModel.objects.get(name='labelname2')
        self.assertEqual(updated_label.name, label_new['name'])

    def test_label_delete(self):
        response = self.client.get('/labels/1/delete/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/labels/1/delete/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/labels/')
        self.assertNotContains(response, self.label_example_UD['name'])
