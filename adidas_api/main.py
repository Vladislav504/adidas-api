import requests
import json
import sys
from stem import Signal
from stem.control import Controller

from CLI import CLI_args
from user import User
from event import Event
from monitor import Monitor
import configs


def main(arguments):
    provider = configs.JSONProvider(arguments.cred_path)
    config = configs.UserConfig(provider)
    user = User(config.email, config.password)
    event = Event(arguments.event_url)
    user.add_event(event)
    monitor = Monitor(user)
    return monitor.process(config.notify_email)
    

if __name__ == "__main__":
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password='1234')
        print("Success!")
        controller.signal(Signal.NEWNYM)
        print("New Tor connection processed")
    arguments = CLI_args(sys.argv)
    print("================================")
    print("The script is called with arguments: ")
    print(arguments)
    try:
        is_signed_up = main(arguments)
        print("User is signed up to event:", is_signed_up)
    except Exception as e:
        print("----Something went wrong!----", e.args)
    print("================================")
