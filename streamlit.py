# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:12:27 2023

@author: Gabriel Yashim
"""

import numpy as np 
import pickle
import streamlit as st


model = pickle.load(open('GradientBoost1.pkl', 'rb'))


st.title('Breast Cancer Prediction System')
html_temp = """
    <h3 style="color:white;text-align:center;">By Gabriel Yashim</h3>
    <div style="background-color:#F45B94;padding:10px;margin-bottom:3rem">
        <p style="text-align:justify;">
            Breast cancer is a cancer that develops in the breast and spreads to other parts of the body. It can begin in either one or both of the breasts. <br> 
                The majority of breast cancers are carcinomas, which are tumors that begin in the epithelial cells that line the organs and tissues in the body. Adenocarcinoma, which begins in cells in the ducts (milk ducts) or the lobules, is the most common kind of carcinoma that forms in the breast (glands in the breast that make milk). When cells proliferate out of control, cancer develops. <br>
                This system can predict between the two types of breast cancer (Benign = B, Malignant = M), all you need do is to supply the required information. <br>
                All you need to do is fill the form below:
        </p>  
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

# create columns for our UI
col1, col2, col3 = st.columns(3)


with col1:
# Input field for column1
    te_me = st.text_input("TEXTURE MEAN")
    ar_me = st.text_input("AREA MEAN")
    sm_me = st.text_input("SMOOTHNESS MEAN")
    co_me = st.text_input("COMPACTNESS MEAN")
    con_me = st.text_input("CONCAVITY MEAN")
    sy_me = st.text_input("SYMMETRY MEAN")
    fdm = st.text_input("FRACTAL DIMENSION MEAN")
    


with col2:
# Dropdown select box for age range
    ra_se = st.text_input("RADIUS SE")
    te_se = st.text_input("TEXTURE SE")
    ar_se = st.text_input("AREA SE")
    sm_se = st.text_input("SMOOTHNESS SE")
    co_se = st.text_input("COMPACTNESS SE")
    con_se = st.text_input("CONCAVITY SE")
    cps = st.text_input("CONCAVE POINTS SE")




with col3:
# Dropdown select box for age range
    sy_se = st.text_input("SYMMETRY SE")
    fds = st.text_input("FRACTAL DIMENSION SE")
    sm_wo = st.text_input("SMOOTHNESS WORST")
    co_wo = st.text_input("COMPACTNESS WORST")
    con_wo = st.text_input("CONCAVITY WORST")
    sy_wo = st.text_input("SYMMETRY WORST")
    fdw = st.text_input("FRACTAL DIMENSION WORST")
    

cancer_pred = ''

results = ''


if st.button('Submit'):
    cancer_pred = model.predict([[te_me,ar_me,sm_me,co_me,con_me,sy_me,fdm,ra_se,te_se,
                               ar_se,sm_se,co_se,con_se,cps,sy_se,
                               fds,sm_wo,co_wo,con_wo,sy_wo,fdw]])
    if cancer_pred[0] == 'M':
        results = 'Malignant'
    else:
        results = 'Benign'
        
    st.write(f"The type of cancer is: {results}")
    




