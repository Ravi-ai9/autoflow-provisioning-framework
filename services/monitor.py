import uuid
from dashboard.app import status_store

class Monitor:

    def __init__(self):
        self.guid = str(uuid.uuid4())
        status_store[self.guid] = {}

    def update(self, state, message):
        status_store[self.guid][state] = message
        print(f"[MONITOR] {state} → {message}")

    def get_status(self):
        return status_store[self.guid]

    def get_guid(self):
        return self.guid