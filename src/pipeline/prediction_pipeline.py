from src.utils import load_pickle_file
import os
import pandas as pd


class Prediction:
    def __init__(self):
        pass

    def initiate_prediction(self, feature):
        try:
            preprocessing_path = os.path.join("artifacts/pickle", "data_transformation.pkl")
            model_path = os.path.join("artifacts/pickle", "model.pkl")

            preprocessing = load_pickle_file(preprocessing_path)
            model = load_pickle_file(model_path)

            processed_data = preprocessing.transform(feature)
            output = model.predict(processed_data)
            print(output)
            return output
        except Exception as e:
            raise e


class Features:
    def __init__(self, gender, age, hypertension, heart_disease, ever_married, work_type,
                 Residence_type, avg_glucose_level, bmi, smoking_status):
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.ever_married = ever_married
        self.work_type = work_type
        self.Residence_type = Residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status

    def to_dataframe(self):
        try:

            feature = {
                'gender': [self.gender],
                'age': [self.age],
                'hypertension': [self.hypertension],
                'heart_disease': [self.heart_disease],
                'ever_married': [self.ever_married],
                'work_type': [self.work_type],
                'Residence_type': [self.Residence_type],
                'avg_glucose_level': [self.avg_glucose_level],
                'bmi': [self.bmi],
                'smoking_status': [self.smoking_status]

            }

            feature_as_dataframe = pd.DataFrame(feature)
            print(feature_as_dataframe)
            return feature_as_dataframe
        except Exception as e:
            raise e
