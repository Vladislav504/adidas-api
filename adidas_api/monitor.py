import time

from user import User


class Monitor:
    def __init__(self, user: User):
        """
        Create monitoring instance
        """
        self._user = user
        self._max_wait = 10

    def start(self):
        """
        Starts monitoring on user events and automatically signes up if there is vacancy. 
        """
        event = self._user.event
        while not event.has_vacancy():
            event.update()
            time.sleep(self._max_wait * 60)
        self._user.signed_up()