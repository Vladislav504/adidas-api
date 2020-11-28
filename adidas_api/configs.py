from betterconf import Config, field
from betterconf.config import AbstractProvider

import json


class JSONProvider(AbstractProvider):
    def __init__(self, path: str):
        self._cread_path = path
        with open(path, "r") as f:
            self._settings = json.load(f)

    def get(self, name):
        return self._settings.get(name)


class UserConfig(Config):
    def __init__(self, provider):
        self._email = field("email", provider=provider)
        self._password = field("password", provider=provider)
        self._notify_email = field("notification email", provider=provider)

    @property
    def email(self):
        return self._email.value

    @property
    def password(self):
        return self._password.value

    @property
    def notify_email(self):
        return self._notify_email.value