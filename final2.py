import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="AI Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# loading the saved models
diabetes_model = pickle.load(open('/Volumes/APPLE SD/Mini Project/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Volumes/APPLE SD/Mini Project/heart_disease_model.sav', 'rb'))

# Custom CSS for consistent styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .css-1aumxhk {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .st-bw {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .css-1v3fvcr {
        padding: 1rem;
    }
    .css-1q8dd3e {
        border-radius: 8px;
        border: 1px solid #e1e4e8;
    }
    .info-box {
        background-color: #e7f5fe;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 0 8px 8px 0;
    }
    .success-box {
        background-color: #e8f5e9;
        border-left: 4px solid #4CAF50;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
    }
    .warning-box {
        background-color: #fff8e1;
        border-left: 4px solid #FFC107;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
    }
    .danger-box {
        background-color: #ffebee;
        border-left: 4px solid #f44336;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('AI Disease Prediction System',
                         ['AI Diabetes Prediction',
                          'AI Heart Disease Prediction'],
                         menu_icon='hospital-fill',
                         icons=['activity', 'heart'],
                         default_index=0,
                         styles={
                             "container": {"padding": "5px"},
                             "icon": {"color": "#4CAF50", "font-size": "18px"}, 
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
                             "nav-link-selected": {"background-color": "#4CAF50"},
                         })

