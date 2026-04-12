from enum import Enum

class State(Enum):
    BOOTSTRAP = "BOOTSTRAP"
    PRECHECK = "PRECHECK"
    IFWI = "IFWI"
    BIOS = "BIOS"
    OS = "OS"
    CLEANUP = "CLEANUP"
    DONE = "DONE"