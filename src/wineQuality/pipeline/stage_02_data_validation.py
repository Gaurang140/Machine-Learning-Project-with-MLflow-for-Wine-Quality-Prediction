from wineQuality.config.configuration import ConfigManager
from wineQuality.components.data_validation import DataValidation 
from wineQuality import logger


STAGE_NAME = "Data_Validation"

class DataValidationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config= data_validation_config)
        data_validation.initiate_validation()


if __name__ == '__main__':

    try :
        logger.info(f">>>>>>>> Starting Stage {STAGE_NAME}<<<<<<<< ")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>> completed Stage {STAGE_NAME} <<<<<<<< \n\nx======================x")
        

    except  Exception as e:
        raise e 