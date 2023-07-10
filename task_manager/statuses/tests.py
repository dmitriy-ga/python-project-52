from django.test import TestCase
from .models import StatusModel
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestStatuses(TestCase):
    fixtures = ['fixture_all.json', ]
    status_example_after = {'name': 'status_example_after', }

    def setUp(self):
        self.client.force_login(User.objects.get(username='tester_user'))

    def test_status_index(self):
        status_index_url = reverse_lazy('statuses_index')
        response = self.client.get(status_index_url)
        self.assertEqual(response.status_code, 200)

    def test_status_create(self):
        success_message = _('Status created successfully')
        status_create_url = reverse_lazy('statuses_create')

        response = self.client.get(status_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(status_create_url,
                                    data=self.status_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        created_status = StatusModel.objects.get(
            name=self.status_example_after['name']
        )
        self.assertEqual(created_status.name, self.status_example_after['name'])

    def test_status_update(self):
        success_message = _('Status updated successfully')
        status_update_url = reverse_lazy('statuses_update', args=[1])

        response = self.client.get(status_update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(status_update_url,
                                    data=self.status_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        updated_status = StatusModel.objects.get(
            name=self.status_example_after['name']
        )
        self.assertEqual(updated_status.name, self.status_example_after['name'])

    def test_status_delete(self):
        status_index_url = reverse_lazy('statuses_index')
        status_delete_url = reverse_lazy('statuses_delete', args=[1])
        status_in_fixture = StatusModel.objects.get(id=1)
        success_message = _('Status deleted successfully')

        response = self.client.get(status_delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(status_delete_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(status_index_url)
        self.assertNotContains(response, status_in_fixture.name)
