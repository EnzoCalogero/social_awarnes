import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html

from app import app

dataset = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")
country_df = pd.read_csv("C:/gits_folders/social_awarnes/data/wikipedia-iso-country-codes.csv")
country_df.columns = ["Country", "A2C", "A3C", "Num", "ISO"]
country_df.columns = ["Country", "A2C", "A3C", "Num", "ISO"]
datac_df = dataset.merge(country_df)

df = datac_df.groupby(["Country", "A3C"])["Value"].agg(["median", "max", "min", "mean"]).reset_index()
config = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['zoom2d', 'hoverCompareCartesian', 'hoverClosestCartesian', 'toggleSpikelines']
}

fig = go.Figure(data=go.Choropleth(
    locations=df['A3C'],
    z=df['max'],
    text=df['Country'],
    colorscale='Rainbow',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
),
)
fig.update_layout(
#    title_text=" ",
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
)
fig.update_layout(
    title={
        'text': "World Map Female Violence",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.H4('Violence Against Women and Girls'),
            width={"size": 6, "offset": 3},
        )),

    dbc.Row(
        dbc.Col(
            html.P("This dataset aggregates agreement with key questions across gender,"
                   "education level and many other socioeconomic variables from 70 different countries."
                   "The data was collected as part of the Demographic and Health Surveys (DHS) program,"
                   " which exists to advance the global understanding of health and population trends "
                   "in developing countries."),
            width={"size": 6, "offset": 3},
        )),

    dbc.Row(
        dbc.Col(
            html.P("We will analyze the data on violence on women and girls. "
                   "The data is collected from 70 countries"
                   " and contains demographics questions"
                   " and answers as well as percent of response to 5 violence specific questions."),
            width={"size": 6, "offset": 3},
        )),

    dbc.Row(
        dbc.Col(
            dcc.Graph(
                id='example-graph',
                figure=fig,
                config=config,

            ),
            width={"size": 6, "offset": 3},
        )),

    dbc.Row(
        dbc.Col(
            html.P(dcc.Link('Next Page', href='/First')),
            width={"size": 6, "offset": 3},
        )),

], style={
    'padding': '0px 10px 15px 10px',
    'marginLeft': 'auto',
    'marginRight': 'auto',
    'width': "150vh",
    'display': 'inline-block',
    'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
},
)

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
