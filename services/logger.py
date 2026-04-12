import logging

class Logger:

    def __init__(self):
        logging.basicConfig(
            filename="autoflow.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def info(self, msg):
        logging.info(msg)
        print(msg)

    def error(self, msg):
        logging.error(msg)
        print(msg)