import requests
import datetime
from myproject.celery_app import app
from django.utils import timezone
from myproject.celery_app import app
from .models import Worker, Statistic, WorkPlace
from django.core.mail import send_mail


@app.task(name='polls.tasks.get_workers')
def get_workers():
    resp = requests.get('https://jsonplaceholder.typicode.com/users')
    workers_list = resp.json()

    for worker in workers_list:
        Worker.objects.create(
            name=worker['name']
        )

@app.task(name='polls.tasks.check_hours_limit')
def check_hours_limit():
    workplaces = WorkPlace.objects.filter(status='Approved')
    
    week_ago = timezone.now() - timezone.timedelta(days=7)

    for workplace in workplaces:
        total_time = workplace.worktime.date_end - week_ago
        if (total_time >= week):
            total_hours = total_time.hours + total_time.minute / 60

        if total_hours > workplace.week_hours_limit:
            worker = workplace.worker.name
            hours = total_hours
            email = workplace.manager.email
            app.send_task(
                'send_mail_if_overtime', args = [worker, hours, email])

@app.task(name='polls.tasks.send_message_if_overtime')
def send_message_if_overtime(worker, hours, email):
    send_mail(
        subject='Your worker exceed the limit of hours',
        message='Worker: %s. Total hours %s' % (worker, hours),
        from_email='somemail@gmail.com',
        recipient_list=(email,),
        fail_silently=False
    )

