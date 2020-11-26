from smtp import Emailing
from user import User


class Monitor:
    def __init__(self, user: User):
        """
        Create monitoring instance
        """
        self._user = user

    def process(self, notify_email):
        """
        Checks if there is vacancy and signs the user if free 
        """
        if self._user.check_signing():
            return True
        self._user.event.update()
        if self._user.event.has_vacancy():
            self._user.signed_up()
            emailing = Emailing(notify_email)
            emailing.send_email(self._user.event.url)
            return True
        return False