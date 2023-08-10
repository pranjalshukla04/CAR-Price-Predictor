import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb


def main(): 
    html_temp="""
     <div style = "background-color:lightblue;padding:16px">
     <h2 style="color:black;text-align:center;"> Car Price Prediction Using ML</h2>
     </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
   

if __name__ == '__main__':
    main()