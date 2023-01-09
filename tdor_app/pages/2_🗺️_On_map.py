import streamlit as st
import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objs as go
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json') as response:
    countries = json.load(response)

st.set_page_config(layout = "wide", page_title="On Map")


fig_general, fig_suicide = st.columns((2,4))
st.markdown("<h1 style='text-align: center'>Where are trans people killed or pushed to suicide ?</h1>", unsafe_allow_html=True)


st.write ("According to scientific literature, the transgender population is 2% around the globe with no difference between countries. o take into consideration the difference in population between countries, a ratio per 100K inhabitants has been made ")

with st.container():
    col1, col2, col3 = st.columns((25,50,25))
    with col2:
            df_general = pd.read_csv('Data/tdor_data_all.csv', 
                   dtype={"counties": str})
import json
world_path = 'Data/custom.geo.json'
with open(world_path) as f:
    geo_world = json.load(f)


found = []
missing = []
countries_geo = []

tmp = df_general.set_index('Country')

for country in geo_world['features']:
    
    country_name = country['properties']['name'] 
    
    if country_name in tmp.index:
        
        found.append(country_name)
        
        geometry = country['geometry']
        
        countries_geo.append({
            'type': 'Feature',
            'geometry': geometry,
            'id':country_name
        })
geo_world_ok = {'type': 'FeatureCollection', 'features': countries_geo}
df_general = pd.read_csv('Data/tdor_data_all.csv')
df_general['ratio'] = df_general['ratio'].astype(float)
df_general = df_general.loc[df_general['ratio']!= 0]
year_option = df_general['year'].unique().tolist()
st.info('Select years (for following graphs)')
year = st.select_slider('',year_option)
df_general = df_general[df_general['year'] == year]
st.write (" This maps represent trans peoples killed  or pushed to suicide in  " , year)
fig_general = px.choropleth_mapbox(df_general, geojson=geo_world_ok, locations='Country', color='ratio',
color_continuous_scale="reds", range_color=(0, 0.1),  opacity=0.5, 
                           mapbox_style="carto-darkmatter", zoom = 0.9,  center = {"lat": 30, "lon": -1})
fig_general.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig_general.update_layout(width=1100,
height=500)
st.plotly_chart(fig_general,  use_container_width=True)


with st.container():
    col1, col2 = st.columns(2, gap="large")
    with col2:
        st.markdown("<h4 style='text-align: center'>Suicides</h4>", unsafe_allow_html=True)
        df_suicide = pd.read_csv('Data/tdor_suicide.csv')
        df_suicide['ratio'] = df_suicide['ratio'].astype(float)
        df_suicide = df_suicide.loc[df_suicide['ratio']!= 0]
        df_suicide = df_suicide[df_suicide['year'] == year]
        st.write (" This maps represent trans peoples pushed to suicide in  " , year)
        fig_suicide = px.choropleth_mapbox(df_suicide, geojson=geo_world_ok, locations='Country', color='ratio',
        range_color=(0, 0.07),
        color_continuous_scale="reds", opacity=0.5,  
        mapbox_style="carto-darkmatter", zoom = 0,
        center = {"lat": 30, "lon": -1})
        fig_suicide.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_suicide, use_container_width= True)


with col1:
            st.markdown("<h4 style='text-align: center'>Violences</h4>", unsafe_allow_html=True)
            df_violence = pd.read_csv('Data/tdor_Violence.csv')
            df_violence['ratio'] = df_violence['ratio'].astype(float)
            df_violence['ratio'].where(df_violence['ratio'] >= 0.0009 ,0, inplace=True)
            df_violence = df_violence[df_violence['year'] == year]
            st.write (" This maps represent trans peoples killed  in  " , year)
            fig_violence = px.choropleth_mapbox(df_violence, geojson=geo_world_ok, locations='Country', color='ratio',
            color_continuous_scale="reds", opacity=0.5, range_color=(0, 0.01),
            mapbox_style="carto-darkmatter", zoom = 0,
            center = {"lat": 30, "lon": -1})
            fig_violence.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig_violence, use_container_width= True)

with st.expander("More info"):
            st.write("""
            Transgender people suffer other types of violence (medical, prison, etc.). In addition, unfortunately, information is missing for many people.  In another tab we will also look at the demography of these peoples """)
