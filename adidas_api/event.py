import requests

from settings import header_event_api
from settings import header


class Event:
    def __init__(self, url: str):
        """
        Create an event instance from adidas api via request with slug from url
        """
        self._full_url = url
        self._slug = url.split("-_-")[-1]
        self._id = Event.get_data(self._slug)["id"]
        self._vacancies = Event._get_vacancies(self._slug)
        self._header = header.copy()
        self._header["Referer"] = self._full_url

    def has_vacancy(self) -> bool:
        """
        Check if there is vacancy in event
        """
        return self._vacancies > 0

    def update(self):
        """
        Updates vacancies of event from api
        """
        self._vacancies = Event._get_vacancies(self._slug)

    def check_signing(self, events: list):
        for event in events:
            if event["id"] == self._id:
                return True
        return False

    @property
    def id(self):
        """
        Return id attribute of event
        """
        return self._id

    @property
    def url(self):
        """
        Return full url to event
        """
        return self._full_url

    @property
    def header(self):
        """
        Return id attribute of event
        """
        return self._header

    @staticmethod
    def get_data(slug):
        """
        Retrieve event data from api with event slug
        """
        url = f"https://www.adidas.ru/adidasrunners/api/events/{slug}"
        response = requests.get(url, headers=header_event_api)
        assert response.ok
        data = response.json()["data"]
        return data

    @staticmethod
    def _get_vacancies(event_slug: str) -> int:
        """
        Retrieve vacancies for event.
        Return neagtive int if there are no vacancies otherwise return positive.
        """
        data = Event.get_data(event_slug)
        max_attendeens = data["maxAttendees"]
        nr_attendeens = data["nrAttendees"]
        return max_attendeens - nr_attendeens