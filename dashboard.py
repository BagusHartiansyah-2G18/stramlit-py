import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

from streamlit_elements import elements, mui, html
sns.set(style='dark')

dtahun = pd.read_csv("./resultData/orderTahunan.csv")
dprodukTerjual = pd.read_csv("./resultData/produkTerjual.csv")
produkKategoriTerjual = pd.read_csv("./resultData/produkKategoriTerjual.csv")
transaksiBulanan = pd.read_csv("./resultData/transaksiBulanan.csv")
itemTransaksi = pd.read_csv("./resultData/itemTransaksi.csv")
customer = pd.read_csv("./resultData/customer.csv")

colors = ["#F99090", "#FFDE4D", "#68FF74", "#4F86FF", "#DD55FF"]
tahun = '2018'


with elements("newElement"):
    col1, col2 = st.columns(2)
     
    col1.image('./dev-mini.png',use_column_width=False, width=80)
    with col2:
        c2a, c2b, c2c  = st.columns(3)
        with c2a:
            st.text('Data')
        with c2b:
            st.text('Grafik')
        with c2c:
            st.text('Kesimpulan')
        


with st.form(key='dataTahun'):
    st.table(dtahun)

    submitted = st.form_submit_button("Reset")
    if submitted:
       st.write('Ok')


with st.form(key='dataProduk'):
    st.header('Produk aktif Tahun '+ tahun)  
    values = []
    for val in dprodukTerjual.keys():
        values.append(dprodukTerjual[val][0])

    # st.header(values) 
    # fig, ax = plt.subplots(figsize=(20, 10))
    # ax.bar(dprodukTerjual.keys(), [100, 200 ,200])

    fig, ax = plt.subplots(figsize=(20, 10))
     
    sns.barplot(y="y", x="x", 
        data={ 'x' : dprodukTerjual.keys(), 'y': values}, 
        palette=colors )
    st.pyplot(fig)

    submitted = st.form_submit_button("Reset")
    if submitted:
       st.write('Ok')


with st.form(key='dataProdukMinMax'):
    st.header('Daftar kategori Produk terlaris '+ tahun)  
    st.table(produkKategoriTerjual)
    submitted = st.form_submit_button("Reset")
    if submitted:
       st.write('Ok')

with st.form(key='dataTransaksiBulanan'):
    st.header('Daftar Transaksi Bulanan Tahun '+ tahun)  
    # st.table(produkKategoriTerjual)

    fig, ax = plt.subplots(figsize=(20, 10))
     
    sns.barplot(y="total", x="bulan", 
        data=transaksiBulanan, 
        palette=colors )
    st.pyplot(fig)

    submitted = st.form_submit_button("Reset")
    if submitted:
       st.write('Ok')

with st.form(key='dataItemTransaksi'):
    st.header('total item setiap transaksi Tahun '+ tahun)  
    st.table(itemTransaksi)

    submitted = st.form_submit_button("Reset")
    if submitted:
       st.write('Ok')

with st.form(key='dataCostumer'):
    st.header('Jumlah Customer Aktif Tahun '+ tahun)  
    values = []
    for val in customer.keys():
        values.append(customer[val][0]) 

    fig, ax = plt.subplots(figsize=(20, 10))
     
    sns.barplot(y="y", x="x", 
        data={ 'x' : customer.keys(), 'y': values}, 
        palette=colors )
    st.pyplot(fig)
    submitted = st.form_submit_button("Reset")
    if submitted:
       st.write('Ok')
