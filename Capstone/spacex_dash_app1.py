from distutils.log import debug
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import wget


# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                dcc.Dropdown(id='Site-down',
                                    options=[
                     {'label': 'All Sites', 'value': "ALL"},
                    {'label': 'CCAFS LC-40', 'value': "CCAFS LC-40"},
                    {'label': 'CCAFS SLC-40', 'value': "CCAFS SLC-40"},
                    {'label': 'KSC LC-39A', 'value': "KSC LC-39A"},
                    {'label': 'VAFB SLC-4E', 'value': "VAFB SLC-4E"},
                                    ],
                              value='ALL',
                placeholder="Select a Launch Site here",
                searchable=True),
                            html.Br(),
                            
                            html.Div(dcc.Graph(id='success-pie-chart')),
                            html.Br(),
                                
                            html.P("Payload range (Kg):"),
                            dcc.RangeSlider(id='Payload-slider',
                                min=0, max=10000, step= 1000,
                                marks={0 : '0', 2000: '2000',
                                       4000 :'4000', 6000:'6000', 8000:'8000'
                                       ,10000: '10000'},
                                value=[min_payload, max_payload]),
                            
                            html.Div(dcc.Graph(id='success-payload-scatter-chart')),    
                                
                                
                                ])


@app.callback(Output(component_id='success-pie-chart',component_property='figure'),
              Input(component_id='Site-down', component_property='value'))

def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class',
                         names='Launch Site',
                         title='Percentage of total successful Launches for all sites.')
        return fig
    else:
         # return the outcomes piechart for a selected site
        df=filtered_df[filtered_df['Launch Site']== entered_site]
        dfs= df.groupby(['Launch Site','class']).size().reset_index(name= 'class count')
        fig = px.pie(dfs, values='class count', 
        names='class', 
        title='Success vrs Failure')
        return fig


@app.callback( Output(component_id='success-payload-scatter-chart', component_property='figure'),
               [Input(component_id='Payload-slider', component_property='value'),
                Input(component_id='Site-down', component_property='value')])

def get_scatter_chart(inputt,entered_site):
    
    new_df= spacex_df[(spacex_df['Payload Mass (kg)']>=inputt[0])&(spacex_df['Payload Mass (kg)']<=inputt[1])] 
    
    if entered_site == 'ALL':
        fig= px.scatter(new_df, x='Payload Mass (kg)', y='class',hover_data=['Booster Version'],color='Booster Version Category',
                        title='Correlation between Payloads and Success Launches')

        return fig
    else:
        new_dff = new_df[new_df['Launch Site']== entered_site]
        fig = px.scatter(new_dff, x='Payload Mass (kg)',y='class', hover_data=['Booster Version'], color='Booster Version Category',
                         title=entered_site + ' correlation between Payloads and Success.')
        return fig
    
    
if __name__ == '__main__':
    app.run_server()