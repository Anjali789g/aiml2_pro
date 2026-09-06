
import streamlit as st

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(180deg,#030712,#0F172A);
}
.hero{
    background: linear-gradient(135deg,#1E3A8A,#0EA5E9);
    padding:25px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:25px;
}
.card{
    background: rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:18px;
    padding:18px;
}
.stButton>button{
    width:100%;
    border-radius:14px;
    background:#2563EB;
    color:white;
    font-weight:bold;
    height:50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🚀 Customer Churn Prediction</h1>
<p>AI-powered dashboard to predict which telecom customers are likely to leave.</p>
</div>
""", unsafe_allow_html=True)

st.title("📊 Customer Churn Prediction")
st.write("Welcome! This is our first AI/ML web app.")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    monthly = st.number_input("Monthly Charges", min_value=0.0, value=500.0)
    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

if st.button("🔮 Predict Churn"):
    st.success("Frontend is working! Step 11 mein real prediction aayega.")