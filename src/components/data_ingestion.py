from src.logger import logging
from src.exception import CustomException

import os
import sys
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","data.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion component")
        # Data read

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()