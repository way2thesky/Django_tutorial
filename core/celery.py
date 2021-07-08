import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'scraping-task': {
        'task': 'scraping.tasks.scraping_quotes',
        'schedule': crontab(hour='1-23/2')

    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # noqa: T001
