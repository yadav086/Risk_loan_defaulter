'''import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('loan_model.pkl')

st.title("💳 Loan Default Prediction App")

st.write("Enter customer details to predict loan default")

# ✅ Input fields

person_age = st.number_input("Age", min_value=18, max_value=100, value=30)
person_income = st.number_input("Income", min_value=0, value=50000)
person_emp_exp = st.number_input("Experience (years)", min_value=0, value=5)
loan_amnt = st.number_input("Loan Amount", min_value=0, value=10000)
loan_int_rate = st.number_input("Interest Rate", min_value=0.0, value=10.0)
loan_percent_income = st.number_input("Loan % Income", min_value=0.0, value=0.2)
cb_person_cred_hist_length = st.number_input("Credit History Length", min_value=0, value=5)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)

# ✅ categorical inputs
person_gender = st.selectbox("Gender", ["male", "female"])
person_education = st.selectbox("Education", ["High School", "Bachelor", "Master", "PhD"])
person_home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE"])
loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"])
previous_loan_defaults_on_file = st.selectbox("Previous Defaults", ["Yes", "No"])

# ✅ Predict button
if st.button("Predict"):

    # Create dataframe
    data = pd.DataFrame({
        'person_age': [person_age],
        'person_income': [person_income],
        'person_emp_exp': [person_emp_exp],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'cb_person_cred_hist_length': [cb_person_cred_hist_length],
        'credit_score': [credit_score],
        'person_gender': [person_gender],
        'person_education': [person_education],
        'person_home_ownership': [person_home_ownership],
        'loan_intent': [loan_intent],
        'previous_loan_defaults_on_file': [previous_loan_defaults_on_file]
    })

    # Prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    # Output
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ High Risk of Default (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low Risk (Probability: {probability:.2f})")

import streamlit as st
import pandas as pd
import joblib
import base64

# ✅ Page config
st.set_page_config(
    page_title="Loan Risk Predictor",
    page_icon="💳",
    layout="wide"
)

# ✅ Convert image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ✅ Set background
def set_bg():
    img = get_base64_of_bin_file("background.jpg")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(0,0,0,0.6), 
                rgba(0,0,0,0.6)
            ),
            url("data:image/png;base64,{img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .card {{
            background-color: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 5px 20px rgba(0,0,0,0.3);
        }}

        .title {{
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #f1f2f6;
        }}

        .subtitle {{
            text-align: center;
            color: #dcdde1;
            margin-bottom: 30px;
        }}

        .stButton>button {{
            background-color: #0A3D62;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Apply background
set_bg()

# ✅ Load model
model = joblib.load("loan_model.pkl")

# ✅ Title
st.markdown('<div class="title">💳 Loan Default Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered credit risk analysis system</div>', unsafe_allow_html=True)

# ✅ Layout
col1, col2 = st.columns([2, 1])

# ✅ INPUT SECTION
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Applicant Details")

    c1, c2 = st.columns(2)

    with c1:
        person_age = st.number_input("Age", 18, 100, 30)
        person_income = st.number_input("Income", 0, 1000000, 50000)
        person_emp_exp = st.number_input("Experience (years)", 0, 40, 5)
        credit_score = st.number_input("Credit Score", 300, 900, 650)

    with c2:
        loan_amnt = st.number_input("Loan Amount", 0, 500000, 10000)
        loan_int_rate = st.number_input("Interest Rate (%)", 0.0, 30.0, 10.0)
        loan_percent_income = st.number_input("Loan % Income", 0.0, 1.0, 0.2)
        cb_person_cred_hist_length = st.number_input("Credit History Length", 0, 30, 5)

    st.subheader("🏠 Personal Info")

    c3, c4 = st.columns(2)

    with c3:
        person_gender = st.selectbox("Gender", ["male", "female"])
        person_education = st.selectbox("Education", ["High School", "Bachelor", "Master", "PhD"])

    with c4:
        person_home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE"])
        loan_intent = st.selectbox("Loan Purpose", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"])

    previous_loan_defaults_on_file = st.selectbox("Previous Default", ["Yes", "No"])

    st.markdown('</div>', unsafe_allow_html=True)

# ✅ OUTPUT SECTION
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Prediction")

    if st.button("🔍 Predict Risk", use_container_width=True):

        data = pd.DataFrame({
            'person_age': [person_age],
            'person_income': [person_income],
            'person_emp_exp': [person_emp_exp],
            'loan_amnt': [loan_amnt],
            'loan_int_rate': [loan_int_rate],
            'loan_percent_income': [loan_percent_income],
            'cb_person_cred_hist_length': [cb_person_cred_hist_length],
            'credit_score': [credit_score],
            'person_gender': [person_gender],
            'person_education': [person_education],
            'person_home_ownership': [person_home_ownership],
            'loan_intent': [loan_intent],
            'previous_loan_defaults_on_file': [previous_loan_defaults_on_file]
        })

        prob = model.predict_proba(data)[0][1]
        threshold = 0.5
        pred = int(prob >= threshold)

        st.markdown("---")

        if pred == 1:
            st.error("⚠️ High Risk of Default")
            st.metric("Risk Probability", f"{prob:.2f}")
        else:
            st.success("✅ Low Risk Customer")
            st.metric("Risk Probability", f"{prob:.2f}")

    st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import joblib

# ✅ Page config
st.set_page_config(
    page_title="Loan Risk Predictor",
    page_icon="💳",
    layout="wide"
)

# ✅ Clean professional styling
st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fa;
    }

    .title {
        text-align: center;
        font-size: 36px;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 15px;
        color: #6c757d;
        margin-bottom: 30px;
    }

    .card {
        background: #ffffff;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e6e9ef;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    .stButton>button {
        background-color: #2c5282;
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-weight: 600;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1a365d;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ✅ Load model
model = joblib.load("loan_model.pkl")

# ✅ Header
st.markdown('<div class="title">💳 Loan Default Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart AI-driven credit risk analysis</div>', unsafe_allow_html=True)

# ✅ Layout
col1, col2 = st.columns([2, 1])

# ✅ INPUT SECTION
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📋 Applicant Details")

    c1, c2 = st.columns(2)

    with c1:
        person_age = st.number_input("Age", 18, 100, 30)
        person_income = st.number_input("Income", 0, 1000000, 50000)
        person_emp_exp = st.number_input("Experience (years)", 0, 40, 5)
        credit_score = st.number_input("Credit Score", 300, 900, 650)

    with c2:
        loan_amnt = st.number_input("Loan Amount", 0, 500000, 10000)
        loan_int_rate = st.number_input("Interest Rate (%)", 0.0, 30.0, 10.0)
        loan_percent_income = st.number_input("Loan % Income", 0.0, 1.0, 0.2)
        cb_person_cred_hist_length = st.number_input("Credit History Length", 0, 30, 5)

    st.subheader("🏠 Personal Information")

    c3, c4 = st.columns(2)

    with c3:
        person_gender = st.selectbox("Gender", ["male", "female"])
        person_education = st.selectbox("Education", ["High School", "Bachelor", "Master", "PhD"])

    with c4:
        person_home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE"])
        loan_intent = st.selectbox("Loan Purpose", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"])

    previous_loan_defaults_on_file = st.selectbox("Previous Defaults", ["Yes", "No"])

    st.markdown('</div>', unsafe_allow_html=True)

# ✅ OUTPUT SECTION
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Prediction")

    if st.button("🔍 Predict Risk", use_container_width=True):

        data = pd.DataFrame({
            'person_age': [person_age],
            'person_income': [person_income],
            'person_emp_exp': [person_emp_exp],
            'loan_amnt': [loan_amnt],
            'loan_int_rate': [loan_int_rate],
            'loan_percent_income': [loan_percent_income],
            'cb_person_cred_hist_length': [cb_person_cred_hist_length],
            'credit_score': [credit_score],
            'person_gender': [person_gender],
            'person_education': [person_education],
            'person_home_ownership': [person_home_ownership],
            'loan_intent': [loan_intent],
            'previous_loan_defaults_on_file': [previous_loan_defaults_on_file]
        })

        prob = model.predict_proba(data)[0][1]
        threshold = 0.5
        pred = int(prob >= threshold)

        st.markdown("---")

        # ✅ Clean metric display
        st.metric("Default Probability", f"{prob:.2%}")

        if pred == 1:
            st.error("⚠️ High Risk Customer")
        else:
            st.success("✅ Low Risk Customer")

    st.markdown('</div>', unsafe_allow_html=True)'''

