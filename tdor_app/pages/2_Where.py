import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go

#st.set_page_config(layout="wide")
paths = "/Users/camille/repo/projet_perso/queer_project/tdor_data.csv"
tdor_data = pd.read_csv(paths)
#df = pd.read_csv("/Users/camille/repo/projet_perso/queer_project/notebook/untrack/mergeon.csv")
df_filter = pd.read_csv('/Users/camille/repo/projet_perso/queer_project/notebook/untrack/df_filter.csv')


tab1, tab2 = st.tabs(["Annual report", "Number of deaths by categories"])

with tab1:
    st.markdown("# Where are trans people killed or pushed to suicide ?")

    df_map = pd.read_csv('/Users/camille/repo/projet_perso/queer_project/notebook/untrack/map_country.csv')

    fig = px.choropleth(df_map, locations= "Country", color='nb_victims_country', locationmode='country names',
                            color_continuous_scale="dense",
                            labels={
                            "nb_victims_country": " Number of deaths"
                    })
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(width=1000,
                            height=500)
    st.plotly_chart(fig)

with tab2 :
        fig2 = px.line(df_filter, x="Year", y="ratio", color='Country')
        fig2.update_layout(width=1000,
                        height=500)
        fig2.update_traces(mode="markers+lines", hovertemplate=None)
        fig2.update_layout(hovermode="x unified")
        fig2.update_traces(mode='markers+lines')    
        st.plotly_chart(fig2)


