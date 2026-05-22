from src.logger.custom_logger import CustomLogger
import logging


loggerobj = CustomLogger()
logger = loggerobj.getLogger(__file__)


def add (a,b):
    logger.info("started add method")
    sum  = a+b
    logger.info("ended add methos")
    return sum

if __name__=="__main__":
    add(2,3)

