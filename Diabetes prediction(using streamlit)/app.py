import streamlit as st
import pickle
import sklearn
from streamlit_option_menu import option_menu
# model = pickle.load(open('model.pkl','rb'))

Diabetes_pred = pickle.load(open('C:/Users/india/OneDrive/Documents/SRAJAN/ML projects/Diabetes prediction/diabetes_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Diabtetes Prediction Using Machine Learning Algorithms',['Diabetes Prediction'],icons = ['activity'])
st.title("Diabetes Prediction")
Pregnancies = st.text_input("Number of Pregnancies")
Gulucose = st.text_input("Gulucose Level")
BloodPressure = st.text_input("BloodPressure")
SkinThickness = st.text_input("SkinThickness")
Insulin = st.text_input("Insulin")
BMI = st.text_input("BMI")
DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
Age = st.text_input("Age")


diab_diagnosis = ''
if st.button('Submit'):
     diab_pred = Diabetes_pred.predict([[Pregnancies, Gulucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
     if (diab_pred[0]==1):
         diab_diagnosis = 'The Person is Diabetic'
     else:
         diab_diagnosis = 'The Person is not Diabetic'
st.success(diab_diagnosis)         
              