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
tdor_data = pre_data.drop(["Photo","Photo source","Thumbnail","Tweet","Permalink","QR code"], axis=1)
tdor_data.to_csv('tdor_data.csv')
