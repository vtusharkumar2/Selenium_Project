import logging

import logging

def setup_logger():
    logging.basicConfig(
        filename="logfile.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()


def set_log():
    logger=logging.getLogger("sutomation_log")
    file_handler=logging.FileHandler("test_log.log")
    formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    logger.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


