import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
paths = "/Users/camille/repo/projet_perso/queer_project/tdor_data.csv"
tdor_data = pd.read_csv(paths)
tdor_data1 = pd.read_csv(paths)
st.set_page_config(layout = "wide")
st.markdown("# TDoR")

def Main_page():
    st.markdown("The dead of transphobia")
    #st.sidebar.markdown("# Over years")

def page_2():
    st.markdown("Where are trans people most killed or pushed to suicide? ")
    #st.sidebar.markdown("# Ranking❄️")

def page3():
    st.markdown("#Ages")
    #st.sidebar.markdown("#Ages")

page_names_to_funcs = {
    "Main Page": Main_page,
    "1_Global_picture ": page_2,
    "2_Where": page3,
}

st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque ligula vitae sapien auctor feugiat. Curabitur sollicitudin sem ac nisi ornare, scelerisque facilisis ex pellentesque. Proin dictum venenatis malesuada. Aenean venenatis maximus tempus. Morbi turpis tellus, dapibus vel velit ultricies, mollis pulvinar urna. Sed venenatis consequat odio, at finibus lectus cursus ac. In commodo dolor auctor dolor aliquam, in elementum augue laoreet. Cras at condimentum libero. Sed quis massa mauris.')
st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque ligula vitae sapien auctor feugiat. Curabitur sollicitudin sem ac nisi ornare, scelerisque facilisis ex pellentesque. Proin dictum venenatis malesuada. Aenean venenatis maximus tempus. Morbi turpis tellus, dapibus vel velit ultricies, mollis pulvinar urna. Sed venenatis consequat odio, at finibus lectus cursus ac. In commodo dolor auctor dolor aliquam, in elementum augue laoreet. Cras at condimentum libero. Sed quis massa mauris.')
st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque ligula vitae sapien auctor feugiat. Curabitur sollicitudin sem ac nisi ornare, scelerisque facilisis ex pellentesque. Proin dictum venenatis malesuada. Aenean venenatis maximus tempus. Morbi turpis tellus, dapibus vel velit ultricies, mollis pulvinar urna. Sed venenatis consequat odio, at finibus lectus cursus ac. In commodo dolor auctor dolor aliquam, in elementum augue laoreet. Cras at condimentum libero. Sed quis massa mauris.')
st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque ligula vitae sapien auctor feugiat. Curabitur sollicitudin sem ac nisi ornare, scelerisque facilisis ex pellentesque. Proin dictum venenatis malesuada. Aenean venenatis maximus tempus. Morbi turpis tellus, dapibus vel velit ultricies, mollis pulvinar urna. Sed venenatis consequat odio, at finibus lectus cursus ac. In commodo dolor auctor dolor aliquam, in elementum augue laoreet. Cras at condimentum libero. Sed quis massa mauris.')
st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam scelerisque ligula vitae sapien auctor feugiat. Curabitur sollicitudin sem ac nisi ornare, scelerisque facilisis ex pellentesque. Proin dictum venenatis malesuada. Aenean venenatis maximus tempus. Morbi turpis tellus, dapibus vel velit ultricies, mollis pulvinar urna. Sed venenatis consequat odio, at finibus lectus cursus ac. In commodo dolor auctor dolor aliquam, in elementum augue laoreet. Cras at condimentum libero. Sed quis massa mauris.')
