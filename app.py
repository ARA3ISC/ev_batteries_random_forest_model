import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("random_forest_model.pkl")

st.title("EV Battery Performance Predictor 🚗🔋")

# Sidebar inputs
st.sidebar.header("Enter Input Features")

# Numeric inputs
soc = st.sidebar.slider("SOC (%)", 0, 100, 50)
voltage = st.sidebar.number_input("Voltage (V)", 0.0, 1000.0, 400.0)
current = st.sidebar.number_input("Current (A)", 0.0, 500.0, 100.0)
battery_temp = st.sidebar.number_input("Battery Temp (°C)", -20.0, 80.0, 25.0)
ambient_temp = st.sidebar.number_input("Ambient Temp (°C)", -20.0, 50.0, 25.0)
charging_cycles = st.sidebar.number_input("Charging Cycles", 0, 2000, 500)
optimal_class = st.sidebar.selectbox("Optimal Charging Duration Class", [0, 1, 2])

# Encoding dictionaries for categorical features
charging_mode_encoding = {"Normal": 0, "Slow": 1, "Fast": 2}
battery_type_encoding = {"Li-ion": 0, "LiFePO4": 1}
ev_model_encoding = {"Model A": 0, "Model B": 1, "Model C": 2}

# Select boxes for categorical features (show friendly text)
charging_mode = st.sidebar.selectbox("Charging Mode", list(charging_mode_encoding.keys()))
battery_type = st.sidebar.selectbox("Battery Type", list(battery_type_encoding.keys()))
ev_model = st.sidebar.selectbox("EV Model", list(ev_model_encoding.keys()))

# Encode categorical features
charging_mode_encoded = charging_mode_encoding[charging_mode]
battery_type_encoded = battery_type_encoding[battery_type]
ev_model_encoded = ev_model_encoding[ev_model]

# Prepare input dataframe
input_df = pd.DataFrame([[
    soc, voltage, current, battery_temp, ambient_temp,
    charging_mode_encoded, battery_type_encoded,
    charging_cycles, ev_model_encoded, optimal_class
]], columns=[
    'SOC (%)', 'Voltage (V)', 'Current (A)', 'Battery Temp (°C)', 'Ambient Temp (°C)',
    'Charging Mode', 'Battery Type', 'Charging Cycles', 'EV Model', 'Optimal Charging Duration Class'
])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.subheader("Predicted Outputs")
    st.write(f"Charging Duration (min): {prediction[0][0]:.2f}")
    st.write(f"Efficiency (%): {prediction[0][1]:.2f}")
    st.write(f"Degradation Rate (%): {prediction[0][2]:.2f}")
