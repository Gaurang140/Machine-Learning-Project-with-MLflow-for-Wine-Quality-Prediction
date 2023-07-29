import os 
import sys
import logging 

logging_string = "[%(asctime)s : %(levelname)s:%(message)s]"

log_dir = "logs"
log_file_path = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir , exist_ok=True)



logging.basicConfig(
    level=logging.INFO,
    format=logging_string,

    handlers = [
        logging.FileHandler(log_file_path) ,  
        logging.StreamHandler(log_file_path)
        ]
)


logger = logging.getLogger("wineQualityLogger")