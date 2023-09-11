import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'PREDICT CLIENT SUBSCRIBE'))

if navigation == 'EDA':
      eda.run()
else: 
      prediction.run()