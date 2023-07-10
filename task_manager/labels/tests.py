from django.test import TestCase
from .models import LabelModel
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestLabel(TestCase):
    fixtures = ['fixture_all.json', ]
    label_example_after = {'name': 'label_example_after', }

    def setUp(self):
        self.client.force_login(User.objects.get(username='tester_user'))

    def test_label_index(self):
        label_index_url = reverse_lazy('labels_index')
        response = self.client.get(label_index_url)
        self.assertEqual(response.status_code, 200)

    def test_label_create(self):
        success_message = _('Label created successfully')
        label_create_url = reverse_lazy('labels_create')

        response = self.client.get(label_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(label_create_url,
                                    data=self.label_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        created_label = LabelModel.objects.get(
            name=self.label_example_after['name']
        )
        self.assertEqual(created_label.name, self.label_example_after['name'])

    def test_label_update(self):
        success_message = _('Label updated successfully')
        label_update_url = reverse_lazy('labels_update', args=[1])

        response = self.client.get(label_update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(label_update_url,
                                    data=self.label_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        updated_label = LabelModel.objects.get(
            name=self.label_example_after['name']
        )
        self.assertEqual(updated_label.name, self.label_example_after['name'])

    def test_label_delete(self):
        label_index_url = reverse_lazy('labels_index')
        label_delete_url = reverse_lazy('labels_delete', args=[1])
        label_in_fixture = LabelModel.objects.get(id=1)
        success_message = _('Label deleted successfully')

        response = self.client.get(label_delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(label_delete_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(label_index_url)
        self.assertNotContains(response, label_in_fixture.name)
