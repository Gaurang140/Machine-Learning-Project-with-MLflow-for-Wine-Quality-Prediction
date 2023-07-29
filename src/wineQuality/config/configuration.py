from wineQuality.constants import *
from wineQuality.utils.common import read_yaml , get_data_from_mongodb ,create_directories
from wineQuality.entity.config_entity import DataIngestionConfig

class ConfigManager:
    def __init__(
        self , 
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH,
        schema_file_path = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)


        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(

            root_dir = config.root_dir,
            local_csv_file_path = config.local_csv_file_path
        )

        return data_ingestion_config
