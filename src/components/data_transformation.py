import numpy as np
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import os
import pandas as pd
from dataclasses import dataclass
from src.utils import save_file_as_pickle


@dataclass
class DataTransformationConfig:
    data_transformation_pickle_path = os.path.join("artifacts/pickle", "data_transformation.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def transform(self):
        numerical_columns = ["age", "avg_glucose_level", "bmi"]
        categorical_columns = ["gender", "hypertension", "heart_disease","ever_married", "Residence_type", "work_type" , "smoking_status"]

        numerical_column_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        categorical_column_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ("ordinalencoder",OrdinalEncoder()),
            ('standardscaler', StandardScaler())
        ])
        preprocessing = ColumnTransformer([
            ("numerical_column_pipeline", numerical_column_pipeline, numerical_columns),
            ("categorical_column_pipeline", categorical_column_pipeline, categorical_columns)
        ])
        return preprocessing

    def initiate_data_transformation(self, train_dataset_path, test_dataset_path):
        try:
            train_dataset = pd.read_csv(train_dataset_path)
            test_dataset = pd.read_csv(test_dataset_path)

            data_transform = self.transform()

            column_to_transform = ["hypertension", "heart_disease"]
            for col in column_to_transform:
                train_dataset[col].replace([0, 1], ["no", "yes"], inplace=True)
                test_dataset[col].replace([0, 1], ["no", "yes"], inplace=True)


            train_dataset = train_dataset.drop(train_dataset[train_dataset["gender"]=="other"].index)

            target_column = "stroke"
            column_to_drop = ["id", "stroke"]

            xtrain = train_dataset.drop(columns=column_to_drop, axis=1)
            ytrain = train_dataset[target_column]

            xtest = test_dataset.drop(columns=column_to_drop, axis=1)
            ytest = test_dataset[target_column]

            transformed_xtrain = data_transform.fit_transform(xtrain)
            transformed_xtest = data_transform.transform(xtest)

            transformed_train_datatset = np.c_[transformed_xtrain, np.array(ytrain)]
            transformed_test_dataset = np.c_[transformed_xtest, np.array(ytest)]

            save_file_as_pickle(data_transform, self.data_transformation_config.data_transformation_pickle_path)

            return transformed_train_datatset, transformed_test_dataset


        except Exception as e:
            raise e
