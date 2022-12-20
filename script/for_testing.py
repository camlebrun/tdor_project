import numpy as np 
import pandas as pd
import datetime
import plotly.express as px
"""" Download the dataset from hhttps://tdor.translivesmatter.info/reports?view=map%5D and save it in the Dataset folder
"""
#raw_data = '../Dataset/tdor_export.csv'
#pre_data = pd.read_csv('raw_data')
##pre_data["Date"] = pd.to_datetime(pre_data["Date"])
#pre_data["year"] = pre_data["Date"].dt.year
#pre_data["nb_victims_year"] = pre_data.groupby('year').year.transform("count")
#pre_data["nb_victims_country"] = pre_data.groupby('Country').Country.transform("count")
#pre_data["nb_victims_country_year"] = pre_data.groupby(['Country', 'year']).year.transform("count")
#pre_data["nb_victims_Category_year"] = pre_data.groupby(['Category', 'year']).year.transform("count")
#pre_data["nb_victims_cause_year"] = pre_data.groupby(['Cause of death', 'year']).year.transform("count"
#pre_data["Birthdate"] = pd.to_datetime(pre_data["Birthdate"])
#pre_data["year_birthdays"] = pre_data["Birthdate"].dt.year.astype('Int64')
#pre_data["age"] = pre_data["year"] - pre_data["year_birthdays"] 
#tdor_data = pre_data.drop(["Age", "Photo","Photo source","Thumbnail","Tweet","Permalink","QR code","Description", "TDoR list ref"], axis=1)
#tdor_data["Category"]= tdor_data.Category.str.capitalize()
#tdor_data.rename(columns = {'Cause of death':'Cause_of_the_death'}, inplace = True)
#tdor_data.rename(columns = {'Country Code':'Country_Code'}, inplace = True)
#tdor_data['Country_Code'] = tdor_data.Country_Code.str.capitalize()
#tdor_data["Cause_of_the_death"] = tdor_data.Cause_of_the_death.str.capitalize()
#tdor_data.to_csv('tdor_data.csv')
#tdor_data['percentage_category'] = ((tdor_data["nb_victims_Category_year"] / 
                      #tdor_data["nb_victims_year"]) * 100).round(1)
#tdor_data.to_csv('tdor_data.csv')
paths = "/Users/camille/repo/projet_perso/queer_project/notebook/track/tdor_data.csv"
tdor_data = pd.read_csv(paths)
tdor_data["percentage_category_all"] = (tdor_data["nb_victims_Category"] /(tdor_data.nb_victims_Category.count()))*100
tdor_data.to_csv('tdor_data.csv')
#tdor_data["percentage_category"] = ((tdor_data["nb_victims_Category"] /tdor_data.nb_victims_Category.count()) * 100).round(2)
"""

NUMBER OF VICTIMS BY YEAR AND CATEGORY
+ TOTAL


fig2 = px.line(tdor_data, x="year", y="nb_victims_Category_year", color='Category',text=tdor_data['percentage_category'].apply(lambda x: '{0:1.1f}%'.format(x)),
                     labels={
                     "nb_victims_Category_year": "Number of victims yearly by category",
                     "year": "Year",
                     "Category": "Category of death",
                 })



fig2.add_scatter(x=tdor_data['year'], y=tdor_data['nb_victims_year'], name = "Total", line=dict(color="#040801"))

fig2.update_traces(mode="markers+lines", hovertemplate=None)
fig2.update_layout(hovermode="x unified")
fig2.update_layout(title_text='Amazing Graph', title_x=0.5, title_font_size=20)

fig2.show()

TOP 3 COUNTRIES

top3=tdor_data.sort_values(['nb_victims_country'],ascending=False).groupby('Country_Code').head(3).drop_duplicates('Country_Code', keep='last').iloc[:3]
fig3 = px.histogram(top3, x="nb_victims_country", y  = "Country", color = "Country", text_auto=True )# table 
fig3.show()



NUMBER OF VICTIMS BY YEAR AND  COUNTRY

import plotly.graph_objs as go


fig4 = px.line(tdor_data, x="year", y="nb_victims_country_year", color='Country',     width=000, height=1000,
                     labels={
                     "nb_victims_Category_year": "Number of victims yearly by category",
                     "year": "Year",
                     "Category": "Category of death"
                 })
fig4.update_traces(mode="markers+lines", hovertemplate=None)
fig4.update_layout(hovermode="x unified")

layout = go.Layout(
    autosize=False,
    width=100,
    height=3000
)
fig4.update_layout(title_text='Amazing Graph', title_x=0.5, title_font_size=20)
#,text=tdor_data['percentage_category'].apply(lambda x: '{0:1.1f}%'.format(x))
fig4.show()
"""