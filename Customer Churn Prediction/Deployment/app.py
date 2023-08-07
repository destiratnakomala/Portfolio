import streamlit as st
import eda
import prediction
from PIL import Image

# Set Config dan icon
st.set_page_config(
        page_title='Churn Prediction',
        layout='wide',
        )


#klik eda, bawa ke page eda
navigation = st.sidebar.selectbox('Select Page (EDA/Churn Prediction):', ('EDA', 'Churn Prediction'))
#menambahkan gambar
image_pred = Image.open('image_pred.jpg')
st.sidebar.image(image_pred, use_column_width=True)



#Run modul dengan if else
if navigation == 'EDA':
    eda.run()
else :
    prediction.run()