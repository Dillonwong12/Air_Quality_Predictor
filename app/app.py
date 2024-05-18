import streamlit as st
import pickle
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import numpy as np
import constants

# Load the scaler
with open('../ml_dev/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

model = tf.keras.models.load_model('../ml_dev/lstm_autoencoder.h5')


st.set_page_config(page_title="Pollutant Predictor", page_icon=":lungs:", layout="wide")

with st.container():
    st.title("Air Quality Predictor")
    
    st.write(f"Based on [De Vito et al. (2008)]({constants.INTRO_PAPER})")
    st.write(f"[Data Source]({constants.DATA_SOURCE})")


with st.container():


    st.write("Enter the values for the features to predict the next day's air quality.")

    # input fields for each feature
    user_input = {}
    for feature, desc in constants.FEATURES.items():
        user_input[feature] = st.text_input(f'{desc}', placeholder=f"e.g., {constants.FEATURES_MEAN[feature]}")


    if st.button("Predict"):
        inputs = []
        for f in constants.FEATURES_ORDERED:
            inputs.append(float(user_input[f]))
        input_vals = np.array(inputs).reshape(1, -1)
        rh = input_vals[:, 10].reshape(-1, 1) 
        input_vals = scaler.transform(input_vals[:, [i for i in range(input_vals.shape[1]) if i != 10]])
        input_vals = np.insert(input_vals, 10, rh/100, axis=1)
        input_arr = input_vals.reshape((1, 1, 12))

        y_pred = model.predict(input_arr).reshape(-1, len(constants.FEATURES))
        # scale features except rh
        input_to_invert = y_pred[:, [i for i in range(y_pred.shape[1]) if i != 10]]
        outputs = scaler.inverse_transform(input_to_invert)
        outputs = np.insert(outputs, 10, y_pred[:, 10], axis=1)
        print(outputs)

        st.write("Predicted values for the next day:")
        for feature, val in zip(constants.FEATURES.values(), outputs.reshape(len(constants.FEATURES))):
            st.write(f"{feature}: {val}")
        