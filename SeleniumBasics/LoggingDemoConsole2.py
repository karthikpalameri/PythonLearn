import logging


class LoggingDemoConsole():

    def testLog(self):

        # create logger
        logger = logging.getLogger("mylogger_name")
        logger.setLevel(logging.DEBUG)

        # create console handler and set the level to debug
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        # create fomatter
        formatter = logging.Formatter('%(asctime)s- %(name)s- %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to console handler
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

        logger.debug("my debugging message")
        logger.info("my info message")
        logger.warning("my warning message")
        logger.error("my error")


if __name__ == '__main__':
    LoggingDemoConsole().testLog()