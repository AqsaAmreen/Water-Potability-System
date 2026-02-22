# app.py
import streamlit as st
import pickle
import os

# -----------------------------
# Function to load model safely
# -----------------------------
def load_model(filename):
    # Get the directory where app.py is located
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, filename)

    # Check if file exists
    if not os.path.exists(model_path):
        st.error(f"Error: {filename} not found in {base_dir}")
        return None

    # Load the model
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

# -----------------------------
# Load model
# -----------------------------
model = load_model("model.pkl")

if model is None:
    st.stop()  # Stop app if model not found

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Water Potability Prediction")

# Example: Ask user for input features
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=100.0)
solids = st.number_input("Solids (ppm)", min_value=0.0, value=1000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=5.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=500.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=5.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=80.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=3.0)

# -----------------------------
# Make prediction
# -----------------------------
if st.button("Predict"):
    input_data = [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Water is Potable")
    else:
        st.warning("⚠️ Water is Not Potable")
        model = load_model("models/model.pkl")