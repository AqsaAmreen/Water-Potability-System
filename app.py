import streamlit as st
import pickle
import numpy as np

# Page title
st.set_page_config(page_title="Water Potability Prediction", page_icon="💧")

st.title("💧 Water Potability Prediction System")

st.write("Enter water quality parameters to check if water is safe to drink.")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# User inputs
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", value=200.0)
solids = st.number_input("Total Dissolved Solids", value=10000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=300.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", value=80.0)
turbidity = st.number_input("Turbidity", value=4.0)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon,
                            trihalomethanes, turbidity]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Water is SAFE to drink.")
    else:
        st.error("❌ Water is NOT safe to drink.")