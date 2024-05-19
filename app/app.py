import streamlit as st
from streamlit_lottie import st_lottie
import pickle
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import numpy as np
import re
import json

import constants

def validate_input(user_input):
    errors = []
    inputs = []
    for f in constants.FEATURES_UNORDERED:
        if f not in user_input or user_input[f].strip() == "":
            errors.append(f"{constants.FEATURES[f]} is required.")
            inputs.append(None)
        else:
            try:
                inputs.append(float(user_input[f]))
            except ValueError:
                errors.append(f"{constants.FEATURES[f]} must be a number.")
                inputs.append(None)
    return inputs, errors


# Load the scaler
with open('../ml_dev/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.set_page_config(page_title="Pollutant Predictor", page_icon=":lungs:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

left, _, right = st.columns(3)
with left:
    with st.container():
        st.title("Air Quality Predictor", anchor=False)
        
        st.caption(f"Based on [De Vito et al. (2008)]({constants.INTRO_PAPER})")
        st.caption(f"[Data Source]({constants.DATA_SOURCE})")


with open("assets/animation.json", "r") as f:
    with right:
        st_lottie(json.load(f), height=250, width=250)

with st.container():

    st.header("Enter the values for the features to predict the next hour's air quality.", divider='blue', anchor=False)
    
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Feature values for the current hour:", anchor=False)
        # input fields for each feature
        user_input = {}
        for feature, desc in constants.FEATURES.items():
            user_input[feature] = st.text_input(f'{desc}', placeholder=f"e.g., {constants.FEATURES_MEAN[feature]}")


    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    with right_column:    
        if st.button("Predict values for the next hour!"):
            
            input_vals, errors = validate_input(user_input)
            if errors:
                for error in errors:
                    with right_column:
                        st.error(error)
            else:
                model = tf.keras.models.load_model('../ml_dev/lstm_autoencoder.h5')
                print(f"input vals: {input_vals}")
                input_vals = np.array(input_vals).reshape(1, -1)
                rh = input_vals[:, 10].reshape(-1, 1) 
                input_vals = scaler.transform(input_vals[:, [i for i in range(input_vals.shape[1]) if i != 10]])
                input_vals = np.insert(input_vals, 10, rh/100, axis=1)
                input_arr = input_vals.reshape((1, 1, 12))

                y_pred = model.predict(input_arr).reshape(-1, 12)
                # scale features except rh
                input_to_invert = y_pred[:, [i for i in range(y_pred.shape[1]) if i != 10]]
                outputs = scaler.inverse_transform(input_to_invert)
                outputs = np.insert(outputs, 10, y_pred[:, 10], axis=1)
                print(outputs)

                #st.subheader("Predicted values for the next hour:", anchor=False)
                for feature in constants.FEATURES_ORDERED:
                    val = outputs.reshape(len(constants.FEATURES))[constants.FEATURES_UNORDERED.index(feature)]
                    st.write("")
                    st.success(f"{re.sub(r'^True h', 'H', constants.FEATURES[feature])}: {val:.3f}")

        st.markdown('</div>', unsafe_allow_html=True)