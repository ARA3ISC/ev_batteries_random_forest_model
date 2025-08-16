# ev_batteries_random_forest_model
A Streamlit web app that predicts charging duration, efficiency, and degradation rate of electric vehicle batteries using a trained Random Forest multi-target regression model. Users can input battery and charging parameters via an interactive sidebar, with categorical features encoded automatically to match the model


# EV Battery Performance Predictor 🚗🔋

A **Streamlit web app** that predicts the **charging duration**, **efficiency**, and **degradation rate** of electric vehicle batteries using a trained **Random Forest multi-target regression model**.  

The app allows users to enter battery and charging parameters through an interactive sidebar. Categorical features like **Charging Mode**, **Battery Type**, and **EV Model** are displayed as user-friendly options but automatically encoded to match the trained model.  

---

## Features

- Predicts **Charging Duration (min)**, **Efficiency (%)**, and **Degradation Rate (%)**.  
- Interactive **Streamlit sidebar** for inputting battery parameters.  
- Handles **categorical feature encoding** automatically.  
- Uses a **pre-trained Random Forest Regressor** for accurate multi-target predictions.  

---

## Inputs

| Feature | Type | Options / Range |
|---------|------|----------------|
| SOC (%) | Numeric | 0 – 100 |
| Voltage (V) | Numeric | 0 – 1000 |
| Current (A) | Numeric | 0 – 500 |
| Battery Temp (°C) | Numeric | -20 – 80 |
| Ambient Temp (°C) | Numeric | -20 – 50 |
| Charging Mode | Categorical | Normal / Slow / Fast |
| Battery Type | Categorical | Li-ion / LiFePO4 |
| Charging Cycles | Numeric | 0 – 2000 |
| EV Model | Categorical | Model A / Model B / Model C |
| Optimal Charging Duration Class | Categorical | 0 / 1 / 2 |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ev-battery-predictor.git
cd ev-battery-predictor
```

2. Install dependencies:
```bash
pip install streamlit pandas scikit-learn joblib
```

3. Usage:
```bash
streamlit run app.py
```
Open the link displayed in your browser.
Use the sidebar to input battery and charging parameters.
Click Predict to see the predicted outputs.
