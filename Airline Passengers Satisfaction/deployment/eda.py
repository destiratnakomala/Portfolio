import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='AIRLINE-SATISFACTORY',
    layout = 'wide',
    initial_sidebar_state='expanded'
)

def run():

    #membuat title
    st.title('Airline Satisfactory Prediction')
    st.write('~ Milstone2-Desti Ratna Komala-RMT-020')


    #Membuat Sub Header
    st.subheader('EDA Analisis Dataset Airline Satisfactory Prediction')

    #menambahkan Gambar 
    image = Image.open('airline.jpg')
    st.image(image, caption='Airline')

    #membuat garis lurus 
    st.markdown('-----')

    #magic syntax
    '''
    Pada page kali ini, penulis akan melakukan ekplorasi sederhana. 
    Dataset yang digunakan adalah dataset Airline Satisfactory
    '''
    #Membuat Sub Header
    st.subheader('Dataset Airline Satisfactory')
    #show dataframe
    data=pd.read_csv('https://raw.githubusercontent.com/destiratnakomala/Hacktiv8_Folder/main/INVISTICO.csv')
    st.dataframe(data)

    #------------------------------------------------
    #1. EDA--------
    #membuat barplot jumlah tiap data kategori
    st.write('#### Plot satisfactory')
    #Visualisasikan satisfied/dissatisfied

    fig=plt.figure(figsize=(15,5))
    fig, ax =plt.subplots(1,2,figsize=(10,5))

    sns.countplot(x='satisfaction', data=data, palette="pastel", ax=ax[0])
    ax[0].set_xlabel("Satisfactory", fontsize= 12)
    ax[0].set_ylabel("# of Passenger", fontsize= 12)
    fig.suptitle('Jumlah dan Persen Kepuasan Passanger', fontsize=12, fontweight='bold')
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+20), ha='center', va='center',fontsize = 11)

    data['satisfaction'].value_counts().plot(kind='pie',labels = ['',''], autopct='%1.1f%%', colors = sns.color_palette('pastel')[0:5], explode = [0,0.05], textprops = {"fontsize":11})
    ax[1].set_ylabel("% of Passanger", fontsize= 12)
    plt.legend(labels=['dissatisfied', 'satisfied'])
    st.pyplot(fig)
#----------------------------------------------------------------------
    st.markdown('-----')
    #Ubah satisfaction menjadi binary
    df=data.copy()
    df['satisfaction']=df['satisfaction'].map({'satisfied': 1, 'dissatisfied': 0})

    pilihanuser=st.selectbox('Pilih Column:',('Gender', 'Customer Type', 'Type of Travel',
       'Class', 'Seat comfort',
       'Departure/Arrival time convenient', 'Food and drink', 'Gate location',
       'Inflight wifi service', 'Inflight entertainment', 'Online support',
       'Ease of Online booking', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Cleanliness', 'Online boarding'))

    fig=plt.figure(figsize=(20,4))
    fig, ax =plt.subplots(1,2,figsize=(10,5))
    fig.suptitle('Jumlah dan Persen Kepuasan Passanger', fontsize=12, fontweight='bold')
    #visualisasikan data
    
    plt.subplot(1,2,1)
    plt.title("Passanger terhadap satisfactory", fontsize=12)
    ax = sns.countplot(data = df, x = df[pilihanuser], hue="satisfaction", palette = 'pastel')
    plt.ylabel("# of satisfactory", fontsize= 10)

    for p in ax.patches:
        ax.annotate((p.get_height()), (p.get_x()+0.01, p.get_height()+5))


    plt.subplot(1,2,2)
    plt.title("Passanger terhadap Persen Kepuasan", fontsize=12)
    ax = sns.barplot(x = df[pilihanuser], y = "satisfaction", data = df, palette = 'pastel', errorbar= None)
    plt.ylabel("% Kepuasan", fontsize= 12)
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.3, p.get_height()+0.01),fontsize=10)
    st.pyplot(fig)



    #----------------------------------------------------------------------------------------
    fig=plt.figure(figsize=(15, 5))
    pilihanuser2=st.selectbox('Pilih Column:',('Age','Departure Delay in Minutes', 'Arrival Delay in Minutes','Flight Distance' ))
    plt.subplot(1,2,1)
    sns.distplot(df[pilihanuser2])
    plt.ticklabel_format(style='plain', axis='x')
    plt.ylabel('')

    plt.subplot(1,2,2)
    sns.kdeplot(df.loc[(df['satisfaction'] == 0), pilihanuser2], label = 'dissatisfied', fill = True)
    sns.kdeplot(df.loc[(df['satisfaction'] == 1), pilihanuser2], label = 'satisfied', fill = True)
    plt.ylabel('')
    plt.legend()
    st.pyplot(fig)

#------------------------------------

#run eda
if __name__=='__main__':
    run()