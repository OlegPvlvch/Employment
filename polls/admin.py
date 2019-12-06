from django.contrib import admin

from .models import Company, Manager, Job, WorkPlace, Worker, WorkTime

admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Job)
admin.site.register(WorkPlace)
admin.site.register(Worker)
admin.site.register(WorkTime)