import streamlit as st
import pandas as pd
import joblib

# ✅ Page config
st.set_page_config(
    page_title="Loan Default Predictor",
    page_icon="💳",
    layout="wide"
)

# ✅ Styling (better readability)
st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fa;
    }

    .title {
        text-align: center;
        font-size: 34px;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6c757d;
        margin-bottom: 25px;
    }

    .card {
        background: white;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e6e9ef;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    label {
        font-weight: 600 !important;
        color: #1e3a5f !important;
    }

    .stButton>button {
        background-color: #2c5282;
        color: white;
        border-radius: 8px;
        padding: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ✅ Load model
model = joblib.load("loan_model.pkl")

# ✅ Header
st.markdown('<div class="title">💳 Loan Default Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered credit risk evaluation</div>', unsafe_allow_html=True)

# ✅ Layout
col1, col2 = st.columns([2, 1])

# ✅ INPUT SECTION
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📋 Applicant Details")

    c1, c2 = st.columns(2)

    with c1:
        person_income = st.number_input("💰 Income", 0, 1000000, 50000)
        loan_amnt = st.number_input("🏦 Loan Amount", 0, 500000, 10000)
        credit_score = st.number_input("📊 Credit Score", 300, 900, 650)
        person_emp_exp = st.number_input("👔 Experience (years)", 0, 40, 5)

    with c2:
        loan_percent_income = st.number_input("📈 Loan % Income", 0.0, 1.0, 0.2)
        person_home_ownership = st.selectbox("🏠 Home Ownership", ["RENT", "OWN", "MORTGAGE"])
        loan_intent = st.selectbox("📌 Loan Purpose", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"])
        previous_loan_defaults_on_file = st.selectbox("⚠️ Previous Defaults", ["Yes", "No"])

    st.markdown('</div>', unsafe_allow_html=True)

# ✅ OUTPUT SECTION
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Prediction Result")

    if st.button("🔍 Predict Risk", use_container_width=True):

        data = pd.DataFrame({
            'person_age': [30],
            'person_income': [person_income],
            'person_emp_exp': [person_emp_exp],
            'loan_amnt': [loan_amnt],
            'loan_int_rate': [10],
            'loan_percent_income': [loan_percent_income],
            'cb_person_cred_hist_length': [5],
            'credit_score': [credit_score],
            'person_gender': ['male'],
            'person_education': ['Bachelor'],
            'person_home_ownership': [person_home_ownership],
            'loan_intent': [loan_intent],
            'previous_loan_defaults_on_file': [previous_loan_defaults_on_file]
        })

        prob = model.predict_proba(data)[0][1]
        pred = int(prob >= 0.5)

        st.markdown("---")

        # ✅ Clear visible probability
        color = "#e74c3c" if prob > 0.5 else "#27ae60"

        st.markdown(
            f"""
            <div style="
                background:#f8fafc;
                padding:15px;
                border-radius:10px;
                text-align:center;
                border:1px solid #e2e8f0;
            ">
                <h4 style="color:#555;">Default Probability</h4>
                <h2 style="color:{color}; font-weight:700;">
                    {prob:.2%}
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        if pred == 1:
            st.error("⚠️ High Risk Customer")
        else:
            st.success("✅ Low Risk Customer")

    st.markdown('</div>', unsafe_allow_html=True)



