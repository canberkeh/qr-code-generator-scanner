import logging
import logging.handlers

LOG_FILE = 'logs'
LEVEL = 'DEBUG'
MAX_BYTES = 50*1024
MAX_BACKUP_COUNT = 3


def logger(name=None):

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
    
    handler = logging.handlers.RotatingFileHandler (
        filename=LOG_FILE,
        mode = 'a',
        maxBytes=MAX_BYTES,
        backupCount=MAX_BACKUP_COUNT
    )

    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(LEVEL)
    logger.addHandler(handler)
    
    return logger