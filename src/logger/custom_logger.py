import os
import logging
from datetime import datetime
class CustomLogger():
    def __init__(self):
        self.Log_Folder = os.path.join(os.getcwd(),"logs")
        os.makedirs(self.LOG_Folder)
        Log_File_Name = f"{datetime.now().strftime("%m_%d_%y")}.log"
        Log_file_Path = os.path.join(Log_Folder,Log_File_Name)
        logging.basicConfig(
            filename= Log_file_Path,
            format = "[%(asctime)s] %(levelname)s %(name)s (line: %(lineno)d)- %(message)s",
            level = logging.INFO
        )

    def getLogger(self):
        File_handler = logging.Filehandler(self.Log_file_Path)
        File_handler.setlevel(logging.INFO)
        File_handler.setFormatter(logging.Formatter "%(message)s")

        #for console

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter (logging.Formatter "%(message)s")

        logging.basicConfig (
            Level = logging.INFO
            format = "%(message)s,"
            handlers=[File_handler,console_handler]
        
        return_logger = logging.getlogger(__name__))

if __name__ == "__main__":
    logger_obj = CustomLogger (
        logger_obj.get_logger()
        logger.info("I am calling from Customlogger")
    )




