from wineQuality import logger 
from wineQuality.pipeline.stage_01_data_ingestion   import DataIngestionPipeline



Stage_name = 'stage_01_data_ingestion'

try:
    logger.info(f">>>>>>>> Starting Stage {Stage_name}<<<<<<<< ")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>> completed Stage {Stage_name} <<<<<<<< \n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise (e)
