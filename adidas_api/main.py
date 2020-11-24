import time
import requests
import json

from user import User
from event import Event
from monitor import Monitor


if __name__ == "__main__":
    notify_email = "vvkovyazin@miem.hse.ru"
    user = User("vvkovyazin@miem.hse.ru", "")
    event = Event(
        "https://www.adidas.ru/adidasrunners/community/moscow/event/ar-atrium-142?cm_sp=RUNNING_HUB-_-LOGGEDIN-_-AR-ATRIUM-142"
    )
    user.add_event(event)
    monitor = Monitor(user)
    monitor.start()
    
        

