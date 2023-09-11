import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
import prediction
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"]="python"

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import load_model



def run() :
  # Load Model
  with open('preprocessor_nn.pkl', 'rb') as file_1:
    preprocessor = pickle.load(file_1)
  model_churn = load_model('nn_best_model.h5', compile=False)



  #form untuk data inference
  with st.form('key=form_client_subscribe_term_deposit'):
        st.write('#### **MASUKKAN DATA DIRI ANDA**')
        full_name=st.text_input('Full Name', value='')
        age=st.number_input('age', min_value=0, max_value=90, step=1, help='Usia Penumpang?')
        job=st.selectbox('job',['management' ,'student' ,'technician' ,'admin.' ,'blue-collar','self-employed', 'services' ,'retired' ,'unemployed', 'housemaid','entrepreneur', 'unknown'], index=1, help='Jenis Kelamin Penumpang?')
        education=st.selectbox('education', ['tertiary' ,'secondary', 'unknown' ,'primary'], index=1, help='Jenis Kelamin Penumpang?')
        st.markdown('-----')
        st.write('#### **MASUKKAN INFORMASI**')
      
        balance=st.number_input('balance', min_value=0, max_value=100000, step=1, help= 'waktu keterlambatan kedatangan (menit)')      
        marital=st.selectbox('marital',[0, 1, 2], index=1 ,help='Kenyamanan kursi yang Anda Tumpangi? 0: No rate, 5: Sangat Baik')
        default=st.selectbox('default', [0, 1], index=1)
        housing=st.selectbox('housing', [0, 1], index=1)
        loan=st.selectbox('loan', [0, 1], index=1)
        month=st.selectbox('month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], index=1)
      
        

        st.markdown('----------------')
        duration=st.slider('duration',0,67,1000, help='Lokasi gerbang keberangkatan dan kedatangan? 0: No comment, 5:Sangat Baik')
        campaign= st.slider('campaign', 0,3,40, help='Pelayanan selama perjalanan? 0: No comment, 5:Sangat Baik')
        pdays= st.slider('pdays', 0,3,40, help='Pelayanan selama perjalanan? 0: No comment, 5:Sangat Baik')
        previous= st.slider('previous', 0,3,40, help='Pelayanan selama perjalanan? 0: No comment, 5:Sangat Baik')
        last_contact_day= st.slider('last_contact_day', 0,3,400, help='Pelayanan selama perjalanan? 0: No comment, 5:Sangat Baik')
        
        st.markdown('-----')

        submitted=st.form_submit_button('Predict')

  #Input data baru dari test dan lihat hasil death eventnya, apakah sesuai atau tidak
  #data inference
  data_inf = {
        'name': full_name,
        'age': age,
        'job':job,
        'marital':marital,
        'education':education,
        'default':default,
        'balance':balance,
        'housing': housing,
        'loan':loan,
        'duration':duration,
        'campaign': campaign,
        'pdays':pdays,
        'previous': previous,
        'last_contact_day':last_contact_day
  }


  data_inf = pd.DataFrame([data_inf])
  data_inf

  if submitted :
    # Feature Scaling and Feature Encoding
    data_final = preprocessor.transform(data_inf)

    # Predict using Linear Regression
    y_inf_pred = np.where(model_churn.predict(data_final) >= 0.5, 1, 0)
    
    if y_inf_pred == 1:
      prediction = 'subscribe'
    else:
      prediction = 'Not subscribe'

    st.write('##### This customer is predicted:', prediction)

if __name__ == '__main__':
    run()