import logging
from sys import stdout

from pydantic_settings import BaseSettings as _BaseSettings


class Settings(_BaseSettings, case_sensitive=True):
    TG_BOT_TOKEN: str


def configure_logging():
    # Configure logging
    logging.getLogger('apscheduler').setLevel(logging.WARNING)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('telegram').setLevel(logging.WARNING)
    logging.getLogger('asyncio').setLevel(logging.WARNING)
    logging.getLogger('httpcore').setLevel(logging.WARNING)

    logger = logging.getLogger()

    try:
        logger.removeHandler(logger.handlers[0])
    except IndexError:
        pass

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(filename)s | Line: %(lineno)d | %(name)s | %(message)s')

    stdout_handler = logging.StreamHandler(stdout)
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('logs.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
