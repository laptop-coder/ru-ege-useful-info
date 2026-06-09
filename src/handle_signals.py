import signal

from config import logger

from publish_post import publish_post


def receive_signal(signal_number, frame):
    match signal_number:
        case signal.SIGUSR1:
            logger.info("Received signal SIGUSR1")
            publish_post()
