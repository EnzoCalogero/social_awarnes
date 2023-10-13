from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app

df2 = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")
df2 = df2[df2.Question !="... for at least one specific reason"]
df2 = df2.sort_values(by=['Value'], ascending=False)

layout = html.Div([
    dbc.Row(
        dbc.Col(
    html.H4("For Each Question Man vs Woman Expectation"),
            width={"size": 6, "offset": 3},
        )),

    dbc.Row(
        dbc.Col([
    html.P("y-axis:"),
    dcc.Checklist(
        id='x-axis',
        options=['country', 'day'],
        value=['time'],
        inline=True
    ),
            ],
            width={"size": 6, "offset": 3},
        )),

    dbc.Row(
        dbc.Col(
    dcc.Graph(id="graph_question"),

            width={"size": 10, "offset": 1},
        )),

    dbc.Row(
        dbc.Col([
    html.P(dcc.Link('Next Page', href='/Third')),
    html.P(dcc.Link('Back Page', href='/First'))
,
            ],
            width={"size": 6, "offset": 3},
        )),

    ], style={
                  'padding': '0px 10px 15px 10px',
                  'marginLeft': 'auto',
                  'marginRight': 'auto',
                  'width': "150vh",
                  'display': 'inline-block',
                  'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
                  })


@app.callback(
    Output("graph_question", "figure"),
    Input("x-axis", "value"))
def generate_question(x):
    fig = px.box(df2,
                 x="Question",
                 y="Value",
                 color="Gender",
                 color_discrete_sequence=["pink", "blue"],
                 )
    fig.update_layout(
        title={
            'text': "For Each Question Man vs Woman Expectation",
 #           'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(
        xaxis=dict(
            title='',
        )),
    fig.update_layout(
        yaxis=dict(
            title='% Expected Violence',
        )),
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(family='Rockwell',
                                   color='crimson',
                                   size=10))
    return fig


if __name__ == '__main__':

    app.run_server(debug=False)
