import logging


logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

logging.debug("my debugging message")
logging.info("my info message")
logging.warning("my warning message")