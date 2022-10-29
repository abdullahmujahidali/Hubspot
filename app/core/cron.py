from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime

from core.factories.user import UserFactory

import logging

logger = logging.getLogger(__name__)

class CronJob:
    """Class for cron job."""

    def __init__(self):
        self.seconds=500
        pass

    def print_hello(self):
        print("HI: ", self.seconds)

    def start(self):
        scheduler = BackgroundScheduler(timezone="Europe/Berlin")
        scheduler.add_job(self.print_hello, 'interval', seconds=self.seconds)
        scheduler.start()