from core.state_machine import State
from modules.ifwi import IFWI
from modules.bios import BIOS
from modules.os_install import OSInstall
from services.logger import Logger


class Orchestrator:

    def __init__(self):
        self.state = State.BOOTSTRAP
        self.logger = Logger()

        # modules
        self.ifwi = IFWI()
        self.bios = BIOS()
        self.os = OSInstall()

    def run(self):
        while self.state != State.DONE:

            self.logger.info(f"Running: {self.state}")

            if self.state == State.BOOTSTRAP:
                self.state = State.PRECHECK

            elif self.state == State.PRECHECK:
                self.state = State.IFWI

            elif self.state == State.IFWI:
                self.ifwi.run()   # 🔥 actual execution
                self.state = State.BIOS

            elif self.state == State.BIOS:
                self.bios.run()   # 🔥 actual execution
                self.state = State.OS

            elif self.state == State.OS:
                self.os.run()     # 🔥 actual execution
                self.state = State.CLEANUP

            elif self.state == State.CLEANUP:
                self.logger.info("Cleaning up system...")
                self.state = State.DONE

        self.logger.info("Pipeline Completed!")