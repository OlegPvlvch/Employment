from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Manager(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Work_place(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE,
                                     primary_key=True)

    def __str__(self):
        return str(self.job) + ' in ' + str(self.company)
