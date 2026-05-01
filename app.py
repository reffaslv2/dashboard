import streamlit as st
from data import *

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

    #Load & Filter Data
    df = load_data()
    year = select_year()
    location = select_location(df)
    df_filtered = filter_data(df, year, location)
    #Kolom 1
    kolom(df_filtered)
    pie_chart1(df_filtered)
    bar_chart1(df_filtered)
    bar_chart2(df_filtered)
    map_chart(df_filtered, year)

elif menu == "Halaman Data":
    judul()
    df = load_data()
    year = select_year()
    location = select_location(df)
    df_filtered = filter_data(df, year, location)
    show_data(df_filtered)