# AI Diabetes Prediction Page
if selected == 'AI Diabetes Prediction':
    st.title('AI Diabetes Prediction')
    
    # Information box
    with st.expander("ℹ️ About Diabetes Prediction", expanded=True):
        st.write("""
        Our AI model predicts diabetes risk based on health parameters. 
        For accurate results, please provide your most recent health metrics.
        """)
    
    # Input columns with placeholders and ranges
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (0–17)', placeholder="e.g. 2")
        SkinThickness = st.text_input('Skin Thickness (10–50 mm)', placeholder="e.g. 23")
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function (0.1–2.5)', placeholder="e.g. 0.47")

    with col2:
        Glucose = st.text_input('Glucose Level (70–150 mg/dL)', placeholder="e.g. 110")
        Insulin = st.text_input('Insulin Level (15–276 μU/mL)', placeholder="e.g. 80")
        Age = st.text_input('Age (21–81 years)', placeholder="e.g. 33")

    with col3:
        BloodPressure = st.text_input('Blood Pressure (60–90 mmHg)', placeholder="e.g. 72")
        BMI = st.text_input('BMI (18.5–40 kg/m²)', placeholder="e.g. 31.6")

    # Prediction code
    if st.button('Get AI Diabetes Prediction', type="primary", key="diabetes_button"):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                        float(SkinThickness), float(Insulin), float(BMI),
                        float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                st.markdown('<div class="danger-box"><h4>⚠️ AI Prediction: High Risk of Diabetes</h4><p>Our AI model indicates a likelihood of diabetes. Please consult with a healthcare provider for comprehensive testing and advice.</p></div>', unsafe_allow_html=True)
                st.markdown("""
                **Next Steps:**
                - Schedule an appointment with your doctor
                - Monitor your blood sugar regularly
                - Consider dietary changes and increased physical activity
                """)
            else:
                st.markdown('<div class="success-box"><h4>✅ AI Prediction: Low Risk of Diabetes</h4><p>Our AI model does not detect signs of diabetes. Maintain healthy habits for prevention.</p></div>', unsafe_allow_html=True)
                st.markdown("""
                **Prevention Tips:**
                - Maintain balanced diet with limited sugars
                - Exercise regularly (150 mins/week)
                - Get annual checkups if over 40
                """)
                
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Additional information
    st.markdown("---")
    st.subheader("Understanding Diabetes Risk Factors")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        **Major Risk Factors:**
        - Family history of diabetes
        - Overweight (BMI > 25)
        - Physical inactivity
        - High blood pressure
        """)
    with col2:
        st.write("""
        **Early Warning Signs:**
        - Frequent urination
        - Increased thirst
        - Fatigue
        - Blurred vision
        """)
    
    st.caption("""
    *Note: This AI prediction tool is not a substitute for professional medical diagnosis. 
    Always consult with a qualified healthcare provider for personal health advice.*
    """)

# AI Heart Disease Prediction Page
if selected == 'AI Heart Disease Prediction':
    st.title('AI Heart Disease Prediction')
    
    # Information box
    with st.expander("ℹ️ About Heart Disease Prediction", expanded=True):
        st.write("""
        Our advanced AI analyzes multiple cardiac risk factors to predict heart disease probability. 
        Enter your most recent cardiac metrics for accurate assessment.
        """)
    
    # Input columns with placeholders and ranges
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age (29–77 years)', placeholder="e.g. 45")
        trestbps = st.text_input('Resting BP (94–200 mmHg)', placeholder="e.g. 120")
        restecg = st.text_input('Resting ECG (0-2)', placeholder="0=normal, 1=abnormality, 2=hypertrophy")
        oldpeak = st.text_input('ST Depression (0-6.2)', placeholder="e.g. 1.2")

    with col2:
        sex = st.text_input('Sex (0=Female, 1=Male)', placeholder="0 or 1")
        chol = st.text_input('Cholesterol (126-564 mg/dL)', placeholder="e.g. 240")
        thalach = st.text_input('Max Heart Rate (71-202 bpm)', placeholder="e.g. 150")
        slope = st.text_input('ST Slope (0-2)', placeholder="0=up, 1=flat, 2=down")

    with col3:
        cp = st.text_input('Chest Pain Type (0-3)', placeholder="0=typical, 1=atypical, 2=non-anginal, 3=asymptomatic")
        fbs = st.text_input('Fasting BS >120 (0=No, 1=Yes)', placeholder="0 or 1")
        exang = st.text_input('Exercise Angina (0=No, 1=Yes)', placeholder="0 or 1")
        ca = st.text_input('Major Vessels (0-3)', placeholder="0-3 vessels")

    thal = st.text_input('Thalassemia (0-3)', placeholder="0=normal, 1=fixed, 2=reversible, 3=other")

    # Prediction code
    if st.button('Get AI Heart Disease Prediction', type="primary", key="heart_button"):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), 
                         float(chol), float(fbs), float(restecg), float(thalach),
                         float(exang), float(oldpeak), float(slope), float(ca), 
                         float(thal)]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.markdown('<div class="danger-box"><h4>⚠️ AI Prediction: Heart Disease Risk Detected</h4><p>Our AI model indicates potential heart disease. Please consult a cardiologist for comprehensive evaluation.</p></div>', unsafe_allow_html=True)
                st.markdown("""
                **Recommended Actions:**
                - Schedule cardiac consultation
                - Monitor blood pressure regularly
                - Consider stress ECG and lipid profile
                - Adopt heart-healthy lifestyle
                """)
            else:
                st.markdown('<div class="success-box"><h4>✅ AI Prediction: Low Heart Disease Risk</h4><p>Our AI model shows no current signs of heart disease. Maintain cardiovascular health through preventive measures.</p></div>', unsafe_allow_html=True)
                st.markdown("""
                **Heart Health Tips:**
                - Regular aerobic exercise
                - Mediterranean-style diet
                - Annual cardiac checkups after 40
                - Stress management techniques
                """)
                
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Additional information
    st.markdown("---")
    st.subheader("Cardiac Health Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        **Key Risk Factors:**
        - High blood pressure
        - Elevated cholesterol
        - Smoking history
        - Diabetes
        - Family history
        """)
    with col2:
        st.write("""
        **Warning Signs:**
        - Chest discomfort
        - Shortness of breath
        - Palpitations
        - Unexplained fatigue
        """)
    
    st.caption("""
    *Disclaimer: AI predictions are probabilistic and should complement, not replace, 
    professional medical evaluation. Individual results may vary based on factors not 
    captured in this model.*
    """)