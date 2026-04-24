import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    df = pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
    return df

# Filter data berdasarkan tahun 
def filter_data(df, year=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun🗓️",
        options=[None, 2020, 2021, 2022],
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )

def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    df_selected = df[selected_columns]
    st.subheader("Data COVID-19 Indonesia 🔴⚪")
    st.dataframe(df_selected.head(10))
    
# Total Kasus
def total_case(df):
    total_kasus= df['Total Cases'].sum()
    return total_kasus

#Total Death
def total_death(df):
    total_kematian = df['Total Deaths'].sum()
    return total_kematian

#Total Sembuh
def total_recovery(df):
    total_sembuh = df['Total Recovered'].sum()
    return total_sembuh

#Tampilkan scoreboard/metrik dalam 3 kolom
def kolom(df):
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Kasus📈",value=f"{kasus/1000:.1f}K", border=True )
    col2.metric("Total Kematian💀",value=f"{kematian/1000:.1f}K", border=True )
    col3.metric("Total Sembuh🏋️‍♂️",value=f"{sembuh/1000:.1f}K", border=True )

#piechart1
def pie_chart1(df):
    #pemanggilan data
    total_mati = total_death(df)
    total_sembuh = total_recovery(df)

    #dataframe
    data = {
        'Status': ['Meninggal', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }

    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=["#e9746c", "#4dbfe8"]
    )

    st.plotly_chart(fig, use_container_width=True)