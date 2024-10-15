import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Health Assistant", layout="wide")


working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/models/parkinsons_model.sav', 'rb'))


with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )


def custom_css():
    st.markdown("""
        <style>
            .stButton>button {
                background-color: #4CAF50; /* Green */
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            .stButton>button:hover {
                background-color: #45a049;
            }
            .result {
                font-size: 20px;
                font-weight: bold;
            }
            .success {
                color: #4CAF50;
            }
            .error {
                color: #FF0000;
            }
        </style>
    """, unsafe_allow_html=True)


custom_css()


def display_disease_prediction(disease_type):
    if disease_type == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')
        inputs = [
            st.text_input('Number of Pregnancies'),
            st.text_input('Glucose Level'),
            st.text_input('Blood Pressure value'),
            st.text_input('Skin Thickness value'),
            st.text_input('Insulin Level'),
            st.text_input('BMI value'),
            st.text_input('Diabetes Pedigree Function value'),
            st.text_input('Age of the Person')
        ]
        if st.button('Diabetes Test Result'):
            with st.spinner('Predicting...'):
                user_input = [float(x) for x in inputs]
                prediction = diabetes_model.predict([user_input])
                st.success('The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic', icon="✅")

    elif disease_type == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction using ML')
        inputs = [
            st.text_input('Age'),
            st.text_input('Sex'),
            st.text_input('Chest Pain types'),
            st.text_input('Resting Blood Pressure'),
            st.text_input('Serum Cholestoral in mg/dl'),
            st.text_input('Fasting Blood Sugar > 120 mg/dl'),
            st.text_input('Resting Electrocardiographic results'),
            st.text_input('Maximum Heart Rate achieved'),
            st.text_input('Exercise Induced Angina'),
            st.text_input('ST depression induced by exercise'),
            st.text_input('Slope of the peak exercise ST segment'),
            st.text_input('Major vessels colored by flourosopy'),
            st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
        ]
        if st.button('Heart Disease Test Result'):
            with st.spinner('Predicting...'):
                user_input = [float(x) for x in inputs]
                prediction = heart_disease_model.predict([user_input])
                st.success('The person is having heart disease' if prediction[0] == 1 else 'The person does not have any heart disease', icon="✅")

    elif disease_type == "Parkinson's Prediction":
        st.title("Parkinson's Disease Prediction using ML")
        inputs = [
            st.text_input('MDVP:Fo(Hz)'),
            st.text_input('MDVP:Fhi(Hz)'),
            st.text_input('MDVP:Flo(Hz)'),
            st.text_input('MDVP:Jitter(%)'),
            st.text_input('MDVP:Jitter(Abs)'),
            st.text_input('MDVP:RAP'),
            st.text_input('MDVP:PPQ'),
            st.text_input('Jitter:DDP'),
            st.text_input('MDVP:Shimmer'),
            st.text_input('MDVP:Shimmer(dB)'),
            st.text_input('Shimmer:APQ3'),
            st.text_input('Shimmer:APQ5'),
            st.text_input('MDVP:APQ'),
            st.text_input('Shimmer:DDA'),
            st.text_input('NHR'),
            st.text_input('HNR'),
            st.text_input('RPDE'),
            st.text_input('DFA'),
            st.text_input('spread1'),
            st.text_input('spread2'),
            st.text_input('D2'),
            st.text_input('PPE')
        ]
        if st.button("Parkinson's Test Result"):
            with st.spinner('Predicting...'):
                user_input = [float(x) for x in inputs]
                prediction = parkinsons_model.predict([user_input])
                st.success("The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease", icon="✅")


display_disease_prediction(selected)
