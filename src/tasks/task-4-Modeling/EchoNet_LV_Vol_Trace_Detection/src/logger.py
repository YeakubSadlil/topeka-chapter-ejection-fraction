import logging

def get_logger():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger
