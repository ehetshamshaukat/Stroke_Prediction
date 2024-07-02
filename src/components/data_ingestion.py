import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_dataset_path=os.path.join("artifacts/train_test_dataset","train_dataset.csv")
    test_dataset_path=os.path.join("artifacts/train_test_dataset","test_dataset.csv")


class DataIngestion:
    def __init__(self):
        self.dataset_path=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv("dataset/stroke-data.csv")
            train_dataset_path,test_dataset_path=train_test_split(df,test_size=0.2)
            os.makedirs(os.path.dirname(self.dataset_path.train_dataset_path),exist_ok=True)
            train_dataset_path.to_csv(self.dataset_path.train_dataset_path,index=False,header=True)
            test_dataset_path.to_csv(self.dataset_path.test_dataset_path,index=False,header=True)
            return self.dataset_path.train_dataset_path,self.dataset_path.test_dataset_path
        except Exception as e:
            raise e