import logging
import colorlog

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
