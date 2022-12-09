import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
pre_data = pd.read_csv('/Users/camille/repo/projet_perso/queer_project/Dataset/tdor_export.csv')
pre_data["Date"] = pd.to_datetime(pre_data["Date"])
pre_data["year"] = pre_data["Date"].dt.year
pre_data["nb_victims_year"] = pre_data.groupby('year').year.transform("count")
pre_data["nb_victims_age"] = pre_data.groupby('Age').year.transform("count")
pre_data["nb_victims_country"] = pre_data.groupby('Country').Country.transform("count")
pre_data["nb_victims_country_year"] = pre_data.groupby(['Country', 'year']).year.transform("count")
pre_data["nb_victims_Category_year"] = pre_data.groupby(['Category', 'year']).year.transform("count")
#pre_data["nb_victims_Category_year"] = pre_data.groupby(['Category', 'year']).year.transform("count") = suicide 
pre_data["Birthdate"] = pd.to_datetime(pre_data["Birthdate"])
pre_data["year_birthdays"] = pre_data["Birthdate"].dt.year.astype('Int64')
pre_data["age"] = pre_data["year"] - pre_data["year_birthdays"] 
tdor_data = pre_data.drop(["Age", "Photo","Photo source","Thumbnail","Tweet","Permalink","QR code","Description", "TDoR list ref"], axis=1)

fig = px.line(tdor_data, x="year", y="nb_victims_year",
                     labels={
                     "nb_victims_year": "Number of victims yearly",
                     "year": "Year"
                 })
fig.update_traces(mode="markers+lines")
fig.update_layout(hovermode="x unified")
fig.update_layout(title_text='Number of deceased trans persons by category and year', title_x=0.5, title_font_size=20)
fig.show()
tdor_data['percentage_category'] = ((tdor_data["nb_victims_Category_year"] / 
                      tdor_data["nb_victims_year"]) * 100).round(1)

tdor_data['percentage_category'] = ((tdor_data["nb_victims_Category_year"] / 
                      tdor_data["nb_victims_year"]) * 100).round(1)

fig2 = px.line(tdor_data, x="year", y="nb_victims_Category_year", color='Category',text=tdor_data['percentage_category'].apply(lambda x: '{0:1.1f}%'.format(x)),
                     labels={
                     "nb_victims_Category_year": "Number of victims yearly by category",
                     "year": "Year",
                     "Category": "Category of death",
                 })
fig2.update_traces(mode="markers+lines", hovertemplate=None)
fig2.update_layout(hovermode="x unified")
fig2.update_layout(title_text='Number of deceased trans persons by category and year', title_x=0.5, title_font_size=20)
fig2.show()