import sys
import traceback
from typing import Optional
from src.logger.custom_logger import CustomLogger

loggerobj = CustomLogger()
logger = loggerobj.get_logger(__file__)

class cCustomException(Exception):

    def __init__(
    self,
    error_message,
    error_detail: Optional[object] = None
):
        normal_message = str(error_message)
        exc_type = exc_value=exc_tb=None

    if error_detail is None:
        exc_type,exc_value,exc_tb = sys.exc_info()

    else:
        if hasattr(error_detail, "exc_info"):
            exc_type, exc_value,exc_tb=error_detail.exc_info()
        elif isinstance(error_detail, BaseException)