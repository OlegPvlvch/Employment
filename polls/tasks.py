import requests
#import json

from myproject.celery_app import app

from .models import Worker


@app.task(name='get_workers')
def get_workers():
    resp = requests.get('https://jsonplaceholder.typicode.com/users')
    workers_list = resp.json()

    for worker in workers_list:
        Worker.objects.create(
            name=worker['name']
        )