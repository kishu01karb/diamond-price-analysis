#STEP 9: MAKE PREDICTIONS ON NEW DIAMONDS 

import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_model():
    lr_model= joblib.load( "linear_regression_model.pkl")
    rf_model=joblib.load("random_forest_model.pkl")
    label_encoder=joblib.load( "label_encoder.pkl")
    return lr_model,rf_model, label_encoder

lr_model, rf_model, label_encoder = load_model()

def predict_diamond_price(carat,cut,color,clarity,depth,table,x,y,z):
    """ 
    Predict the price of a diamond based on its characteristics
    """
    
    # encode the categorical features
    cut_encoded = label_encoder['cut'].transform([cut])[0]
    color_encoded = label_encoder['color'].transform([color])[0]
    clarity_encoded = label_encoder['clarity'].transform([clarity])[0]
    
    #create feature  array
    features =np.array([[carat,cut_encoded,color_encoded,clarity_encoded,depth,table,x,y,z]])
    
    #predict with both models
    price_lr = lr_model.predict(features)[0]
    price_rf = rf_model.predict(features)[0]
    avg_price = (price_lr + price_rf)/2
    
    
    st.subheader(f"\n Diamond charcteristics:")
    st.write(f" Carat : {carat}, Cut:{cut},Color:{color},Clarity:{clarity},DepthL{depth},Table:{table},X:{x},Y:{y},Z:{z}")
    st.write(f"\n Predicted Prices:")
    st.subheader(f"  Linear Regression: $ {price_lr:.2f}")
    st.write(f"  Random Forest:     $ {price_rf:.2f}")
    st.write(f"  Average Prediction:$ {(price_lr + price_rf)/2:.2f}")
    
    return avg_price

st.title("💎 Diamond Price Predictor")

carat = st.number_input("Carat",min_value=0.01,step=0.01)
cut = st.selectbox("Cut", label_encoder['cut'].classes_)
color =st.selectbox("Color", label_encoder['color'].classes_)
clarity =st.selectbox("Clarity", label_encoder['clarity'].classes_)
depth = st.number_input("Depth",min_value=0.0,step=0.1)
table= st.number_input("Table",min_value=0.0,step=0.1)
x= st.number_input("X(length in mm)", min_value=0.0,step=0.01)
y= st.number_input("Y(length in mm)", min_value=0.0,step=0.01)
z= st.number_input("Z(length in mm)", min_value=0.0,step=0.01)

if st.button("Predict Price"):
    predict_diamond_price(carat,cut,color ,clarity,depth,table,x,y,z)
