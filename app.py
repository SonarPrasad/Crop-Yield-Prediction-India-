from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("Execution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e, sys)