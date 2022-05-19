from distutils.log import error
import streamlit as st
import pandas as pd
import numpy as np

Data_Product = {
    101:"Beras Putih",	
    102:"Gula Pasir",
    103:"Gula Jawa",
    104:"Mie Instan",
    105:"Telur Ayam",
    106:"Minyak Goreng",
    107:"Susu Bubuk",
    108:"Susu Kental",
    109:"Susu UHT",
    110:"T. Terigu",
    111:"T. Maizena",
    112:"T. Tapioka",
    113:"T. Beras",
    114:"T. Ketan",
    115:"Kopi Hitam",
    116:"Kecap Manis",
    117:"Kecap Asin",
}
Daftar_Harga = {
    101: 15000,
    102: 12000,
    103: 28000,
    104: 48000,
    105: 20000,
    106: 21000,
    107: 35000,
    108: 15000,
    109: 6000,
    110: 18000,
    111: 17000,
    112: 15000,
    113: 12000,
    114: 19000,
    115: 10000,
    116: 13000,
    117: 13000,
}

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    st.session_state.button_clicked = True


st.title('Toko Sederhana')
barang = pd.DataFrame(
    {
        'Nama Produk': Data_Product,
        'Harga Produk': Daftar_Harga
    })

st.table(barang)
 
produk = st.selectbox(
     'Pilih ID Produk',
     (Data_Product))
name = st.text_input('Nama Pembeli')
address = st.text_input('Alamat Pembeli')
no_hp = st.text_input('Nomor HP')
ekspedisi = st.text_input(' Ekspedisi Pengiriman')

method = st.radio(
     "Metode Pembayaran",
     ('Transfer Bank', 'Cash on Delivery'))
st.write('Harga ', Data_Product[produk], 'adalah Rp.', Daftar_Harga[produk])
input_price = st.number_input(' Masukan nominal pembayaran', min_value=0)

result = st.button('Bayar', on_click=callback) or st.session_state.button_clicked

if result:
    if name ==  '' or address ==  '' or no_hp ==  '' or ekspedisi == '' or input_price == '':
        st.warning('Isian tidak boleh kosong')
    else:
        # TABLE
        # buyer = pd.DataFrame({
        #     'Nama Pembeli': [name],
        #     'Alamat Pembeli': [address],
        #     'Nomor Hp Pembeli': [no_hp],
        #     'Ekspedisi Pembeli': [ekspedisi],
        #     'Barang yang dibeli': [Data_Product[produk]],
        #     'Harga barang': [Daftar_Harga[produk]],
        #     'Metode Pembayaran': [method],
        #     'Uang yang dibayarkan': [input_price],
        # })
        # st.table(buyer)
        # TEXT
        st.write('Nama Pembeli :', name)
        st.write('Alamat Pembeli :', address)
        st.write('No Hp Pembeli :', no_hp)
        st.write('Ekspedisi :', ekspedisi)
        st.write('Barang yang di beli :', Data_Product[produk])
        st.write('Harga Barang yang di beli : Rp.', Daftar_Harga[produk])
        st.write('Metode pembayaran :', method)
        st.write('Uang yang dibayarkan : Rp.', input_price)

        st.write('Apakah anda yakin ingin melakukan pembelian ?')
        confirm = st.button('Yes')
        cancel = st.button('No')
        if confirm:
            if input_price < Daftar_Harga[produk]:
                st.info('Uang yang anda masukan kurang')
            else:
                st.success('Proses Transaksi Berhasil')
        
        if cancel:
            st.error('Proses Transaksi Batal')




