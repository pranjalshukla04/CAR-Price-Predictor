import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb

import joblib
date_time = datetime.datetime.now()
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

    st.markdown(
        """
        <style>
        body {
            background-image: url('https://raw.githubusercontent.com/pranjalshukla04/CAR-Price-Predictor/main/MB.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin-top: 10rem; /* Adjust this value to center the content vertically */
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Container for header and content
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.write('<h2 style="color: white;">Predict Car Prices with AI Magic</h2>', unsafe_allow_html=True)

    
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write("### Are you planning to sell your car?")
    st.write("### Let's try evaluating the price...")
    
    st.write('')
    st.write('')
    p1 = st.number_input('What is the current ex-showroom price of the car ?  (In Lakhs)',2.5,25.0,step=1.0) 
    
    
    p2 = st.number_input('What is distance completed by the car in Kilometers ?',100,50000000,step=100)

    s1 = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'))
    if s1=="Petrol":
        p3=0
    elif s1=="Diesel":
        p3=1
    elif s1=="CNG":
        p3=2
        
    s2 = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'))
    
    if s2=="Dealer":
        p4=0
    elif s2=="Indivisual":
        p4=1
        
    s3 = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'))
    if s3=="Manual":
        p5=0
    elif s3=="Automatic":
        p5=1
        
    p6 = st.slider("Number of Owners the car previously had",0,3)
    
    
    years = st.number_input('In which year car was purchased ?',1990,date_time.year,step=1)
    p7 = date_time.year-years
    
    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    try: 
        if st.button('Predict'):
            prediction = model.predict(data_new)
            if prediction>0:
                st.balloons()
                st.success('You can sell the car for {:.2f} lakhs'.format(prediction[0]))
            else:
                st.warning("You will be not able to sell this car !!")
    except:
        st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    main()
