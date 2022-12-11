import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
paths = "/Users/camille/repo/projet_perso/queer_project/notebook/track/tdor_data.csv"
tdor_data = pd.read_csv(paths)
st.set_page_config(layout = "wide")
st.markdown("# TDoR")
st.sidebar.markdown("# Over years")
def main_page():
    st.markdown("Over years")
    #st.sidebar.markdown("# Over years")

def page_2():
    st.markdown("Ranking")
    #st.sidebar.markdown("# Ranking❄️")

def page3():
    st.markdown("#Ages")
    #st.sidebar.markdown("#Ages")

page_names_to_funcs = {
    "Main Page": main_page,
    "My test": page_2,
    "Page 3": page3,
}
tab1, tab2, tab3 = st.tabs(["Categorie", "Dog", "Owl"])

with tab1:
   #st.header("A cat")
   st.title("Déces par catégories et par année (total inclus)")

selected_cat = st.multiselect('Show category', tdor_data.Category.unique().tolist())
df_cat = tdor_data[tdor_data['Category'].isin(selected_cat)]


fig_categorie_y = px.line(df_cat, x="year", y="nb_victims_Category_year",
                        color='Category',
                        text=df_cat['percentage_category'].apply(lambda x: '{0:1.1f}%'.format(x)),
                        labels={
                        "nb_victims_Category_year": "Number of victims yearly by category",
                        "year": "Year",
                        "Category": "Category of death",
                })

fig_categorie_y.update_layout(width=1000,
                        height=900)

fig_categorie_y.add_scatter(x=tdor_data['year'], 
                y=tdor_data['nb_victims_year'], 
                name = "Total", 
                line=dict(color="#040801"))

fig_categorie_y.update_traces(mode="markers+lines", hovertemplate=None)
fig_categorie_y.update_layout(hovermode="x unified")
fig_categorie_y.update_layout(title_x=0.5, title_font_size=20)

st.plotly_chart(fig_categorie_y)


with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()
