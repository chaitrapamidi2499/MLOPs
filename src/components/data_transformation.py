import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from pathlib import Path

from dataclasses import dataclass
import os
import sys

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            pass
        except:
            pass

    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head(2).to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head(2).to_string()}')

            logging.info("Obtaining Preprocessor Object")

            preprocessing_obj = self.get_data_transformation()

        except:
            pass

