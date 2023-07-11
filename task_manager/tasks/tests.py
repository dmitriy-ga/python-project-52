import json
from django.test import TestCase
from task_manager.tasks.models import TaskModel
from task_manager.users.models import User
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class TestTasks(TestCase):
    fixtures = ['fixture_all.json', ]

    def setUp(self):
        with open('task_manager/fixtures/task_example_after.json') as f:
            self.task_example_after = json.load(f)

        self.client.force_login(User.objects.get(username='tester_task2'))

    def test_tasks_index(self):
        task_index_url = reverse_lazy('tasks_index')
        response = self.client.get(task_index_url)
        self.assertEqual(response.status_code, 200)

    def test_tasks_create(self):
        success_message = _('Task created successfully')
        task_create_url = reverse_lazy('tasks_create')

        response = self.client.get(task_create_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(task_create_url,
                                    data=self.task_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        created_task = TaskModel.objects.get(
            name=self.task_example_after['name']
        )
        self.assertEqual(created_task.name, self.task_example_after['name'])

    def test_tasks_update(self):
        success_message = _('Task updated successfully')
        task_update_url = reverse_lazy('tasks_update', args=[1])
        response = self.client.get(task_update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(task_update_url,
                                    data=self.task_example_after,
                                    follow=True)
        self.assertContains(response, success_message)

        updated_task = TaskModel.objects.get(
            name=self.task_example_after['name']
        )
        self.assertEqual(updated_task.name, self.task_example_after['name'])

    def test_tasks_delete(self):
        self_task_in_fixture = TaskModel.objects.get(id=1)
        non_self_task_in_fixture = TaskModel.objects.get(id=2)

        success_message = _('Task deleted successfully')
        protected_message = _('Only author can delete this task')

        task_index_url = reverse_lazy('tasks_index')
        non_self_task_delete_url = reverse_lazy('tasks_delete', args=[1])
        self_task_delete_url = reverse_lazy('tasks_delete', args=[2])

        # Checking deleting self task
        response = self.client.get(non_self_task_delete_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(non_self_task_delete_url, follow=True)
        self.assertContains(response, success_message)

        response = self.client.get(task_index_url)
        self.assertNotContains(response, self_task_in_fixture.name)

        # Checking deleting non-self task
        response = self.client.get(self_task_delete_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(self_task_delete_url, follow=True)
        self.assertContains(response, protected_message)

        response = self.client.get(task_index_url)
        self.assertContains(response, non_self_task_in_fixture.name)

    def test_tasks_filter(self):
        task_index_url = reverse_lazy('tasks_index')
        task_example = TaskModel.objects.get(id='1')
        filter_task_example = TaskModel.objects.get(id='2')

        response = self.client.get(task_index_url, {'status': 2,
                                                    'executor': 2})
        self.assertContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)

        response = self.client.get(task_index_url, {'self_task': 'on'})
        self.assertContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)

        response = self.client.get(task_index_url, {'status': 1})
        self.assertNotContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)
