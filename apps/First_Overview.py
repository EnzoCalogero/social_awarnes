import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
from dash import html, dcc, Input, Output

from app import app

df = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")
df_1 = df[df["Question"] == "... for at least one specific reason"].copy()
df_1 = df_1.sort_values(by=['Value'], ascending=False)

country = df_1.sort_values(by=['Country'], ascending=True)
country = country['Country'].unique()
country = np.concatenate((country, ["All Countries"]))

config = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['zoom2d', 'hoverCompareCartesian', 'hoverClosestCartesian', 'toggleSpikelines']
}

layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.H4("Overview for each country expected violence man vs woman"),
            width={"size": 6, "offset": 3},
        )),
    dbc.Row(
        dbc.Col([
            html.P("Countries Selection:"),
            dcc.Dropdown(
                id='x-axis',
                options=country,
                value='All Countries',
                multi=True,
                clearable=False,
             )],
            width={"size": 6, "offset": 3},
        )),
    dbc.Row(
        dbc.Col([
    dcc.Graph(id="graph",
              config=config)
            ],  width={"size": 10, "offset": 1},
        )),

    dbc.Row(
        dbc.Col([
            html.P(dcc.Link('Next Page', href='/Second')),
            html.P(dcc.Link('Back Page', href='/'))
        ],
            width={"size": 6, "offset": 3},
        )),

], style={
    'padding': '0px 10px 15px 10px',
    'marginL,eft': 'auto',
    'marginRight': 'auto',
    'width': "150vh",
    'display': 'inline-block',
    'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
})


@app.callback(
    Output("graph", "figure"),
    Input("x-axis", "value"))
def generate_chart(x):
    fig = px.box(df_1,
                 x="Country",
                 y="Value",
                 color="Gender",
                 color_discrete_sequence=["pink", "blue"],
                 )
    fig.update_layout(
        title={
            'text': "For Each Country Man vs Woman Expectation",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(
        xaxis=dict(
            title='',
        )),
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(family='Rockwell',
                                   color='crimson',
                                   size=10),
                     )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
