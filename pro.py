import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="AI Health Assistant Pro",
    layout="wide",
    page_icon="⚕️",
    initial_sidebar_state="expanded"
)

# loading the saved models
diabetes_model = pickle.load(open('/Volumes/APPLE SD/Mini Project/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Volumes/APPLE SD/Mini Project/heart_disease_model.sav', 'rb'))
# Custom CSS for professional styling
st.markdown("""
    <style>
    :root {
        --primary: #4CAF50;
        --secondary: #2196F3;
        --danger: #f44336;
        --warning: #FFC107;
        --success: #4CAF50;
        --dark-bg: #1a2634;
        --darker-bg: #0d1520;
        --sidebar-text: #ffffff;
        --sidebar-secondary: #B0BEC5;
        --light: #f8f9fa;
    }
    
    /* Main content styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
    }
    
    /* Dark mode compatibility */
    @media (prefers-color-scheme: dark) {
        .main {
            background: #0E1117;
        }
        .card, .result-card {
            background-color: #1e293b;
            color: white;
            border: 1px solid #2a3a4d;
        }
        .stTextInput>div>div>input {
            background-color: #1e293b;
            color: white;
            border-color: #2a3a4d;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: white;
        }
    }
    
    /* Sidebar styling - forced dark mode */
    [data-testid="stSidebar"] {
        background: linear-gradient(195deg, var(--dark-bg) 0%, var(--darker-bg) 100%) !important;
    }
    
    /* Sidebar text elements */
    [data-testid="stSidebar"] * {
        color: var(--sidebar-text) !important;
    }
    
    /* Sidebar input fields */
    [data-testid="stSidebar"] .stTextInput>div>div>input,
    [data-testid="stSidebar"] .stNumberInput>div>div>input {
        background-color: #2a3a4d !important;
        color: white !important;
        border-radius: 8px !important;
        border: 1px solid #3e4d63 !important;
        padding: 10px 15px !important;
    }
    
    /* Sidebar selection boxes */
    [data-testid="stSidebar"] div[role="radiogroup"] {
        background-color: #2a3a4d !important;
        border-radius: 10px !important;
        padding: 8px !important;
    }
    
    /* Selected item in sidebar */
    [data-testid="stSidebar"] .st-eb {
        border-radius: 8px !important;
        background-color: rgba(76, 175, 80, 0.2) !important;
    }
    
    /* Rest of your existing styles... */
    .st-bw {
        background-color: white;
    }
    
    .stButton>button {
        background: linear-gradient(to right, var(--primary), #2E7D32);
        color: white;
        border-radius: 8px;
        padding: 12px 28px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        background: linear-gradient(to right, #43A047, #1B5E20);
    }
    
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px 15px;
        border: 1px solid #e0e0e0;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 2px rgba(76,175,80,0.2);
    }
    
    .stExpander {
        border-radius: 10px;
        border: 1px solid rgba(0,0,0,0.1);
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--dark);
    }
    
    .card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    
    .result-card {
        border-left: 5px solid;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    .danger-card {
        border-left-color: var(--danger);
        background: linear-gradient(to right, #ffebee 0%, #ffffff 100%);
    }
    
    .success-card {
        border-left-color: var(--success);
        background: linear-gradient(to right, #e8f5e9 0%, #ffffff 100%);
    }
    
    .info-card {
        border-left-color: var(--secondary);
        background: linear-gradient(to right, #e7f5fe 0%, #ffffff 100%);
    }
    
    .feature-icon {
        font-size: 24px;
        margin-right: 10px;
        color: var(--primary);
    }
    
    .risk-meter {
        height: 10px;
        border-radius: 5px;
        background: linear-gradient(to right, #4CAF50, #FFC107, #f44336);
        margin: 10px 0;
    }
    
    .progress-container {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin: 15px 0;
    }
    
    .progress-bar {
        height: 20px;
        border-radius: 5px;
        background: linear-gradient(to right, #4CAF50, #FFC107, #f44336);
        text-align: center;
        line-height: 20px;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# sidebar for navigation
with st.sidebar:
    st.markdown(f"""
    <h1 style='color: var(--sidebar-text) !important; font-size: 28px; margin-bottom: 20px;'>
    AI Health Assistant Pro
    </h1>
    <div style='color: var(--sidebar-secondary) !important; margin-bottom: 30px;'>
    Advanced Disease Prediction System
    </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        '',
        ['AI Diabetes Prediction', 'AI Heart Disease Prediction'],
        icons=['activity', 'heart-pulse'],
        menu_icon="hospital",
        default_index=0,
        styles={
            "container": {
                "padding": "0", 
                "background-color": "transparent",
            },
            "icon": {
                "color": "var(--sidebar-text)", 
                "font-size": "18px"
            }, 
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px 0",
                "color": "var(--sidebar-text)",
                "border-radius": "8px",
                "padding": "10px 15px",
                "background-color": "transparent"
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, rgba(76,175,80,0.8) 0%, rgba(76,175,80,1) 100%)",
                "color": "var(--sidebar-text)",
                "font-weight": "bold",
                "border": "none"
            },
        }
    )
    
    st.markdown("---")
    st.markdown(f"""
    <div style='color: var(--sidebar-secondary) !important; font-size: 14px; padding: 10px;'>
    <b>Disclaimer:</b> This AI tool provides health risk assessments but is not a substitute for professional medical advice.
    </div>
    """, unsafe_allow_html=True)

