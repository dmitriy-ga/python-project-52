from django.test import TestCase

from task_manager.tasks.models import TaskModel
from task_manager.users.models import User
from task_manager.statuses.models import StatusModel


class TestTasks(TestCase):
    def setUp(self):
        StatusModel.objects.create(name='statusname')
        StatusModel.objects.create(name='statusname2')

        User.objects.create(username='executer_user',
                            first_name='tasker_executor',
                            last_name='surname_executor')

        User.objects.create(username='author_user',
                            first_name='tasker_author',
                            last_name='surname_author')
        self.client.force_login(User.objects.get(username='author_user'))

        self.task_example_ud = {
            'name': 'TestTask2',
            'description': 'This testing task, updated',
            'executor': '1',
            'status': '1',
        }
        self.client.post('/tasks/create/', data=self.task_example_ud)

    def test_tasks_index(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_tasks_create(self):
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 200)

        task_example_c = {
            'name': 'TestTask',
            'description': 'This testing task',
            'executor': '1',
            'status': '1',
        }
        response = self.client.post('/tasks/create/', data=task_example_c)
        self.assertEqual(response.status_code, 302)
        created_task = TaskModel.objects.get(name='TestTask')
        self.assertEqual(created_task.name, task_example_c['name'])

    def test_tasks_update(self):
        response = self.client.get('/tasks/1/update/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/tasks/1/update/',
                                    data=self.task_example_ud)
        self.assertEqual(response.status_code, 302)

        updated_task = TaskModel.objects.get(name='TestTask2')
        self.assertEqual(updated_task.name, self.task_example_ud['name'])

    def test_tasks_delete(self):
        response = self.client.get('/tasks/1/delete/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/tasks/1/delete/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/tasks/')
        self.assertNotContains(response, self.task_example_ud['name'])

    def test_tasks_filter(self):
        TaskModel.objects.create(
            name='Filtertest', description='sometext',
            author_id='1', executor_id='2', status_id='1'
        )
        task_example = TaskModel.objects.get(id='1')
        filter_task_example = TaskModel.objects.get(id='2')

        response = self.client.get('/tasks/?status=1&executor=1')
        self.assertContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)

        response = self.client.get('/tasks/?self_task=on')
        self.assertContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)

        response = self.client.get('/tasks/?status=2')
        self.assertNotContains(response, task_example.name)
        self.assertNotContains(response, filter_task_example.name)
