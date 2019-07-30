import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p®')

logging.debug("my debugging message")
logging.info("my info message")
logging.warning("my warning message")
logging.error("my error")
