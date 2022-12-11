import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
paths = "/Users/camille/repo/projet_perso/queer_project/tdor_data.csv"
tdor_data = pd.read_csv(paths)
st.markdown("# The dead of transphobia")



tab1, tab2, tab3 = st.tabs(["Annual report", "Number of deaths by categories", "% Categories"])


with tab1:
        fig_annual = px.line(tdor_data, x="year", y="nb_victims_year",
                            labels={
                            "nb_victims_year": "Number of victims yearly",
                            "year": "Years"
                        })
        fig_annual.update_traces(mode="markers+lines")
        fig_annual.update_layout(hovermode="x unified")
        fig_annual.update_traces(line_color='#040801')
        fig_annual.update_traces(hovertemplate="<br>".join(["Number of victims yearly: %{y}",]))
        fig_annual.update_layout(width=1000,height=500)
        fig_annual.update_traces(line_color='#147852')
        fig_annual.update_layout(title_text=' Number of deaths per year', title_x=0.5, title_font_size=20)
        st.plotly_chart(fig_annual, use_container_width = True)
        st.write('Hello, *World!* :sunglasses:')


with tab2:
   st.title("Number of deaths by categories per year")
   selected_cat = st.multiselect('Show category', tdor_data.Category.unique().tolist())
   df_cat = tdor_data[tdor_data['Category'].isin(selected_cat)]
   fig_categorie_y = px.line(df_cat, x="year", y="nb_victims_Category_year",
                        color='Category',
                        text=df_cat['percentage_category'].apply(lambda x: '{0:1.1f}%'.format(x)),
                        labels={
                        "nb_victims_Category_year": " Number of deaths",
                        "year": "Years",
                        "Category": "Category of deaths"
                })
   fig_categorie_y.update_layout(width=1000,
                        height=500)

   fig_categorie_y.add_scatter(x=tdor_data['year'], 
                y=tdor_data['nb_victims_year'], 
                name = "Total", 
                line=dict(color="#040801"))

   fig_categorie_y.update_traces(mode="markers+lines", hovertemplate=None)
   fig_categorie_y.update_layout(hovermode="x unified")
   fig_categorie_y.update_layout(title_x=0.5, title_font_size=20)
   st.plotly_chart(fig_categorie_y, use_container_width = True)
   st.write('Hello, *World!* :sunglasses:')

with tab3:
   st.title("Distribution of deaths by categories")
   test=tdor_data.sort_values(['nb_victims_Category'],ascending=False).groupby('Category').head(3).drop_duplicates('Category', keep='last')
   ab = px.bar(test, x="nb_victims_Category", y="Category",
                            color='Category',
                            text=test['percentage_category_all'].apply(lambda x: '{0:1.1f}%'.format(x)), 
                        labels={
                        "nb_victims_Category": " Number deaths",
                        "year": "Year",
                        "text": "Percentage",
                })
   ab.update_layout(width=1000, height=500)
   ab.update_layout(title_x=0.5, title_font_size=20)
                
   st.plotly_chart(ab, use_container_width = True)
   st.write('Hello, *World!* :sunglasses:')

