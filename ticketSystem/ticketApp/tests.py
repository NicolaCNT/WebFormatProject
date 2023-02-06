from django.test import TestCase
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import *


class TestUrls(TestCase):

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func.view_class, Dashboard)

    def test_create_task_url_resolves(self):
        url = reverse('create_task')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)

    def test_remove_task_url_resolves(self):
        tasks_to_remove = Task.objects.all()
        for task in tasks_to_remove:
            url = reverse(TaskRemove, args=(task.id))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        