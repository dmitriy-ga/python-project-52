from django.test import TestCase
from .models import LabelModel
from task_manager.users.models import User
import os.path


class TestLabel(TestCase):
    fixtures = ['fixture_all.json', ]
    label_example_after = {'name': 'label_example_after', }

    label_index_url = os.path.join('/', 'labels', '')
    label_create_url = os.path.join(label_index_url, 'create', '')
    label_update_1_url = os.path.join(label_index_url, '1', 'update', '')
    label_delete_1_url = os.path.join(label_index_url, '1', 'delete', '')

    def setUp(self):
        self.client.force_login(User.objects.get(username='tester_user'))

    def test_label_index(self):
        response = self.client.get(self.label_index_url)
        self.assertEqual(response.status_code, 200)

    def test_label_create(self):
        success_message = 'Метка успешно создана'

        response = self.client.get(self.label_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.label_create_url,
                                    data=self.label_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        created_label = LabelModel.objects.get(
            name=self.label_example_after['name']
        )
        self.assertEqual(created_label.name, self.label_example_after['name'])

    def test_label_update(self):
        success_message = 'Метка успешно изменена'

        response = self.client.get(self.label_update_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.label_update_1_url,
                                    data=self.label_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        updated_label = LabelModel.objects.get(
            name=self.label_example_after['name']
        )
        self.assertEqual(updated_label.name, self.label_example_after['name'])

    def test_label_delete(self):
        label_in_fixture = LabelModel.objects.get(id=1)
        success_message = 'Метка успешно удалена'

        response = self.client.get(self.label_delete_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.label_delete_1_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(self.label_index_url)
        self.assertNotContains(response, label_in_fixture.name)
