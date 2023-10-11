from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

from app import app

dataset = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")

Education = dataset[dataset["Demographics Question"] == "Education"]
Education = Education.groupby(['Demographics Response', 'Gender'])["Value"]\
                                            .agg(["median", "max", "min", "mean"]).reset_index()
Education = Education.sort_values(by=['median'], ascending=False)

Marital_status = dataset[dataset["Demographics Question"] == "Marital status"]
Marital_status = Marital_status.groupby(['Demographics Response', 'Gender'])["Value"]\
                                            .agg(["median", "max", "min", "mean"]).reset_index()
Marital_status = Marital_status.sort_values(by=['median'], ascending=False)

Age = dataset[dataset["Demographics Question"] == "Age"]
Age = Age.groupby(['Demographics Response', 'Gender'])["Value"]\
                                                .agg(["median", "max", "min", "mean"]).reset_index()
Age = Age.sort_values(by=['median'], ascending=False)

Residence = dataset[dataset["Demographics Question"] == "Residence"]
Residence = Residence.groupby(['Demographics Response', 'Gender'])["Value"]\
                                                .agg(["median", "max", "min", "mean"]).reset_index()
Residence = Residence.sort_values(by=['median'], ascending=False)

layout = html.Div([
         dbc.Row(
            dcc.Checklist(
                id='x-axis',
                options=['country', 'day'],
                value=['time'],
                inline=True)),

        dbc.Row([
            dbc.Col(dcc.Graph(id="education_graph"), width=6),
            dbc.Col(dcc.Graph(id="Residence_graph"), width=6),


        ]),

         dbc.Row([
             dbc.Col(dcc.Graph(id="Age_graph"), width=6),
             dbc.Col(dcc.Graph(id="Marital status_graph"), width=6),
         ])
    #, style={
        #           'padding': '0px 10px 15px 10px',
        #           'marginLeft': 'auto',
        #           'marginRight': 'auto',
        #           'width': "50%",
        #           'display': 'inline-block',
        #           'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
        #           }),
        # html.P(dcc.Link('Next Page', href='/Index')),
        # html.P(dcc.Link('Back Page', href='/Second')),
        ], style={'padding': '0px 10px 15px 10px',                  'marginL,eft': 'auto',
                  'marginRight': 'auto',
                  'width': "140vh",
                  'display': 'inline-block',
                  'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
                  }
         )


@app.callback(
    Output("education_graph", "figure"),
    Input("x-axis", "value"),
)
def update_education(on):
    fig = px.bar(Education, x='Demographics Response',
                 y='median',
                 color='Gender',
                 color_discrete_sequence=["pink", "blue"])
    fig.update_layout(
        title={
            'text': "Education impact on Man vs Woman Violence Expectation",

            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='% Expected Violence (global Median)',
            titlefont_size=16,
            tickfont_size=14,
            color='crimson',),

        xaxis=dict(
            title='',
            #titlefont_size=16,
            #tickfont_size=14,
            #color='crimson',
        ),
    )
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(barmode='group')
    return fig


@app.callback(
    Output("Marital status_graph", "figure"),
    Input("x-axis", "value"),
)
def update_marital(on):
    fig = px.bar(Marital_status, x='Demographics Response',
                 y='median',
                 color='Gender',
                 color_discrete_sequence=["pink", "blue"])
    fig.update_layout(
        title={
            'text': "Marital Status impact on Man vs Woman Violence Expectation",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='% Expected Violence (global Median)',
            titlefont_size=16,
            tickfont_size=14,
            color='crimson',),

        xaxis=dict(
            title='',
          #  titlefont_size=16,
          #  tickfont_size=14,
          #  color='crimson',
        ),
    )
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(barmode='group')
    return fig


@app.callback(
    Output("Residence_graph", "figure"),
    Input("x-axis", "value"),
)
def update_Residence(on):
    fig = px.bar(Residence, x='Demographics Response',
                 y='median',
                 color='Gender',
                 color_discrete_sequence=["pink", "blue"])
    fig.update_layout(
        title={
            'text': "Residence impact on Man vs Woman Violence Expectation",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='% Expected Violence (global Median)',
            titlefont_size=16,
            tickfont_size=14,
            color='crimson',),

        xaxis=dict(
            title='',
            #titlefont_size=16,
            #tickfont_size=14,
            #color='crimson',
        ),
    )
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(barmode='group')
    return fig


@app.callback(
    Output("Age_graph", "figure"),
    Input("x-axis", "value"),
)
def update_age(on):
    fig = px.bar(Age, x='Demographics Response',
                 y='median',
                 color='Gender',
                 color_discrete_sequence=["pink", "blue"])
    fig.update_layout(
        title={
            'text': "Age impact on Man vs Woman Violence Expectation",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='',
           # titlefont_size=16,
           # tickfont_size=14,
           # color='crimson',
            ),

        xaxis=dict(
            title='',
            #titlefont_size=16,
            #tickfont_size=14,
            #color='crimson',
        ),
    )
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(barmode='group')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
