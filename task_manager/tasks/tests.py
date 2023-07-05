from django.test import TestCase

from task_manager.tasks.models import TaskModel
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestTasks(TestCase):
    fixtures = ['fixture_all.json', ]
    task_example_after = {
        'name': 'TestTask',
        'description': 'This is testing task',
        'executor': '1',
        'status': '1',
    }

    task_index_url = reverse_lazy('tasks_index')
    task_create_url = reverse_lazy('tasks_create')
    task_update_1_url = reverse_lazy('tasks_update', args=[1])
    task_delete_1_url = reverse_lazy('tasks_delete', args=[1])

    def setUp(self):
        self.client.force_login(User.objects.get(username='tester_task2'))

    def test_tasks_index(self):
        response = self.client.get(self.task_index_url)
        self.assertEqual(response.status_code, 200)

    def test_tasks_create(self):
        success_message = _('Task created successfully')

        response = self.client.get(self.task_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.task_create_url,
                                    data=self.task_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        created_task = TaskModel.objects.get(
            name=self.task_example_after['name']
        )
        self.assertEqual(created_task.name, self.task_example_after['name'])

    def test_tasks_update(self):
        success_message = _('Task updated successfully')
        response = self.client.get(self.task_update_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.task_update_1_url,
                                    data=self.task_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        updated_task = TaskModel.objects.get(
            name=self.task_example_after['name']
        )
        self.assertEqual(updated_task.name, self.task_example_after['name'])

    def test_tasks_delete(self):
        task_in_fixture = TaskModel.objects.get(id=1)
        success_message = _('Task deleted successfully')

        response = self.client.get(self.task_delete_1_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.task_delete_1_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(self.task_index_url)
        self.assertNotContains(response, task_in_fixture.name)

    def test_tasks_filter(self):
        task_example = TaskModel.objects.get(id='1')
        filter_task_example = TaskModel.objects.get(id='2')

        response = self.client.get(self.task_index_url, {'status': 2,
                                                         'executor': 2})
        self.assertContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)

        response = self.client.get(self.task_index_url, {'self_task': 'on'})
        self.assertContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)

        response = self.client.get(self.task_index_url, {'status': 1})
        self.assertNotContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)
