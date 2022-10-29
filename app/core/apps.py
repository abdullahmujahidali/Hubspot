from django.apps import AppConfig

from core.cron import CronJob


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        job = CronJob()
        job.start()