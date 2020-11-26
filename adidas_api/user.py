import requests
import json
from hyper.contrib import HTTP20Adapter

from event import Event
from settings import header
from settings import me_header


class User:
    def __init__(self, email, password):
        self._accessToken = User.auth(email, password)
        self._me_url = "https://www.adidas.ru/adidasrunners/api/users/me"
        self._event = None
        self._event_header = None

    def add_event(self, event: Event):
        """
        Bind event to user
        """
        self._event = event

    def signed_up(self):
        assert self._event is not None
        url = f"https://www.adidas.ru/adidasrunners/api/events/{self._event.id}/signup"
        payload = json.dumps({
            "accessToken": self._accessToken,
            "adidasMarket": "RU"
        })
        response = requests.post(url, headers=self._event.header, data=payload)
        assert response.ok

    def check_signing(self):
        assert self._event is not None
        me_header_modified = self._form_me_header()
        sessions = User.create_session()
        response = sessions.get(self._me_url, headers=me_header_modified)
        assert response.ok
        user_signed_events = response.json()["data"]["events"]
        return self._event.check_signing(user_signed_events)
        


    def _form_me_header(self):
        me_header_modified = me_header.copy()
        me_header_modified["referer"] = self._event.url
        me_header_modified["x-access-token"] = self._accessToken
        return me_header_modified

    @property
    def event(self):
        """
        Return user event
        """
        return self._event

    @staticmethod
    def create_session():
        sessions = requests.session()
        sessions.mount("https://www.adidas.ru/", HTTP20Adapter())
        return sessions

    @staticmethod
    def auth(email: str, password: str):
        url = 'https://www.adidas.ru/adidasrunners/api/auth/login'
        data = {"email": email, "password": password, "adidasMarket": "RU"}
        response = requests.post(url, headers=header, data=json.dumps(data))
        assert response.ok
        return response.json()["data"]["accessToken"]