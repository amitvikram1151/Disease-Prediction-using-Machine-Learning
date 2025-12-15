import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant")


# loading the saved models
diabetes_model = pickle.load(open('/Volumes/APPLE SD/Mini Project/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Volumes/APPLE SD/Mini project/heart_disease_model.sav', 'rb'))  # Added this line


# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using AI')

    # Input columns
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (0–17)', placeholder="e.g. 2")
    with col2:
        Glucose = st.text_input('Glucose Level (70–150)', placeholder="e.g. 110")
    with col3:
        BloodPressure = st.text_input('Blood Pressure (60–90)', placeholder="e.g. 72")
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness (10–50)', placeholder="e.g. 23")
    with col2:
        Insulin = st.text_input('Insulin Level (15–276)', placeholder="e.g. 80")
    with col3:
        BMI = st.text_input('BMI (18.5–40)', placeholder="e.g. 31.6")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function (0.1–2.5)', placeholder="e.g. 0.47")
    with col2:
        Age = st.text_input('Age (21–81)', placeholder="e.g. 33")

    # Prediction code
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = '❌The person is diabetic'
            else:
                diab_diagnosis = '✅  The person is not diabetic'
        except:
            diab_diagnosis = 'Please enter valid numeric values in all fields.'

    st.success(diab_diagnosis)
    
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title with icon
    st.title('Heart Disease Prediction using AI')
    
    # Input columns with placeholders and ranges based on your dataset
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age (29–77 years)', placeholder="e.g. 45")
        trestbps = st.text_input('Resting Blood Pressure (94–200 mmHg)', placeholder="e.g. 120")
        restecg = st.text_input('Resting ECG (0-2)', placeholder="0 = normal, 1 = ST-T abnormality, 2 = hypertrophy")
        oldpeak = st.text_input('ST Depression (0-6.2)', placeholder="e.g. 1.2")

    with col2:
        sex = st.text_input('Sex (0 = female, 1 = male)', placeholder="0 or 1")
        chol = st.text_input('Serum Cholesterol (126-564 mg/dl)', placeholder="e.g. 240")
        thalach = st.text_input('Max Heart Rate (71-202 bpm)', placeholder="e.g. 150")
        slope = st.text_input('Slope of ST Segment (0-2)', placeholder="0 = up, 1 = flat, 2 = down")

    with col3:
        cp = st.text_input('Chest Pain Type (0-3)', placeholder="0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic")
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (0 = no, 1 = yes)', placeholder="0 or 1")
        exang = st.text_input('Exercise Induced Angina (0 = no, 1 = yes)', placeholder="0 or 1")
        ca = st.text_input('Major Vessels (0-3)', placeholder="0-3 vessels colored by fluoroscopy")

    thal = st.text_input('Thalassemia (0-3)', placeholder="0 = normal, 1 = fixed defect, 2 = reversible defect, 3 = other")

    # Prediction code
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result', type="primary", key="heart_button"):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), 
                         float(chol), float(fbs), float(restecg), float(thalach),
                         float(exang), float(oldpeak), float(slope), float(ca), 
                         float(thal)]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = '❌The person is likely to have heart disease'
            else:
                heart_diagnosis = '✅ The person does not show signs of heart disease'
        except:
            heart_diagnosis = 'Please enter valid numeric values in all fields.'
            
    st.success(heart_diagnosis)