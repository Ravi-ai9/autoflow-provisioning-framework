from core.state_machine import State

class Orchestrator:

    def __init__(self):
        self.state = State.BOOTSTRAP

    def run(self):
        while self.state != State.DONE:
            print(f"Running: {self.state}")

            if self.state == State.BOOTSTRAP:
                self.state = State.PRECHECK

            elif self.state == State.PRECHECK:
                self.state = State.IFWI

            elif self.state == State.IFWI:
                self.state = State.BIOS

            elif self.state == State.BIOS:
                self.state = State.OS

            elif self.state == State.OS:
                self.state = State.CLEANUP

            elif self.state == State.CLEANUP:
                self.state = State.DONE

        print("Pipeline Completed!")