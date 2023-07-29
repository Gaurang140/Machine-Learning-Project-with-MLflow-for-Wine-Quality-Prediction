import os 
from pathlib import Path
from  wineQuality import logger
from wineQuality.utils.common import get_size,get_data_from_mongodb
from wineQuality.entity.config_entity import DataIngestionConfig
import pandas as pd





class DataIngestion:
    def __init__(self , config : DataIngestionConfig):
        self.config = config 

    def download_file_from_mongodb(self) :
        if not os.path.exists(self.config.local_csv_file_path)  :

            data = get_data_from_mongodb()
            data.to_csv(self.config.local_csv_file_path , index=False)
            
            logger.info(f"data has been downloaded from MongoDB {len(data)}")
        else:  
            logger.info(f"File already exists of size {get_size(Path(self.config.local_csv_file_path))}")
            
            


