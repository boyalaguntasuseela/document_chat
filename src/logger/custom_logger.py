import os
import logging
from datetime import datetime
import logging
import structlog




class CustomLogger:
    def __init__(self):
        self.log_folder = os.path.join(os.getcwd(), "logs")

        # Create logs directory if it doesn't exist
        os.makedirs(self.log_folder, exist_ok=True)

        # Create log file name
        log_file_name = f"{datetime.now().strftime('%m_%d_%y')}.log"

        # Full log file path
        log_file_path = os.path.join(self.log_folder, log_file_name)

        # Configure logging
        logging.basicConfig(
            filename=log_file_path,
            format="[%(asctime)s] %(levelname)s %(name)s (line: %(lineno)d) - %(message)s",
            level=logging.INFO
        )

        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger
   


def getLogger(self):

    # File handler
    file_handler = logging.FileHandler(self.log_file_path)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(message)s"))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(message)s"))
 # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


#customlogger to structlog implemetation

import structlog


structlog.configure(
    processors=[
        structlog.processors.TimeStamper(
            fmt="iso",
            utc=True,
            key="timestamp"
        ),

        structlog.processors.add_log_level,

        structlog.processors.EventRenamer(
            to="event"
        ),

        structlog.processors.JSONRenderer()
    ],

    logger_factory=structlog.stdlib.LoggerFactory(),

    cache_logger_on_first_use=True
)






if __name__ == "__main__":

    logger_obj = CustomLogger()

    logger = logger = logger_obj.get_logger()

    logger.info("I am calling from CustomLogger")




