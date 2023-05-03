import logging

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomLogger:
    def __init__(self):
        # USAGE
        # self.logger.debug('debug message')
        # self.logger.info('info message')
        # self.logger.warning('warn message')
        # self.logger.error('error message')
        # self.logger.critical('critical message')

        self.logger = logging.getLogger("Upwork bot")
        self.logger.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler("error_upwork.log")
        fileHandler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)

        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.DEBUG)
        c_handler.setFormatter(CustomFormatter())
        self.logger.addHandler(c_handler)
    
    def info(self, msg):
        """Log info"""
        self.logger.info(msg)

    def debug(self, msg):
        "Only logs if the static variable {DEBUG} is set to True."
        self.logger.debug(msg)
    def warning(self, msg):
        "Only logs if the static variable {DEBUG} is set to True."
        self.logger.warning(msg)
    def critical(self, msg):
        "Only logs if the static variable {critical} is set to True."
        self.logger.critical(msg)
    def error(self, msg):
        "Only logs if the static variable {error} is set to True."
        self.logger.error(msg)

logger = CustomLogger()