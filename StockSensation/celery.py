from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockSensation.settings')

app = Celery('StockSensation')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add_func_every_5sec':{
        'task': 'StockVisualData.tasks.add',
        'schedule': 5.0,
        'args': (5, 6)
    }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))