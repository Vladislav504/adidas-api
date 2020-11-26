class CLI_args:
    def __init__(self, sys_: list):
        self.event_url = sys_[1]
        self.email = sys_[2]
        self.password = sys_[3]
        self.notify_email = sys_[4]

    def __str__(self):
        return f"Event url: {self.event_url}\nEmail: {self.email}\nPassword: {self.password}\nNotify email: {self.notify_email}"