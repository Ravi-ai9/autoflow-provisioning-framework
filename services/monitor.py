import uuid

class Monitor:

    def __init__(self):
        self.guid = str(uuid.uuid4())
        self.status = {}

    def update(self, state, message):
        self.status[state] = message
        print(f"[MONITOR] {state} → {message}")

    def get_status(self):
        return self.status

    def get_guid(self):
        return self.guid