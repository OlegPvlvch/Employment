from django.contrib import admin

from .models import Company, Manager, Job, Work_place, Worker

admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Job)
admin.site.register(Work_place)
admin.site.register(Worker)
