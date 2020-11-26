import requests
import json

from event import Event
from settings import header


class User:
    def __init__(self, email, password):
        self._accessToken = User.auth(email, password)
        self._event = None

    def add_event(self, event: Event):
        """
        Bind event to user
        """
        self._event = event

    def signed_up(self):
        url = f"https://www.adidas.ru/adidasrunners/api/events/{self._event.id}/signup"
        sign_header = header.copy()
        sign_header["Referer"] = self._event.url
        payload = json.dumps({
            "accessToken": self._accessToken,
            "adidasMarket": "RU"
        })
        response = requests.post(url, headers=header, data=payload)
        assert response.ok

    @property
    def event(self):
        """
        Return user event
        """
        return self._event

    @staticmethod
    def auth(email: str, password: str):
        url = 'https://www.adidas.ru/adidasrunners/api/auth/login'
        data = {"email": email, "password": password, "adidasMarket": "RU"}
        response = requests.post(url, headers=header, data=json.dumps(data))
        assert response.ok
        return response.json()["data"]["accessToken"]