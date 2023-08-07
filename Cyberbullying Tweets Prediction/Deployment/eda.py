import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run() :
    # Membuat Sub Header
    st.title('**EDA Churn Customer**')
    st.write('~ P2M1-Desti Ratna Komala-RMT-020')
    #menambahkan Gambar 
    image = Image.open('image_pred.jpg')
    st.image(image, caption='churn.jpg')

    # Import df
    df_eda = pd.read_csv('https://raw.githubusercontent.com/destiratnakomala/Hacktiv8_Folder/main/churn.csv')

    #membuat garis lurus 
    st.markdown('-----')

    #magic syntax
    '''
    Pada page ini, akan dilakukan ekplorasi dataset sederhana. 
    Berikut adalah dataset Customer Churn yang digunakan
    '''
    #membuat title
    st.subheader('Customer Churn EDA')
    
    # Import df
    df = pd.read_csv('https://raw.githubusercontent.com/destiratnakomala/Hacktiv8_Folder/main/churn.csv')
    st.dataframe(df)






    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Customer* yang *churn* lebih banyak dari pada *customer* yang tidak *churn*')
    #membuat garis lurus 
    st.markdown('-----')
    pilihanuser=st.selectbox('Pilih Feature:', ('gender', 'region_category', 'membership_category', 'joined_through_referral', 'preferred_offer_types', 'medium_of_operation', 'internet_option', 'used_special_discount', 'offer_application_preference', 'past_complaint', 'complaint_status', 'feedback'))


    #--------------------------------------------

    fig, ax =plt.subplots(1,3,figsize=(25,8))
    fig.suptitle(f'{pilihanuser} terhadap Customer Churn', fontsize=17, fontweight='bold')
    #visualisasikan data

    plt.subplot(1,3,1)
    plt.title(f'{pilihanuser} terhadap Customer Churn', fontsize=14)
    ax = sns.countplot(data = df, x = df[pilihanuser], hue="churn_risk_score", palette = 'pastel')
    plt.ylabel("#churn", fontsize= 14)
    plt.xticks(rotation=90)
    plt.legend(loc=0)

   
    plt.subplot(1,3,2)
    plt.title(f'{pilihanuser} terhadap %Customer Churn', fontsize=12)
    ax = sns.barplot(x = df[pilihanuser], y = "churn_risk_score", data = df, palette = sns.color_palette('pastel')[1:2], errorbar= None)
    plt.ylabel("%Churn", fontsize= 14)
    plt.xticks(rotation=90)
    
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.3, p.get_height()+0.005),fontsize=12)
        
    plt.subplot(1,3,3)
    round(df[pilihanuser].value_counts()/df.shape[0]*500,2).plot.pie(autopct= '%1.1f%%',colors=sns.color_palette('pastel')[0:10],shadow=True, legend=None)
    plt.ylabel("")
    plt.xticks(rotation=45)
    plt.title(pilihanuser, fontsize=14)
    st.pyplot(fig)


    st.markdown('-----')
    fig=plt.figure(figsize=(15, 5))
    pilihanuser2=st.selectbox('Pilih Feature Numerik:',('age','days_since_last_login', 'avg_time_spent','avg_transaction_value', 'avg_frequency_login_days', 'points_in_wallet'))
    plt.subplot(1,2,1)
    sns.distplot(df[pilihanuser2])
    plt.ticklabel_format(style='plain', axis='x')
    plt.ylabel('')

    plt.subplot(1,2,2)
    sns.kdeplot(df.loc[(df['churn_risk_score'] == 0), pilihanuser2], label = 'not_churn', fill = True)
    sns.kdeplot(df.loc[(df['churn_risk_score'] == 1), pilihanuser2], label = 'churn', fill = True)
    plt.ylabel('')
    plt.legend()
    st.pyplot(fig)




    #membuat garis lurus 
    st.markdown('-----')


if __name__ == '__main__':
    run()