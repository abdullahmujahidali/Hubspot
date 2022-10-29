from apscheduler.schedulers.background import BackgroundScheduler


import json
import requests


from datetime import datetime

from core.factories.user import UserFactory

import logging

logger = logging.getLogger(__name__)

class CronJob:
    """Class for cron job."""

    def __init__(self):
        self.minutes=15
        pass

    def print_hello(self):
        pass
        self.user1 = UserFactory.create()
        self.user2 = UserFactory.create()
        res = requests.post(
            "https://api.hubapi.com/contacts/v1/contact/",
            headers={
                'Authorization': 'Bearer pat-na1-ba52c54e-b47c-416a-88d3-1ba19d5dcacb',
                'Content-Type': 'application/json'
            },
            data=json.dumps(
                {
                    "properties": [
                        {"property": "email",
                         "value": self.user1.email},
                        {"property": "firstname",
                         "value": self.user1.first_name},
                        {"property": "lastname",
                         "value": self.user1.last_name},
                    ]
                }
            ),
        )
        output = json.loads(res.content)
        self.user1.hubspot_id =output["identityProfile"]["vid"]
        self.user1.save()
        
        res = requests.post(
            "https://api.hubapi.com/contacts/v1/contact/",
            headers={
                'Authorization': 'Bearer pat-na1-ba52c54e-b47c-416a-88d3-1ba19d5dcacb',
                'Content-Type': 'application/json'
            },
            data=json.dumps(
                {
                    "properties": [
                        {"property": "email",
                         "value": self.user2.email},
                        {"property": "firstname",
                         "value": self.user2.first_name},
                        {"property": "lastname",
                         "value": self.user2.last_name},
                    ]
                }
            ),
        )
        output = json.loads(res.content)
        self.user2.hubspot_id =output["identityProfile"]["vid"]
        self.user2.save()

    def start(self):
        scheduler = BackgroundScheduler(timezone="Europe/Berlin")
        scheduler.add_job(self.print_hello, 'interval', minutes=self.minutes)
        scheduler.start()