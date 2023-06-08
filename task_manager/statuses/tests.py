from django.test import TestCase
from .models import StatusModel
from task_manager.users.models import User
import os.path


class TestStatuses(TestCase):
    fixtures = ['fixture_all.json', ]
    status_example_after = {'name': 'status_example_after', }

    status_index_url = os.path.join('/', 'statuses', '')
    status_create_url = os.path.join(status_index_url, 'create', '')
    status_update_1_url = os.path.join(status_index_url, '1', 'update', '')
    status_delete_1_url = os.path.join(status_index_url, '1', 'delete', '')

    def setUp(self):
        self.client.force_login(User.objects.get(username='tester_user'))

    def test_status_index(self):
        response = self.client.get(self.status_index_url)
        self.assertEqual(response.status_code, 200)

    def test_status_create(self):
        success_message = 'Статус успешно создан'

        response = self.client.get(self.status_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.status_create_url,
                                    data=self.status_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        created_status = StatusModel.objects.get(
            name=self.status_example_after['name']
        )
        self.assertEqual(created_status.name, self.status_example_after['name'])

    def test_status_update(self):
        success_message = 'Статус успешно изменен'

        response = self.client.get(self.status_update_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.status_update_1_url,
                                    data=self.status_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        updated_status = StatusModel.objects.get(
            name=self.status_example_after['name']
        )
        self.assertEqual(updated_status.name, self.status_example_after['name'])

    def test_status_delete(self):
        status_in_fixture = StatusModel.objects.get(id=1)
        success_message = 'Статус успешно удален'

        response = self.client.get(self.status_delete_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.status_delete_1_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(self.status_index_url)
        self.assertNotContains(response, status_in_fixture.name)
