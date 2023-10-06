
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

from app import app

df = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")
df_1 = df[df["Question"] == "... for at least one specific reason"].copy()
df_1 = df_1.sort_values(by=['Value'], ascending=False)

# List questions
layout = html.Div([
    html.H4("Analysis of the restaurant's revenue"),
    html.P("y-axis:"),
    dcc.Checklist(
        id='x-axis',
        options=['country', 'day'],
        value=['time'],
        inline=True
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis',
        options=['total_bill', 'tip', 'size'],
        value='total_bill',
        inline=True
    ),
    dcc.Graph(id="graph"),
    html.P(dcc.Link('Next Page', href='/Second')),
    html.P(dcc.Link('Back Page', href='/'))], style={#'width': '40%',
                  'padding': '0px 10px 15px 10px',
                  'marginL,eft': 'auto',
                  'marginRight': 'auto',
                  'width': "150vh",
                  'display': 'inline-block',
                  'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
                  })


@app.callback(
    Output("graph", "figure"),
    Input("x-axis", "value"),
    Input("y-axis", "value"))
def generate_chart(x, y):
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
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(family='Rockwell',
                                   color='crimson',
                                   size=10))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)