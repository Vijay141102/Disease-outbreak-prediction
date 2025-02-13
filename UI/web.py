import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Set up page configuration
st.set_page_config(
    page_title="Disease Prediction Outbreak System",
    page_icon="🩺",
    layout="wide"
)

# Load trained models
diabetes_model = pickle.load(open(r"C:\Users\vijay\OneDrive\Pictures\Documents\DISEASE OUTBREAK PREDICTION\training_models\diabetic_model.sav", "rb"))
heart_disease_model = pickle.load(open(r"C:\Users\vijay\OneDrive\Pictures\Documents\DISEASE OUTBREAK PREDICTION\training_models\heart_model.sav", "rb"))
parkinson_model = pickle.load(open(r"C:\Users\vijay\OneDrive\Pictures\Documents\DISEASE OUTBREAK PREDICTION\training_models\parkinsons_model.sav", "rb"))


# Sidebar navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2777/2777267.png", width=100)
    st.title("🔍 Disease Prediction System")
    st.markdown("Select an option from below:")

    selected = option_menu(
        "Navigation",
        ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson’s Prediction"],
        icons=["house", "activity", "heart", "person"],
        default_index=0,
    )

# Function to display prediction results
def display_result(prediction, disease_name):
    if prediction[0] == 1:
        st.success(f"✅ The person **has {disease_name}**.")
    else:
        st.warning(f"❌ The person **does not have {disease_name}**.")

# Home Page
if selected == "Home":
    st.title("🏥 Welcome to Disease Prediction System")
    st.markdown("""
    This system helps predict the likelihood of **Diabetes, Heart Disease, and Parkinson’s Disease**  
    based on user inputs using **Machine Learning Models**.  
    **Select a disease from the sidebar to proceed.**
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/4140/4140047.png", width=400)

# Diabetes Prediction Page
elif selected == "Diabetes Prediction":
    st.title("🩸 Diabetes Prediction")
    st.markdown("Enter the required details below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
        SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0.0)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)

    with col2:
        Glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.0)
        Insulin = st.number_input("Insulin Level (IU/mL)", min_value=0.0)
        Age = st.number_input("Age (years)", min_value=1, step=1)

    with col3:
        BloodPressure = st.number_input("Blood Pressure (mmHg)", min_value=0.0)
        BMI = st.number_input("BMI (Body Mass Index)", min_value=0.0)

    if st.button("🔎 Get Diabetes Prediction"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        prediction = diabetes_model.predict([user_input])
        display_result(prediction, "Diabetes")

# Heart Disease Prediction Page
elif selected == "Heart Disease Prediction":
    st.title("💓 Heart Disease Prediction")
    st.markdown("Enter the required details below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age (years)")
        trestbps = st.number_input("Resting Blood Pressure (trestbps) [mmHg]")
        restecg = st.number_input("Resting ECG (restecg) [0=Normal, 1=ST-T abnormality, 2=LVH]", min_value=0, max_value=2, step=1)
        oldpeak = st.number_input("ST Depression (oldpeak)")

    with col2:
        sex = st.number_input("Sex [1=Male, 0=Female]", min_value=0, max_value=1, step=1)
        cp = st.number_input("Chest Pain Type (cp) [0=Typical, 1=Atypical, 2=Non-anginal, 3=Asymptomatic]", min_value=0, max_value=3, step=1)
        chol = st.number_input("Serum Cholesterol (chol) [mg/dL]")
        fbs = st.number_input("Fasting Blood Sugar (fbs) [1=True, 0=False]", min_value=0, max_value=1, step=1)

    with col3:
        thalach = st.number_input("Max Heart Rate (thalach) [bpm]")
        exang = st.number_input("Exercise-Induced Angina (exang) [1=Yes, 0=No]", min_value=0, max_value=1, step=1)
        slope = st.number_input("ST Slope (slope) [0=Upsloping, 1=Flat, 2=Downsloping]", min_value=0, max_value=2, step=1)
        ca = st.number_input("Number of Major Vessels (ca)", min_value=0, max_value=3, step=1)
        thal = st.number_input("Thalassemia (thal) [0=Normal, 1=Fixed Defect, 2=Reversible Defect]", min_value=0, max_value=3, step=1)

    if st.button("🔎 Get Heart Disease Prediction"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_disease_model.predict([user_input])
        display_result(prediction, "Heart Disease")

# Parkinson’s Prediction Page
elif selected == "Parkinson’s Prediction":
    st.title("🧠 Parkinson’s Disease Prediction")
    st.markdown("Enter the required details below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.number_input("MDVP:Fo (Hz)")
        MDVP_Fhi = st.number_input("MDVP:Fhi (Hz)")
        MDVP_Flo = st.number_input("MDVP:Flo (Hz)")
        MDVP_Jitter = st.number_input("Jitter (%)")
        MDVP_Jitter_Abs = st.number_input("Jitter Abs")
        MDVP_RAP = st.number_input("MDVP:RAP")
        MDVP_PPQ = st.number_input("MDVP:PPQ")
        Jitter_DDP = st.number_input("Jitter DDP")

    with col2:
        MDVP_Shim = st.number_input("Shimmer")
        MDVP_Shim_dB = st.number_input("Shimmer (dB)")
        Shimmer_APQ3 = st.number_input("Shimmer:APQ3")
        Shimmer_APQ5 = st.number_input("Shimmer:APQ5")
        MDVP_APQ = st.number_input("MDVP:APQ")
        Shimmer_DDA = st.number_input("Shimmer:DDA")
        NHR = st.number_input("NHR")
        HNR = st.number_input("HNR")

    with col3:
        RPDE = st.number_input("RPDE")
        DFA = st.number_input("DFA")
        spread1 = st.number_input("Spread1")
        spread2 = st.number_input("Spread2")
        D2 = st.number_input("D2")
        PPE = st.number_input("PPE")

    if st.button("🔎 Get Parkinson’s Prediction"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                      MDVP_Shim, MDVP_Shim_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA,
                      spread1, spread2, D2, PPE]
        prediction = parkinson_model.predict([user_input])
        display_result(prediction, "Parkinson’s Disease")

st.markdown("---")
st.markdown("⚠ **Disclaimer:** This tool provides a risk assessment based on machine learning predictions. It is not a substitute for medical diagnosis. Please consult a qualified healthcare professional for expert advice.")