def create_risk_meter(percentage):
    color = "#4CAF50"
    if percentage > 70:
        color = "#f44336"
    elif percentage > 30:
        color = "#FFC107"
    
    return f"""
    <div style='margin: 20px 0;'>
        <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
            <span>0%</span>
            <span>Risk: {percentage:.1f}%</span>
            <span>100%</span>
        </div>
        <div class='progress-container'>
            <div class='progress-bar' style='width: {percentage}%; background-color: {color};'>
                {percentage:.1f}%
            </div>
        </div>
        <div style='display: flex; justify-content: space-between; margin-top: 5px;'>
            <span>Low</span>
            <span>Moderate</span>
            <span>High</span>
        </div>
    </div>
    """

# AI Diabetes Prediction Page
if selected == 'AI Diabetes Prediction':
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title('AI Diabetes Prediction')
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3069/3069172.png", width=80)
    
    # Information card
    with st.expander("📊 About Diabetes Prediction", expanded=True):
        st.write("""
        Our advanced AI model evaluates multiple health parameters to assess your diabetes risk. 
        For optimal accuracy, please provide your most recent health metrics.
        """)
        st.markdown("""
        <div class='risk-meter'></div>
        <div style='display: flex; justify-content: space-between; margin-top: 5px;'>
            <span>Low Risk</span>
            <span>Moderate Risk</span>
            <span>High Risk</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Input columns with placeholders and ranges
    st.markdown("### 🩺 Health Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h4>Basic Information</h4>", unsafe_allow_html=True)
        Pregnancies = st.text_input('Number of Pregnancies (0–17)', placeholder="e.g. 2", key="preg")
        Age = st.text_input('Age (21–81 years)', placeholder="e.g. 33", key="age")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h4>Blood Metrics</h4>", unsafe_allow_html=True)
        BloodPressure = st.text_input('Blood Pressure (60–90 mmHg)', placeholder="e.g. 72", key="bp")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h4>Glucose & Insulin</h4>", unsafe_allow_html=True)
        Glucose = st.text_input('Glucose Level (70–150 mg/dL)', placeholder="e.g. 110", key="glucose")
        Insulin = st.text_input('Insulin Level (15–276 μU/mL)', placeholder="e.g. 80", key="insulin")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h4>Body Composition</h4>", unsafe_allow_html=True)
        SkinThickness = st.text_input('Skin Thickness (10–50 mm)', placeholder="e.g. 23", key="skin")
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h4>Additional Metrics</h4>", unsafe_allow_html=True)
        BMI = st.text_input('BMI (18.5–40 kg/m²)', placeholder="e.g. 31.6", key="bmi")
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function (0.1–2.5)', placeholder="e.g. 0.47", key="dpf")
        st.markdown("</div>", unsafe_allow_html=True)

    # Prediction button
    st.markdown("<div style='text-align: center; margin: 30px 0;'>", unsafe_allow_html=True)
    if st.button('🔍 Get AI Diabetes Prediction', type="primary", key="diabetes_button"):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])
            prediction_proba = diabetes_model.predict_proba([user_input])[0][1] * 100

            st.markdown(create_risk_meter(prediction_proba), unsafe_allow_html=True)
            
            if diab_prediction[0] == 1:
                st.markdown(f"""
                <div class='result-card danger-card'>
                    <h3>⚠️ High Risk of Diabetes ({prediction_proba:.1f}%)</h3>
                    <p>Our AI model indicates a significant likelihood of diabetes based on your health parameters.</p>
                    <div style='background: rgba(244,67,54,0.1); padding: 15px; border-radius: 8px; margin-top: 15px;'>
                        <h4>📌 Recommended Actions:</h4>
                        <ul style='margin-bottom: 0;'>
                            <li>Schedule an appointment with an endocrinologist</li>
                            <li>Begin regular blood glucose monitoring</li>
                            <li>Consult a dietitian for meal planning</li>
                            <li>Start an exercise program (150 mins/week)</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='result-card success-card'>
                    <h3>✅ Low Risk of Diabetes ({prediction_proba:.1f}%)</h3>
                    <p>Our AI model does not detect significant signs of diabetes based on your current health metrics.</p>
                    <div style='background: rgba(76,175,80,0.1); padding: 15px; border-radius: 8px; margin-top: 15px;'>
                        <h4>💡 Prevention Strategies:</h4>
                        <ul style='margin-bottom: 0;'>
                            <li>Maintain balanced diet with complex carbohydrates</li>
                            <li>Continue regular physical activity</li>
                            <li>Annual HbA1c testing if over 40</li>
                            <li>Monitor weight and blood pressure</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
        except ValueError:
            st.error("❗ Please enter valid numeric values in all fields.")
        except Exception as e:
            st.error(f"❗ An error occurred: {str(e)}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Additional information
    st.markdown("---")
    st.markdown("## 📚 Diabetes Health Information")
    
    tab1, tab2, tab3 = st.tabs(["Risk Factors", "Symptoms", "Prevention"])
    
    with tab1:
        st.markdown("""
        <div class='card'>
            <h3>🔍 Major Diabetes Risk Factors</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🧬</span>
                    <div>
                        <h4>Genetic Factors</h4>
                        <p>Family history of diabetes increases risk by 2-6x</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🏋️</span>
                    <div>
                        <h4>Lifestyle Factors</h4>
                        <p>Physical inactivity and poor diet</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🩸</span>
                    <div>
                        <h4>Medical Conditions</h4>
                        <p>Prediabetes, PCOS, gestational diabetes</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>👶</span>
                    <div>
                        <h4>Other Factors</h4>
                        <p>Age >45, ethnicity, low HDL cholesterol</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class='card'>
            <h3>🛑 Early Warning Signs</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🚰</span>
                    <div>
                        <h4>Increased Thirst</h4>
                        <p>Excessive thirst (polydipsia)</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🚽</span>
                    <div>
                        <h4>Frequent Urination</h4>
                        <p>Especially at night (polyuria)</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>😴</span>
                    <div>
                        <h4>Fatigue</h4>
                        <p>Persistent tiredness</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>👁️</span>
                    <div>
                        <h4>Blurred Vision</h4>
                        <p>Fluid shifts affecting lenses</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class='card'>
            <h3>🛡️ Prevention Strategies</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🥗</span>
                    <div>
                        <h4>Dietary Changes</h4>
                        <p>High fiber, low glycemic index foods</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🏃</span>
                    <div>
                        <h4>Physical Activity</h4>
                        <p>150 mins moderate exercise weekly</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>⚖️</span>
                    <div>
                        <h4>Weight Management</h4>
                        <p>5-7% weight loss if overweight</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🩺</span>
                    <div>
                        <h4>Regular Screening</h4>
                        <p>Annual checks if at risk</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.caption("""
    <div style='text-align: center; margin-top: 30px; color: #666;'>
        ℹ️ This AI tool provides risk assessment only. For diagnosis and treatment, consult a healthcare professional.
    </div>
    """, unsafe_allow_html=True)

# AI Heart Disease Prediction Page
if selected == 'AI Heart Disease Prediction':
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title('AI Heart Disease Prediction')
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3050/3050159.png", width=80)
    
    # Information card
    with st.expander("📊 About Heart Disease Prediction", expanded=True):
        st.write("""
        Our advanced AI evaluates multiple cardiovascular parameters to assess your heart disease risk.
        For optimal accuracy, please provide your most recent cardiac metrics.
        """)
        st.markdown("""
        <div class='risk-meter'></div>
        <div style='display: flex; justify-content: space-between; margin-top: 5px;'>
            <span>Low Risk</span>
            <span>Moderate Risk</span>
            <span>High Risk</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Input columns with placeholders and ranges
    st.markdown("### 🩺 Cardiac Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><h4>Basic Information</h4>", unsafe_allow_html=True)
        age = st.text_input('Age (29–77 years)', placeholder="e.g. 45", key="h_age")
        sex = st.text_input('Sex (0=Female, 1=Male)', placeholder="0 or 1", key="h_sex")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h4>Blood Pressure</h4>", unsafe_allow_html=True)
        trestbps = st.text_input('Resting BP (94–200 mmHg)', placeholder="e.g. 120", key="h_bp")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h4>Cholesterol & ECG</h4>", unsafe_allow_html=True)
        chol = st.text_input('Cholesterol (126-564 mg/dL)', placeholder="e.g. 240", key="h_chol")
        restecg = st.text_input('Resting ECG (0-2)', placeholder="0=normal, 1=abnormality, 2=hypertrophy", key="h_ecg")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h4>Exercise Metrics</h4>", unsafe_allow_html=True)
        exang = st.text_input('Exercise Angina (0=No, 1=Yes)', placeholder="0 or 1", key="h_exang")
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><h4>Heart Function</h4>", unsafe_allow_html=True)
        thalach = st.text_input('Max Heart Rate (71-202 bpm)', placeholder="e.g. 150", key="h_thalach")
        oldpeak = st.text_input('ST Depression (0-6.2)', placeholder="e.g. 1.2", key="h_oldpeak")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='card'><h4>Additional Metrics</h4>", unsafe_allow_html=True)
        slope = st.text_input('ST Slope (0-2)', placeholder="0=up, 1=flat, 2=down", key="h_slope")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Second row of inputs
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card'><h4>Chest Pain</h4>", unsafe_allow_html=True)
        cp = st.text_input('Chest Pain Type (0-3)', placeholder="0=typical, 1=atypical, 2=non-anginal, 3=asymptomatic", key="h_cp")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'><h4>Blood Sugar</h4>", unsafe_allow_html=True)
        fbs = st.text_input('Fasting BS >120 (0=No, 1=Yes)', placeholder="0 or 1", key="h_fbs")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'><h4>Advanced Metrics</h4>", unsafe_allow_html=True)
        ca = st.text_input('Major Vessels (0-3)', placeholder="0-3 vessels", key="h_ca")
        thal = st.text_input('Thalassemia (0-3)', placeholder="0=normal, 1=fixed, 2=reversible, 3=other", key="h_thal")
        st.markdown("</div>", unsafe_allow_html=True)

    # Prediction button
    st.markdown("<div style='text-align: center; margin: 30px 0;'>", unsafe_allow_html=True)
    if st.button('🔍 Get AI Heart Disease Prediction', type="primary", key="heart_button"):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), 
                         float(chol), float(fbs), float(restecg), float(thalach),
                         float(exang), float(oldpeak), float(slope), float(ca), 
                         float(thal)]

            heart_prediction = heart_disease_model.predict([user_input])
            prediction_proba = heart_disease_model.predict_proba([user_input])[0][1] * 100

            st.markdown(create_risk_meter(prediction_proba), unsafe_allow_html=True)
            
            if heart_prediction[0] == 1:
                st.markdown(f"""
                <div class='result-card danger-card'>
                    <h3>⚠️ High Risk of Heart Disease ({prediction_proba:.1f}%)</h3>
                    <p>Our AI model indicates significant cardiovascular risk based on your parameters.</p>
                    <div style='background: rgba(244,67,54,0.1); padding: 15px; border-radius: 8px; margin-top: 15px;'>
                        <h4>📌 Recommended Actions:</h4>
                        <ul style='margin-bottom: 0;'>
                            <li>Schedule immediate cardiology consultation</li>
                            <li>Complete lipid profile and stress test</li>
                            <li>Begin heart-healthy diet (Mediterranean)</li>
                            <li>Start supervised exercise program</li>
                            <li>Monitor blood pressure daily</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='result-card success-card'>
                    <h3>✅ Low Risk of Heart Disease ({prediction_proba:.1f}%)</h3>
                    <p>Our AI model shows no significant signs of cardiovascular disease currently.</p>
                    <div style='background: rgba(76,175,80,0.1); padding: 15px; border-radius: 8px; margin-top: 15px;'>
                        <h4>💡 Prevention Strategies:</h4>
                        <ul style='margin-bottom: 0;'>
                            <li>Maintain regular aerobic exercise</li>
                            <li>Follow balanced, low-sodium diet</li>
                            <li>Annual cardiac screening after 40</li>
                            <li>Manage stress through mindfulness</li>
                            <li>Avoid tobacco and limit alcohol</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
        except ValueError:
            st.error("❗ Please enter valid numeric values in all fields.")
        except Exception as e:
            st.error(f"❗ An error occurred: {str(e)}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Additional information
    st.markdown("---")
    st.markdown("## 📚 Cardiac Health Information")
    
    tab1, tab2, tab3 = st.tabs(["Risk Factors", "Symptoms", "Prevention"])
    
    with tab1:
        st.markdown("""
        <div class='card'>
            <h3>🔍 Major Cardiac Risk Factors</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🩸</span>
                    <div>
                        <h4>Hypertension</h4>
                        <p>BP >130/80 mmHg increases risk</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🧪</span>
                    <div>
                        <h4>Cholesterol</h4>
                        <p>High LDL or low HDL levels</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🚬</span>
                    <div>
                        <h4>Lifestyle</h4>
                        <p>Smoking, sedentary habits</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🧬</span>
                    <div>
                        <h4>Genetics</h4>
                        <p>Family history of heart disease</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class='card'>
            <h3>🛑 Warning Signs</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>💢</span>
                    <div>
                        <h4>Chest Discomfort</h4>
                        <p>Pressure, squeezing, or pain</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>😫</span>
                    <div>
                        <h4>Shortness of Breath</h4>
                        <p>With or without chest discomfort</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>💫</span>
                    <div>
                        <h4>Lightheadedness</h4>
                        <p>Dizziness or fainting spells</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🦵</span>
                    <div>
                        <h4>Leg Swelling</h4>
                        <p>Fluid retention in extremities</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class='card'>
            <h3>🛡️ Prevention Strategies</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🏃</span>
                    <div>
                        <h4>Regular Exercise</h4>
                        <p>150 mins moderate activity weekly</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🥑</span>
                    <div>
                        <h4>Heart-Healthy Diet</h4>
                        <p>Mediterranean diet pattern</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🧘</span>
                    <div>
                        <h4>Stress Management</h4>
                        <p>Mindfulness and relaxation</p>
                    </div>
                </div>
                <div style='display: flex; align-items: flex-start;'>
                    <span class='feature-icon'>🩺</span>
                    <div>
                        <h4>Regular Checkups</h4>
                        <p>Annual cardiac screening</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.caption("""
    <div style='text-align: center; margin-top: 30px; color: #666;'>
        ℹ️ This AI assessment doesn't replace medical evaluation. Seek professional care for symptoms.
    </div>
    """, unsafe_allow_html=True)