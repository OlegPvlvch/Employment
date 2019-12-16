from django.test import TestCase
from polls.models import (
    Company, Manager, WorkPlace, Job, Worker)

class CompanyModelTest(TestCase):
    def test_company(self):
        cp = Company.objects.create(
            company_name='TestName'
        )
        self.assertNotEqual(cp.id, None)
        self.assertEqual(cp.company_name, 'TestName')


class ManagerModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_name="TestCp"
        )
        self.manager = Manager.objects.create(
            name="Manager Test",
            company = self.company
        )
    
    def test_manager(self):
        self.assertIsNotNone(self.manager.company)
        self.assertEqual(
            self.manager.company.company_name, 'TestCp')

class WorkplaceModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_name='TestCp'
        )
        self.job = Job.objects.create(
            name='TestJb',
            company = self.company
        )
        self.worker = Worker.objects.create(
            name = 'TestWr'
        )
        self.workplace = WorkPlace.objects.create(
            job=self.job,
            worker=self.worker
        )
    
    def test_workplace(self):
        self.assertEqual(self.workplace.status, 'New')
        self.assertIsNotNone(self.workplace.worker)
        self.assertIsNotNone(self.workplace.job)