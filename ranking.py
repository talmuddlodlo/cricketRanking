import streamlit as st
import pandas as pd
from urllib.request import Request,urlopen

req = Request('https://sports.ndtv.com/cricket/icc-rankings', headers = {'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req)
data = pd.read_html(webpage, header=0)

st.title('Cricket Rankings, created by Talmud Msindazi for learning purposes')
st.markdown('We are webscrapping ICC Rankings from NDTV sport')

menu1 = ["Team", "Player"]
a = st.sidebar.selectbox("Select", menu1)

if a=="Team":
    menu2= ["T20", "ODI", "Test"]
    b = st.sidebar.selectbox("Format", menu2)
    if b=="Test":
        df = data[0]
        st.dataframe(df)

    if b=="ODI":
        df = data[4]
        st.dataframe(df)

    if b=="T20":
        df = data[8]
        st.dataframe(df)

if a=="Player":
    menu3= ["T20", "ODI", "Test"]
    b = st.sidebar.selectbox("Format", menu3)
    if b=="Test":
        menu4 = ["Batting", "Bowling", "All Rounder"]
        c = st.selectbox("Select", menu4)

        if c=="Batting":
            df = data[1]
            st.dataframe(df)

        if c=="Bowling":
            df = data[2]
            st.dataframe(df)

        if c=="All Rounder":
            df = data[3]
            st.dataframe(df)

    if b=="ODI":
        menu4 = ["Batting", "Bowling", "All Rounder"]
        c = st.selectbox("Select", menu4)

        if c=="Batting":
            df = data[5]
            st.dataframe(df)

        if c=="Bowling":
            df = data[6]
            st.dataframe(df)

        if c=="All Rounder":
            df = data[7]
            st.dataframe(df)

    if b=="T20":
        menu4 = ["Batting", "Bowling", "All Rounder"]
        c = st.selectbox("Select", menu4)

        if c=="Batting":
            df = data[9]
            st.dataframe(df)

        if c=="Bowling":
            df = data[10]
            st.dataframe(df)

        if c=="All Rounder":
            df = data[11]
            st.dataframe(df)