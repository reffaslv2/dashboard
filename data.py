import streamlit as st
import pandas as pd

#fungsi memuat data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

#fungsi menampilkan data
def show_data():
    df = load_data()
    st.subheader("Data Covid-19 di Indonesia")
    st.dataframe(df.head(10))
    st.subheader("Statistika Deskriptif")
    st.write(df.describe())