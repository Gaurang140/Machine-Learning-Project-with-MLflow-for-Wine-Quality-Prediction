from wineQuality.config.configuration import ConfigManager
from wineQuality.components.data_ingestion import DataIngestion
from wineQuality import logger




Stage_name = "Data_Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file_from_mongodb()


if __name__ == '__main__':

    try:
        logger.info(f">>>>>>>> Starting Stage {Stage_name}<<<<<<<< ")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>> completed Stage {Stage_name} <<<<<<<< \n\nx======================x")
    except Exception as e:
        logger.exception(e)
        raise (e)
