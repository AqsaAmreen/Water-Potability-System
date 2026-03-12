# app.py

import streamlit as st
import pickle
import os
import numpy as np

# -----------------------------
# Multi-Language Dictionary
# -----------------------------
LANGUAGES = {
    "English": {
        "title": "💧 Water Potability Prediction System",
        "instruction": "Enter water quality parameters to check if water is safe to drink.",
        "predict": "Predict",
        "safe": "✅ Water is SAFE to drink",
        "unsafe": "❌ Water is NOT safe to drink"
    },

    "Spanish": {
        "title": "💧 Sistema de Predicción de Potabilidad del Agua",
        "instruction": "Ingrese parámetros de calidad del agua para verificar si es segura para beber.",
        "predict": "Predecir",
        "safe": "✅ El agua es SEGURA para beber",
        "unsafe": "❌ El agua NO es segura para beber"
    }
}

# -----------------------------
# Language Selector
# -----------------------------
language = st.sidebar.selectbox("Select Language", list(LANGUAGES.keys()))
T = LANGUAGES[language]

# -----------------------------
# Function to load model safely
# -----------------------------
def load_model(filename):
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, filename)

    if not os.path.exists(model_path):
        st.error(f"Error: {filename} not found in {base_dir}")
        return None

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model


# -----------------------------
# Load ML Model
# -----------------------------
model = load_model("random_forest_model.pkl")

if model is None:
    st.stop()

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Water Potability Prediction", page_icon="💧")

st.title(T["title"])
st.write(T["instruction"])

# -----------------------------
# User Inputs
# -----------------------------
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
# Prediction
# -----------------------------
if st.button(T["predict"]):

    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon,
                            trihalomethanes, turbidity]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success(T["safe"])
    else:
        st.error(T["unsafe"])
