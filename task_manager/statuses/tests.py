from django.test import TestCase
from .models import StatusModel
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestStatuses(TestCase):
    fixtures = ['fixture_all.json', ]
    status_example_after = {'name': 'status_example_after', }

    status_index_url = reverse_lazy('statuses_index')
    status_create_url = reverse_lazy('statuses_create')
    status_update_1_url = reverse_lazy('statuses_update', args=[1])
    status_delete_1_url = reverse_lazy('statuses_delete', args=[1])

    def setUp(self):
        self.client.force_login(User.objects.get(username='tester_user'))

    def test_status_index(self):
        response = self.client.get(self.status_index_url)
        self.assertEqual(response.status_code, 200)

    def test_status_create(self):
        success_message = _('Status created successfully')

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
        success_message = _('Status updated successfully')

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
        success_message = _('Status deleted successfully')

        response = self.client.get(self.status_delete_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.status_delete_1_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(self.status_index_url)
        self.assertNotContains(response, status_in_fixture.name)
