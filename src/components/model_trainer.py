import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
import os
import sys
from dataclasses import dataclass
from pathlib import Path

@dataclass 
class ModelTrainerConfig:
    pass

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_training(self,train_array,test_array):
        try:
            pass

        except:
            pass
