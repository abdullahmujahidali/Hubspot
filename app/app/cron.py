import json
import requests
import logging
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from core.factories.user import UserFactory


logger = logging.getLogger(__name__)

class CronJob:
    """Class for cron job."""

    def __init__(self):
        self.seconds=900 # 15 minutes interval
        pass

    def search_user(self, email):
        result = requests.get('https://api.hubapi.com/contacts/v1/contact/email/${email}/profile',
            headers={
                'Authorization': 'Bearer pat-na1-ba52c54e-b47c-416a-88d3-1ba19d5dcacb',
                'Content-Type': 'application/json'
            },
        )
        return result

    def create_user(self, user):
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
                        "value": user.email},
                        {"property": "firstname",
                        "value": user.first_name},
                        {"property": "lastname",
                        "value": user.last_name},
                    ]
                }
            ),
        )
        output = json.loads(res.content)
        return output

    def task_tbd(self):
        """Task to be done."""

        #create 2 fake users
        self.user1 = UserFactory.create()
        self.user2 = UserFactory.create()

        result = self.search_user(self.user1.email)
        if result.status_code == 404: # if 404 means user doesn't exists in that case create a new user
            output = self.create_user(self.user1)
            self.user1.hubspot_id =output["vid"]
            self.user1.save()
        else:
            # wasn't clear what to update in the document
            pass

        result = self.search_user(self.user2.email)
        if result.status_code == 404: # if 404 means user doesn't exists in that case create a new user
            output = self.create_user(self.user2)
            self.user2.hubspot_id =output["vid"]
            self.user2.save()
        else:
            # wasn't clear what to update in the document
            pass

    def start(self):
        scheduler = BackgroundScheduler(timezone="Europe/Berlin")
        scheduler.add_job(self.task_tbd, 'interval', seconds=self.seconds)
        scheduler.start()