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
