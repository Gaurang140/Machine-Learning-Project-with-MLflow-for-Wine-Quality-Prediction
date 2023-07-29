from wineQuality import logger 
from wineQuality.pipeline.stage_03_data_transformation import DataTransformationPipeline



Stage_name = 'Data_transformation'

try:
    logger.info(f">>>>>>>> Starting Stage {Stage_name}<<<<<<<< ")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>> completed Stage {Stage_name} <<<<<<<< \n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise (e)
