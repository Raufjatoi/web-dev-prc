import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("iris_model.pkl")

# App title
st.title("Iris Flower Species Prediction")

# Input fields for features
st.write("Enter flower characteristics:")
sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

# Make prediction
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    st.write("Predicted Iris Species:", prediction[0])
