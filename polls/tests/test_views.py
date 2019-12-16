from django.test import TestCase
from polls.models import Company, Worker
from django.urls import reverse

class TestHomePage(TestCase):
    def setUp(self):
        cp = Company.objects.create(
            company_name='TestName'
        )
    
    def test_homepage(self):
        resp = self.client.get(reverse('index'))
        self.assertTrue(resp.context['object_list'])

class TestCompanyDetails(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_name='TestName'
        )
    
    def test_company_details(self):
        resp = self.client.get(
            reverse('get_details', args=[self.company.id]))
        self.assertTrue(resp.context['company'])

class TestWorkerDetails(TestCase):
    def setUp(self):
        self.worker = Worker.objects.create(
            name = "TestName"
        )
    
    def test_worker_details(self):
        resp = self.client.get(
            reverse('worker_details', args=[self.worker.id])
        )
        self.assertEqual(resp.context['worker'], self.worker)