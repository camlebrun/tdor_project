import streamlit as st
st.title('TDOR')
def main_page():
    st.markdown("#Over years")
    st.sidebar.markdown("# Over years")

def page2():
    st.markdown("Ranking")
    st.sidebar.markdown("# Ranking❄️")

def page3():
    st.markdown("#Ages")
    st.sidebar.markdown("#Ages")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def plot():

    df = pd.DataFrame(px.data.gapminder())

    clist = df["country"].unique().tolist()

    countries = st.multiselect("Select country", clist)
    st.header("You selected: {}".format(", ".join(countries)))

    dfs = {country: df[df["country"] == country] for country in countries}

    fig = go.Figure()
    for country, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["year"], y=df["gdpPercap"], name=country))

    st.plotly_chart(fig)


plot()