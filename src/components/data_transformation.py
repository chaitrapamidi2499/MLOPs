import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from pathlib import Path

#from dataclasses import dataclass
import os
import sys

#@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_obj(self):
        pass

    def initialize_data_transformation(self,train_path,test_path):
        pass
