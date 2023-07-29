import os 
from pathlib import Path
from  wineQuality import logger
from wineQuality.entity.config_entity import DataValidationConfig
import pandas as pd








class DataValidation:

    def __init__(self,data_validation_config : DataValidationConfig) :
        self.config = data_validation_config

    def initiate_validation(self) :

        try: 
            validation_status = None

            data = pd.read_csv(self.config.data_dir)
            all_columns = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col  not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE_PATH , "w") as f:
                        f.write(f"validation status {validation_status}")

                else :
                    validation_status = True 
                    with open(self.config.STATUS_FILE_PATH , "w") as f:
                        f.write(f"validation status {validation_status}")
            return validation_status

        except Exception as e :
            raise e
