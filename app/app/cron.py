import logging

logger = logging.getLogger(__name__)


def print_hello():
    print("HELLO")
    logger.info("Cron Job was called")
