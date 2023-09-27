import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.write('Workcloud Cyberbullying Tweets')

    # Import DF
    df_eda = pd.read_csv('https://raw.githubusercontent.com/destiratnakomala/Hacktiv8_Folder/main/cyberbully.csv')


    # Membuat Sub Header
    st.subheader('**Persebaran Kategori Tweet**')

    # Membuat visualisasi Distribusi Tweet
    fig, ax =plt.subplots(1,2,figsize=(15,6))

    sns.countplot(x='cyberbullying_type', data=df_eda, palette="pastel", ax=ax[0])
    ax[0].set_xlabel("cyberbullying_type", fontsize= 10)
    ax[0].set_ylabel("#tweet", fontsize= 10)
    fig.suptitle('Distribution cyberbullying_type', fontsize=10, fontweight='bold')

    ax[0].tick_params(axis='x', rotation=90)
    plt.xlabel("cyberbullying_type", fontsize= 10)
    plt.ylabel("#tweet", fontsize= 10)

    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+50), ha='center', va='center',fontsize = 10)

    df_eda['cyberbullying_type'].value_counts().plot(kind='pie',autopct='%1.1f%%',colors = sns.color_palette('pastel')[0:7], textprops = {"fontsize":10})
    ax[1].set_ylabel("%tweet", fontsize= 10)
    st.pyplot(fig)


    # Membuat Sub Header
    st.subheader('**All Tweet**')
    #st.image('1.png')

    # Membuat Sub Header
    st.subheader('**Not Cyberbullying Tweet**')
    st.image('2.png')

    # Membuat Sub Header
    st.subheader('**Gender Tweet**')
    st.image('3.png')

    # Membuat Sub Header
    st.subheader('**Religion Tweet**')
    st.image('4.png')

    # Membuat Sub Header
    st.subheader('**Other Cyberbullying Tweet**')
    st.image('5.png')

    # Membuat Sub Header
    st.subheader('**Age Tweet**')
    st.image('6.png')

    
if __name__ == '__main__':
    run()