import streamlit as st
from model import predict_threat

st.title("AI Driven Cloud Threat Detection")

st.subheader("Cloud Infrastructure Monitoring")

cpu = st.slider("CPU Usage",0,100)
login = st.slider("Login Attempts",0,20)
traffic = st.slider("Network Traffic",0,1000)

if st.button("Analyze Activity"):
    
    result = predict_threat(cpu,login,traffic)
    
    st.write("Threat Status:", result)