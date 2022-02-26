# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update


app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the automobiles data into pandas dataframe
spacex_df =  pd.read_csv('spacex_launch_geo.csv', 
                            encoding = "ISO-8859-1"
                            )

#Layout Section of Dash

app.layout = html.Div(children=[#TASK 3A
    html.H1('SpaceX Launch Record Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 24}),
     #outer division starts
     html.Div([
                   # First inner divsion for  adding dropdown helper text for Selected Drive wheels
#                    html.Div(
#                            html.H2('Drive Wheels Type:', style={'margin-right': '2em'})#TASK 3B
#                            ,
#                     ),
                     


                    dcc.Dropdown(
                            id='site-dropdown',
                        options=[
                               {'label':'All Sites', 'value': 'ALL'},
                             {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                             {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                             {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL'
        ),#TASK 3C
                
        
#        dcc.Graph

#                    Second Inner division for adding 2 inner divisions for 2 output graphs 
                    html.Div([

                        html.Div(id='plot1')
                        #TASK 3D

                    ], style={'display': 'flex'}),
                    
      # Range SLider 
      dcc.RangeSlider(id='payload_range',
                min=0, max=10000, step=1000,
                marks={0: '0',
                       10000: '10k'},
                value=[1000, 5000]),

       # Scatter plot of sucess with different versions of booster 
                    html.Div(id='plot2')


    ])
    #outer division ends

])
#layout ends

#Place to add @app.callback Decorator
#TASK 3E
@app.callback([Output(component_id='plot1', component_property='children'), 
               Output(component_id='plot2', component_property='children')],
               Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload_range', component_property='value'))
#@app.callback(Output(component_id='plot2', component_property='children'),
#              Input(component_id='payload_range', component_property='value'))

#Place to define the callback function .
#TASK 3F

#def display_selected_drive_charts(value):
#    filtered_df = spacex_df.groupby('Launch Site')['class'].mean().reset_index()
#    if entered_site == 'ALL':
#        fig1 = px.pie(spacex_df, values='class', 
#        names='Launch Site', 
#        title='Total success launches by site')
#    else:
#        data2 = spacex_df[spacex_df['Launch Site']== entered_site]
#        fig1 = px.pie(data2, values='class', names= 'class',
#        title = 'Success rate')


def get_pie_chart(entered_site, range_payload):
    filtered_df = spacex_df.groupby('Launch Site')['class'].mean().reset_index()
    if entered_site == 'ALL':
        fig1 = px.pie(spacex_df, values='class', 
        names='Launch Site', 
        title='Total success launches by site')
    else:
        data2 = filtered_df[filtered_df['Launch Site']== entered_site]
        data3 = pd.DataFrame({'Suc':[1,0],'class':[data2.loc[0,'class'], 1-data2.loc[0,'class']]})
        fig1 = px.pie(data3, values='class', names= 'Suc',
        title = 'Total Success rate of site:'+ entered_site) 
        # return the outcomes piechart for a selected site
    max_payload = range_payload[1]
    min_payload = range_payload[0]
    fill_df = spacex_df[(spacex_df['Payload Mass (kg)'] <= max_payload) & (spacex_df['Payload Mass (kg)'] >= min_payload)]
    version_cat =[list(fill_df['Booster Version'])[i].split(' ')[1] for i in range(len(fill_df))]
    fill_df['Booster Version Category'] = version_cat
    fig3 = px.scatter(fill_df, x='Payload Mass (kg)', y = 'class', color='Booster Version Category') 
    
    return [dcc.Graph(figure=fig1), dcc.Graph(figure=fig3)]

#def get_scatter_chart(range_payload):


#def update_output(value):
#    max_payload = value[1]
#    min_payload = value[0] 
#    return 'You have selected "{}"'.format(max_payload)


if __name__ == '__main__':
    app.run_server()

# Read the airline data into pandas dataframe
#spacex_df =  pd.read_csv('spacex_launch_geo.csv', 
#                            encoding = "ISO-8859-1")
## Create a dash application
#app = dash.Dash(__name__)

## REVIEW1: Clear the layout and do not display exception till callback gets executed
#app.config.suppress_callback_exceptions = True

#                               
#app.layout = html.Div(children=[#TASK 3A
#    html.H1('SpaceX Launch Records Dashboard', 
#                                style={'textAlign': 'center', 'color': '#503D36',
#                                'font-size': 24}),
#     #outer division starts
##     html.Div([
##                   # First inner divsion for  adding dropdown helper text for Selected Drive wheels
##                    html.Div(
##                            html.H2('Drive Wheels Type:', style={'margin-right': '2em'})#TASK 3B
##                            ,
##                     ),
#                     
## 'CCAFS LC-40', 'VAFB SLC-4E', 'KSC LC-39A', 'CCAFS SLC-40'

#                    dcc.Dropdown(
#                            id='site-dropdown',
#                        options=[
#                               {'label':'All Sites', 'value': 'ALL'},
#                             {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
#                            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
#                             {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'}
#        ],
#        value='ALL'
#        ),#TASK 3C

#                    #Second Inner division for adding 2 inner divisions for 2 output graphs 
#                    html.Div(
#                        html.Div([ ], id='success-pie-chart')
#                        #TASK 3D

#                    , style={'display': 'flex'}),


#    ])
#    #outer division ends

##])
##layout ends

##Place to add @app.callback Decorator
##TASK 3E
##@app.callback([Output(component_id='plot1', component_property='children'),
##               Output(component_id='plot2', component_property='children')],
##               Input(component_id='demo-dropdown', component_property='value'))


##Place to define the callback function .
##TASK 3F
#@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
#              Input(component_id='site-dropdown', component_property='value'))

#def get_pie_chart(entered_site):
#    filtered_df = spacex_df.groupby('Launch Site')['class'].mean().reset_index()
#    if entered_site == 'ALL':
#        fig = px.pie(spacex_df, values='class', 
#        names='Launch Site', 
#        title='Total success launches by site')
#    else:
#        data2 = spacex_df[spacex_df['Launch Site']== entered_site]
#        fig = px.pie(data2, value='class', names= 'class',
#        title = 'Success rate') 
#        # return the outcomes piechart for a selected site
#    return fig

#if __name__ == '__main__':
#    app.run_server()

