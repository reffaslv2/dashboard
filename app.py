import streamlit as st
from data import show_data, select_year, load_data, filter_data, kolom, pie_chart1

# Judul Dashboard
def judul():
    st.title("📊Dashboard Covid-19")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data COVID-19 di Indonesia.")

#Sidebar Navigasi
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home","Halaman Data"])

#Halaman Home
if menu == "Home":
    judul()
    #Pilih Tahun
    year = select_year()
    #Load & Filter Data
    df = load_data()
    df_filtered = filter_data(df, year)
    kolom(df_filtered)
    pie_chart1(df_filtered)

elif menu == "Halaman Data":
    judul()
    year = select_year()
    #Load & Filter Data
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)