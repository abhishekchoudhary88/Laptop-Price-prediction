import streamlit as st
import pandas as pd
import pickle
import os
import streamlit as st
import pickle

# st.write("Current working directory:", os.getcwd())
# st.write("Files in current dir:", os.listdir())
# st.write("Files in app dir:", os.listdir(os.path.dirname(__file__)))

# ===============================
# Load trained model
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "laptop_price_model.pkl")

data = pickle.load(open(model_path, "rb"))

model = data["model"]
model_columns = data["columns"]

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

st.title("💻 Laptop Price Prediction App")
st.write("Enter laptop details to predict the estimated price")

# ===============================
# User Inputs
# ===============================

brand = st.selectbox(
    "Laptop Brand",
    ["HP", "Dell", "Lenovo", "Asus", "Acer", "Apple", "MSI"]
)

ram = st.selectbox(
    "RAM (GB)",
    [4, 8, 16, 32]
)

storage = st.selectbox(
    "Storage (ROM)",
    ["256GB SSD", "512GB SSD", "1TB HDD", "1TB SSD"]
)

weight = st.number_input(
    "Laptop Weight (kg)",
    min_value=0.5,
    max_value=5.0,
    step=0.1
)

# ===============================
# Prediction
# ===============================
if st.button("🔮 Predict Price"):

    input_dict = {
        "ram": ram,
        "weight": weight,
        f"brand_{brand}": 1,
        f"storage_{storage}": 1
    }

    input_df = pd.DataFrame([input_dict])

    # Align with training columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)

    st.success(f"💰 Estimated Laptop Price: ₹ {int(prediction[0])}")



