import streamlit as st
from src.pipeline.prediction_pipeline import Features,Prediction


st.header("Stroke Prediction")
gender=st.selectbox("please select gender",["Male","Female"])
age=st.number_input("please enter age",value=0)
hypertension=st.selectbox("please enter if you have hyper tension",["yes","no"])
heart_disease=st.selectbox("please select if you have any heart disease",["yes","no"])
ever_married=st.selectbox("please select if you are married",["Yes","No"])
work_type=st.selectbox("please select your work type",['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
Residence_type=st.selectbox("please select your residence type",['Urban', 'Rural'])
avg_glucose_level=st.number_input("please enter your glucose level",value=0)
bmi=st.number_input("please enter bmi",value=0)
smoking_status=st.selectbox("please enter your smoking status",['formerly smoked', 'never smoked', 'smokes', 'Unknown'])


ok = st.button("Predict")


if ok:

    feature=Features(gender,age,hypertension,heart_disease,ever_married,work_type,
         Residence_type,avg_glucose_level,bmi,smoking_status)

    feature_to_df=feature.to_dataframe()

    pred=Prediction()
    result=pred.initiate_prediction(feature_to_df)
    if result == 0:
        st.write("Congrat! Stroke not detected")
    else:
        st.write("Sorry, Stroke detected")
