import json
import requests
import streamlit as st
import tensorflow

url = 'https://2281-34-170-171-60.ngrok-free.app/LeavesCount_prediction'  # Replace with your Ngrok URL

input_data_for_model = {
    'waterTemperature': 25.5,
    'waterPh': 6.8,
    'waterSr': 0.3,
    'waterOrp': 65,
    'waterTds': 9,
    'waterEc': 14,
    'Day': 31
}

response = requests.post(url, json=input_data_for_model)

if response.status_code == 200:
    prediction = response.json()["prediction"]
    print("Prediction:", prediction)
    st.write("Prediction:", round(prediction[0][0],0))
else:
    print("Error:", response.text)
    st.write("Prediction:", prediction)
