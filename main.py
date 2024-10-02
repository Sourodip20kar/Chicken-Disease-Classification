""" from package.subpackage import module """
""" or """
""" 
from .module import something
from ..subpackage import something 
"""

""" from src.cnnClassifier import logger

logger.info("this is a custom log message") """

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n==========x")
except Exception as e:
        logger.exception(e)
        raise e