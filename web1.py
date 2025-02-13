import os
import pickle  # pre-trained model loading
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide', page_icon="🩺")

# Load models
diabetes_model = pickle.load(open(r"C:\Users\siddu\Downloads\diabetes_model.sav", "rb"))
heart_model = pickle.load(open(r"C:\Users\siddu\Downloads\heart_model.sav", "rb"))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks',
                           ['Diabetes Prediction', 'Heart Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)

# Diabetes Prediction Section
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
