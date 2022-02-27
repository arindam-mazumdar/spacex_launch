import plotly.express as px
import pandas as pd

spacex_df =  pd.read_csv('spacex_launch_geo.csv', 
                            encoding = "ISO-8859-1"
                            )


fig1 = px.pie(spacex_df, values='class', 
        names='Launch Site', 
        title='Total success launches by site')
        
data2 = spacex_df[spacex_df['Launch Site']== 'VAFB SLC-4E']
fig2 = px.pie(data2, values='class', names= 'class',
        title = 'Success rate')
        
entered_site =  'KSC LC-39A'

filtered_df = spacex_df.groupby('Launch Site')['class'].mean().reset_index()
data2 = filtered_df[filtered_df['Launch Site']== entered_site]
data3 = pd.DataFrame({'Suc':[1,0],'class':[data2.loc[0,'class'], 1-data2.loc[0,'class']]})
fig4 = px.pie(data3, values='class', names= 'Suc',
title = 'Total Success rate of site:'+ entered_site) 

max_payload = 7000
min_payload = 2000
fill_df = spacex_df[(spacex_df['Payload Mass (kg)'] <= max_payload) & (spacex_df['Payload Mass (kg)'] >= min_payload)]
version_cat =[list(fill_df['Booster Version'])[i].split(' ')[1] for i in range(len(fill_df))]
fill_df['Booster Version Category'] = version_cat

fig3 = px.scatter(fill_df, x='Payload Mass (kg)', y = 'class', color='Booster Version Category') 
        
fig4.show()
