from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Manager(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 200)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class WorkPlace(models.Model):
    STATUS = (('New', 'New'), 
              ('Approved', 'Approved'), 
              ('Cancelled', 'Cancelled'), 
              ('Finished', 'Finished'))
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    week_hours_limit = models.IntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.job)+' in '+str(self.job.company)

class WorkTime(models.Model):
    STATUS = (('New', 'New'), 
              ('Approved', 'Approved'), 
              ('Cancelled', 'Cancelled'))
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    workplace = models.OneToOneField(WorkPlace, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_end-self.date_start)

class Statistic(models.Model):
    workplace = models.ForeignKey(WorkPlace, related_name='workplaces', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='workers', on_delete=models.CASCADE)
    start_record_date = models.DateTimeField(auto_now_add=True)