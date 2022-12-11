import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
paths = "/Users/camille/repo/projet_perso/queer_project/tdor_data.csv"
tdor_data = pd.read_csv(paths)
st.markdown("# How are trans people killed or pushed to suicide ?")


cat_per=tdor_data.sort_values(['nb_victims_Category'],ascending=False).groupby('Category').head(3).drop_duplicates('Category', keep='last')
cat_bar = px.bar(cat_per, x="nb_victims_Category", y="Category",
                            color='Category',
                            text=cat_per['percentage_category_all'].apply(lambda x: '{0:1.1f}%'.format(x)))

st.plotly_chart(cat_bar)