import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
paths = "/Users/camille/repo/projet_perso/queer_project/tdor_data.csv"
tdor_data = pd.read_csv(paths)
st.markdown("# How are trans people killed or pushed to suicide ?")


top3=tdor_data.sort_values(['nb_victims_country'],ascending=False).groupby('Country_Code').head(3).drop_duplicates('Country_Code', keep='last').iloc[:3]
fig_top3 = px.histogram(top3, x="nb_victims_country", y  = "Country", color = "Country", text_auto=True )# table 

st.plotly_chart(fig_top3)
st.write('Hello, *World!* :sunglasses:')