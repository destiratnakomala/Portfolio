import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

#load Model
load_model = joblib.load("logreg_model.pkl")


#def run
def run():



  #form untuk data inference
  with st.form('key=form_airline_satisfactory'):
        st.write('#### **MASUKKAN DATA DIRI ANDA**')
        full_name=st.text_input('Full Name', value='')
        age=st.number_input('age', min_value=0, max_value=90, step=1, help='Usia Penumpang?')
        gender=st.selectbox('gender',['Male', 'Female'], index=1, help='Jenis Kelamin Penumpang?')
        st.markdown('-----')
        st.write('#### **MASUKKAN INFORMASI AIRLINE**')
        customer_type=st.selectbox('customer_type',['Loyal Customer', 'disloyal Customer'], index=1, help='Apakah Anda rutin menggunakan airline kami?')
        type_of_travel=st.selectbox('type_of_travel',['Business travel', 'Personal Travel'], index=1, help='Jenis perjalanan?')
        classish=st.selectbox('class',['Eco Plus', 'Eco', 'Business'], index=1, help='Kelas yang dipilih untuk melakukan perjalanan?')
        flight_distance=st.number_input('flight_distance', min_value=10, max_value=80000, step=1, help= 'Jarak Penerbangan')
        departure_min=st.number_input('departure_delay_min', min_value=0, max_value=10000, step=1, help= 'waktu Keterlambatan keberangkatan (menit)')
        arrival_min=st.number_input('arrival_delay_min', min_value=0, max_value=10000, step=1, help= 'waktu keterlambatan kedatangan (menit)')
        
        
        st.markdown('-----')
        st.write('#### **MASUKKAN RATING PELAYANAN**')
        seat_comfort=st.selectbox('seat_comfort',[0, 1, 2,3,4,5], index=1 ,help='Kenyamanan kursi yang Anda Tumpangi? 0: No rate, 5: Sangat Baik')
        departure=st.selectbox('DA_time_convenient', [0, 1, 2,3,4,5], index=1 , help= 'Waktu kedatangan dan keberangkatan Jarak Penerbangan0: No rate, 5: Sangat Baik')
        food_drink=st.selectbox('food_drink',[0, 1, 2,3,4,5], index=1 , help='Makanan dan minuman yang disajikan? 0: No comment, 5: Sangat Baik')
        online_support=st.selectbox('online_support', [0, 1, 2,3,4,5], index=1, help='support online dari pegawai airline? 0: No comment, 5: Sangat Baik')
        online_booking=st.selectbox('ease_online_booking',[0, 1, 2,3,4,5], index=1, help='Kemudahan melakukan booking tiket? 0: No comment, 5: Sangat Baik')
        inflight_wifi=st.selectbox('inflight_wifi', [0, 1, 2,3,4,5], index=1 , help='Akses wifi selama perjalanan? 0: No comment, 5: Sangat Baik')
        inflight_ent=st.selectbox('inflight_entertain', [0, 1, 2,3,4,5], index=1 , help='Hiburan/film/lagu selama perjalanan? 0: No comment, 5:Sangat Baik')

        st.markdown('----------------')
        st.write('#### MASUKKAN RATING FASILITAS AIRLINE')
        gate_location=st.slider('gate_location',0,3,5, help='Lokasi gerbang keberangkatan dan kedatangan? 0: No comment, 5:Sangat Baik')
        on_board= st.slider('onboard_service', 0,3,5, help='Pelayanan selama perjalanan? 0: No comment, 5:Sangat Baik')
        leg_room=st.slider('legroom_service', 0,3,5, help='Pelayanan penambahan ruang pada kaki? 0: No comment, 5: Sangat Baik')
        baggage=st.slider('baggage_handling', 0,3,5, help='Penanganan bagasi? 0: No comment, 5: Sangat Baik')
        checking=st.slider('checkin_service', 0,3,5, help='pelayanan pada saat check-in? 0: No comment, 5: Sangat Baik')
        clean=st.slider('clealiness', 0,3,5, help='Kebersihan selama perjalanan? 0: No comment, 5: Sangat Baik')
        online_boarding=st.slider('online_boarding', 0,3,5, help='Kemudahan dalam boarding online? 0: No comment, 5: Sangat Baik')
        
        st.markdown('-----')

        submitted=st.form_submit_button('Predict')

  #Input data baru dari test dan lihat hasil death eventnya, apakah sesuai atau tidak
  #data inference
  data_inf = {
        'full_name': full_name,
        'gender': gender,
        'customer_type': customer_type,
        'age':age,
        'type_travel':type_of_travel,
        'class':classish,
        'flight_distance':flight_distance,
        'seat_comfort': seat_comfort,
        'DA_time_convenient':departure,
        'food_drink':food_drink,
        'gate_location':gate_location,
        'inflight_wifi':inflight_wifi,
        'inflight_entertain':inflight_ent,
        'online_support':online_support,
        'ease_online_booking':online_booking,
        'onboard_service':on_board,
       'legroom_service':leg_room,
        'baggage_handling':baggage,
        'checkin_service':checking,
        'clealiness':clean,
       'online_boarding':online_boarding,
        'departure_delay_min':departure_min,
        'arrival_delay_min':arrival_min
      
      
      
    
      

  }
  data_inf = pd.DataFrame([data_inf])
  st.dataframe(data_inf)

  if submitted:

    pred_new= load_model.predict(data_inf)
    pred_new
    if (pred_new == 0):
      st.write('##### Tingkat Kepuasan Anda:', str(int(pred_new)),'-Tidak puas.','\n',' Saran dan Kritik dapat disampaikan di website kami. *Have a nice day and thank you for using our Airlines!*')
    else:
      st.write('##### Tingkat Kepuasan Anda:', str(int(pred_new)),'-Puas.','\n',' Terimakasih telah memilih Airlines Kami. *Have a nice day and thank you for using our Airlines!*')



#run prediction
if __name__=='__main__':
    run()