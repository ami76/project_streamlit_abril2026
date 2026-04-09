import streamlit as st
from pickle import load

MODEL_PATH = "models/model.pkl"

model = load(open(MODEL_PATH, "rb"))

class_dict = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica"
}

st.title("Iris - Model prediction")
st.write("Introduce the values")

val1 = st.number_input("Petal width", format="%.4f")
val2 = st.number_input("Petal length", format="%.4f")
val3 = st.number_input("Sepal width", format="%.4f")
val4 = st.number_input("Sepal length", format="%.4f")

if st.button("Predict"):
    data = [[val1, val2, val3, val4]]
    prediction = str(model.predict(data)[0])
    pred_class = class_dict[prediction]
    st.success(f"Prediction: {pred_class}")