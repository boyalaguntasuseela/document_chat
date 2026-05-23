import structlog
from src. exception.custom_exception import CustomException
from src.logger.custom_logger import CustomLogger
import logging
import os
from path lib import path


logger_obj = CustomLogger()
logger = logger_obj.get_logger(__file__)


def add (a,b): 
    logger.info("started add method")
    sum  = a+b
    logger.info("ended add method")
    return sum

if __name__=="__main__":

    try:
        add(2,3)
    

def get_logger(self, name = __file__):

    logger_name = os.path.basename(self)

    return structlog.get_logger()


