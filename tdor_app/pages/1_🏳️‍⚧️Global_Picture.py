import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
import os 
st.set_page_config(layout="wide", page_title="TDoR")

fig_annual, fig_categorie_y = st.columns((2,4))

st.markdown("<h1 style='text-align: center'>The dead of transphobia</h1>", unsafe_allow_html=True)
tdor_data = pd.read_csv("Data/tdor_data_all.csv")

with st.container():
    col1, col2, col3 = st.columns((100,500,100))
    with col2:
        fig_annual = px.line(tdor_data, x="year", y="nb_victims_year",
                            labels={
                            "nb_victims_year": "Number of victims yearly",
                            "year": "Years"
                        })
        fig_annual.update_traces(mode="markers+lines")
        fig_annual.update_layout(hovermode="x unified")
        fig_annual.update_layout(hoverlabel=dict(font_size=14)
)

        fig_annual.update_traces(line_color='#040801')
        fig_annual.update_traces(hovertemplate="%{y}")
        fig_annual.update_layout(width=1100,height=500)
        fig_annual.update_traces(textposition='top center')
        fig_annual.update_traces(line_color='#147852')
        st.markdown("<h2 style='text-align: center'>Number of deaths per year</h2>", unsafe_allow_html=True)
        st.write ("According to scientific literature, the transgender population is 2% around the globe with no difference between countries. o take into consideration the difference in population between countries, a ratio per 100K inhabitants has been made ")

        st.plotly_chart(fig_annual, use_container_width = True)
with st.container():
    col1, col2 = st.columns(2, gap="large")
    with col2:
        st.markdown("<h2 style='text-align: center'>Number of deaths by categories per year</h2>", unsafe_allow_html=True)
        selected_cat = st.multiselect('Show category', tdor_data.Category.unique().tolist(),['Violence', 'Suicide'])
        df_cat = tdor_data[tdor_data['Category'].isin(selected_cat)]
        fig_categorie_y = px.line(df_cat, x="year", y="nb_victims_Category_year",
                                color='Category',
                                text=df_cat['percentage_category'].apply(lambda x: '{0:1.1f}%'.format(x)),
                                labels={
                                "nb_victims_Category_year": " Number of deaths",
                                "year": "Years"  })
        fig_categorie_y.update_layout(width=1000,
                                height=500)



        fig_categorie_y.update_traces(mode="markers+lines", hovertemplate=None)
        fig_categorie_y.update_layout(hovermode="x unified")
        fig_categorie_y.update_layout(showlegend=False)
        st.plotly_chart(fig_categorie_y,  use_container_width = True)


with col1:
        st.markdown("<h2 style='text-align: center'>Distribution of deaths by categories</h2>", unsafe_allow_html=True)
        test=tdor_data.sort_values(['nb_victims_Category'],ascending=False).groupby('Category').head(3).drop_duplicates('Category', keep='last')
        ab = px.bar(test, x="nb_victims_Category", y="Category",
                                color='Category', 
                                text=(test['percentage_category'].sort_values(ascending=False)).apply(lambda x: '{0:1.1f}%'.format(x)), 
                                labels={
                     "nb_victims_Category": "Percentage of deaths per category"} )
        ab.update_layout(showlegend=False)
        ab.update_layout(hoverlabel=dict(font_size=14))
        ab.update_layout(width=1000, height=500)
        ab.update_traces(hoverinfo='skip', hovertemplate=None)

        st.plotly_chart(ab, use_container_width = True, config=dict({'staticPlot':True}))


