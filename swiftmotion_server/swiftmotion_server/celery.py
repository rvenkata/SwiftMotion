from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiftmotion_server.settings')
app = Celery('swiftmoition_server')

# Using a string allows worker to prevent 'pickling' object on windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r})'.format(self.reqeust))
