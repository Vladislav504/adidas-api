class CLI_args:
    def __init__(self, sys_: list):
        self.event_url = sys_[1]
        self.cred_path = sys_[2]

    def __str__(self):
        return f"Event url: {self.event_url}\nCred_path: {self.cred_path}"
