import logging
import json
from datetime import datetime as dt


class Jsonificator(logging.Formatter):

    def format(self, record):
        time = f"{dt.now():%Y-%m-%d %H:%M:%S}"

        response = {
            'time': time,
            'level': record.levelname,
            'message': record.getMessage()
        }

        if record.exc_info:
            response["exception"] = self.formatException(record.exc_info)

        return json.dumps(response)
    

def my_logger(mode = "INFO") -> logging.Logger:
    logger = logging.getLogger()

    if hasattr(logging, mode):
        logger.setLevel(getattr(logging, mode))
    else:
        logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("whataspp/bot.log", mode="a")
    file_handler.setFormatter(Jsonificator())

    logger.addHandler(file_handler)
    
    return logger