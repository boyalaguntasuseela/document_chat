import os
import logging
from datetime import datetime
class CustomLogger():
    def __init__(self):
        self.Log_Folder = os.path.join(os.getcwd(),"logs")
        os.makedirs(self.Log_Folder, exist_ok=True)
        Log_File_Name = f"{datetime.now().strftime("%m_%d_%y")}.log"
        self.log_file_path = os.path.join(self.Log_Folder,Log_File_Name)
        logging.basicConfig(
            filename= self.log_file_path,
            format = "[%(asctime)s] %(levelname)s %(name)s (line: %(lineno)d)- %(message)s",
            level = logging.INFO
        )

    def getLogger(self):
        File_handler = logging.FileHandler(self.log_file_path)
        File_handler.setLevel(logging.INFO)
        File_handler.setFormatter(logging.Formatter ("%(message)s")
        )

        #for console

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter (logging.Formatter ("%(message)s"))

        logging.basicConfig (
            level = logging.INFO,
            format = "[%(asctime)s ] %(levelname)s %(name)s (line: %(lineno)d) - %(message)s",
            handlers=[File_handler,console_handler])
        
        
        return_logger = logging.getLogger(__name__)

        return return_logger
if __name__ == "__main__":
    loggerobj = CustomLogger()

    logger = loggerobj.getLogger()

    logger.info("I am calling from Customlogger")



