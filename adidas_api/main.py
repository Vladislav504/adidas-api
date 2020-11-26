import requests
import json
import sys

from cli_arguments import CLI_args
from user import User
from event import Event
from monitor import Monitor

if __name__ == "__main__":
    try:
        arguments = CLI_args(sys.argv)
        user = User(arguments.email, arguments.password)
        event = Event(arguments.event_url)
        user.add_event(event)
        monitor = Monitor(user)
        monitor.process(arguments.notify_email)
    except Exception as e:
        print("Something went wrong!", e.args)
