import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='BANK-MARKETING-DEPOSIT',  
    initial_sidebar_state='expanded'
)


def run():

    #membuat title
    st.markdown("<h1 style='text-align: center;'>Term Deposit Client-Subscription Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>~ Final Project-Desti Ratna Komala-RMT-020</h6>", unsafe_allow_html=True)
    #membuat garis lurus 
        #menambahkan Gambar 
    image = Image.open('banking.jpg')
    st.image(image, caption='')
    st.markdown('-----')
    #Membuat Sub Header
    st.markdown("<h4 style='text-align: center;'>Exploratory Data Analysis</h4>", unsafe_allow_html=True)


   

    #magic syntax
    '''
    Berikut adalah eksplorasi data  yang digunakan adalah bank marketing in Vietnam
    '''
    #Membuat Sub Header
    st.markdown("<h5 style='text-align: left;'> ► Dataset Bank Marketing Vietnam</h5>", unsafe_allow_html=True)
    #show dataframe
    data=pd.read_csv(r"C:\Users\Rein\Desktop\BANK MARKETING\bank_marketing.csv")
    st.dataframe(data)

    #------------------------------------------------
    #1. EDA--------
    #def visualisasi
    df_eda=data.copy()

    #membuat barplot jumlah tiap data kategori
    st.write('##### ► Distribusi Data Term Deposit')
    #Visualisasikan satisfied/dissatisfied
    df_eda=data.copy()

    fig=plt.figure(figsize=(15,5))
    fig, ax =plt.subplots(1,2,figsize=(10,5))

    sns.countplot(x='term_deposit', data=df_eda,palette = sns.color_palette('pastel')[0:10], ax=ax[0])
    ax[0].set_xlabel("term_deposit", fontsize= 12)
    ax[0].set_ylabel("# of client", fontsize= 12)
    fig.suptitle('Client- term_deposit Distribution', fontsize=12, fontweight='bold')
    ax[0].set_ylim(0,4250)
    plt.xlabel("term_deposit", fontsize= 10)
    plt.ylabel("# of Client", fontsize= 10)
    ax[0].set_xticks([0,1], ['Not Subscribe', 'Subscribe'])
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+100), ha='center', va='center',fontsize = 10)

    df_eda['term_deposit'].value_counts().plot(kind='pie', labels = ['subscribe', 'Not subscribe'],autopct='%1.1f%%', textprops = {"fontsize":10}, colors = sns.color_palette('pastel')[0:10])
    ax[1].set_ylabel("% of Client", fontsize= 10)

    st.pyplot(fig)
    st.markdown('Berdasarkan informasi diatas, karena sebelumnya telah dilakukan resampling undersampling. Sehingga distribusi data pada term_deposit memiliki data yang sudah seimbang/balanced dan akan mencegah hasil pemodelan cenderung not_subscribe (data mayoritas).')
#----------------------------------------------------------------------
    st.markdown('-----')

    #1 plotdrwaing
    #tampilkan histplot
    df_eda=data.copy()
    df=data.copy()

    #age
    #distribusi age
    st.write('#### ► Informasi Data Klien')
    fig=plt.figure(figsize=(8, 6))
    age_plt = sns.histplot(data = df_eda[df_eda['age'] <= 100]['age'], color = 'pink')
    age_plt.set_ylabel('# % clients', fontsize = 13)
    age_plt.set_xlabel('Age', fontsize = 13)
    age_plt.set_title('# % client terhadap age', fontsize = 14)
    st.pyplot(fig)
    '''Berdasarkan gambar tersebut:\n
- Umur klien memiliki range dari 18 tahun hingga 95 tahun\n
- Kebanyakan klien yang berumur 30 tahun yang menjadi klien di bank ini.'''


    fig=plt.figure(figsize=(10,4))
    age_dep = sns.kdeplot(data = df_eda, x = 'age', hue = 'term_deposit', multiple="stack", palette= 'pastel')
    age_dep.set_ylabel('# of clients', fontsize = 13)
    age_dep.set_xlabel('age', fontsize = 13)
    age_dep.set_title('deposit terhadap Age', fontsize = 14)
    st.pyplot(fig)
    '''Selanjutnya, dilakukan pembagian kategori umur (dewasa Muda, Paruh Baya, Lansia) berdasarkan DepKes RI untuk melihat pengaruh deposit terhadap kategori umur.'''




    #----------------------------------------------------------------------------------------

#run eda
if __name__=='__main__':
    run()