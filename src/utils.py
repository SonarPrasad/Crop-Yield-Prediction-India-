import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging

def read_csv_data():
    logging.info("Reading CSV database started")

    try:
        df = pd.read_csv("data\crop_production.csv")
        df.head()
        logging.info("Read Succesfully")

        return df

    except Exception as e:
        raise CustomException(e, sys)