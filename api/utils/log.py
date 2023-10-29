import sys
import logging
from logging.handlers import RotatingFileHandler

log = logging.getLogger("pseudo_town")
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(asctime)s][%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler = RotatingFileHandler("info.log", backupCount=5, maxBytes=10)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.addHandler(stream_handler)


if __name__ == "__main__":
    log.info("Test")
