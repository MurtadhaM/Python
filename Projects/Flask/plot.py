# Author: Murtadha Marzouq
# Date: 2020-11-24
# Group: 15 
# Assignment: Final Project
# 
# 
# DATA SET INFORMATION:
# https://data.humdata.org/dataset/covid-19-global-travel-restrictions-and-airline-information
# https://databank.worldbank.org/source/2?series=ST.INT.RCPT.XP.ZS&country=&savedlg=1&l=en
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('static/Travel_Restrictions.csv')
fig = go.Figure(go.Scatter(x = df['adm0_name'], y = df['adm0_name'],
                  name='Travel Restrictions'))



# Table Data Restrictions
fig2 = go.Figure(data=[go.Table(
    header=dict(values=[['Country'], ['Effective Data'] ],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.adm0_name, df.published],
               fill_color='lavender',
               align='left'))
])



# Table Airline Restrictions
fig.update_layout(title='Travel Restrictions (2021)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)


fig2.update_layout(title='Travel Restrictions (2021)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)


print(fig.write_html('static/plot.html'))


print(fig2.write_html('static/table.html'))
