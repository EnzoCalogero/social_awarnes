from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import numpy as np
import pandas as pd

from app import app

config = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['zoom2d', 'hoverCompareCartesian', 'hoverClosestCartesian', 'toggleSpikelines']
}

dataset = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")

Education = dataset[dataset["Demographics Question"] == "Education"]
Marital_status = dataset[dataset["Demographics Question"] == "Marital status"]
Age = dataset[dataset["Demographics Question"] == "Age"]
Residence = dataset[dataset["Demographics Question"] == "Residence"]

country = dataset.sort_values(by=['Country'], ascending=True)
country = country['Country'].unique()
country = np.concatenate((country, ["All Countries"]))

layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.H4("For Each Demographic the Violence  % Expectation"),
            width={"size": 6, "offset": 2},
        )),
    dbc.Row([
        dbc.Col(
            html.H5("Countries Selection:"),
            width={"size": 2, "offset": 4}
        ),
        dbc.Col(
            dcc.Dropdown(
                id='country2_id',
                options=country,
                value='All Countries',
                multi=True,
                clearable=False, ),
            width={"size": 4, }, )
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id="education_graph",
                          config=config), width=6),
        dbc.Col(dcc.Graph(id="Residence_graph",
                          config=config), width=6),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id="Age_graph",
                          config=config), width=6),
        dbc.Col(dcc.Graph(id="Marital status_graph",
                          config=config), width=6),
    ]),
    dbc.Row(
        dbc.Col([
            html.P(dcc.Link('Next Page', href='/Full_Details')),
            html.P(dcc.Link('Back Page', href='/Second')),
        ],
            width={"size": 6, "offset": 3},
        )),

], style={'padding': '0px 10px 15px 10px',
          'marginL,eft': 'auto',
          'marginRight': 'auto',
          'width': "140vh",
          'display': 'inline-block',
          'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
          }
)


@app.callback(
    Output("education_graph", "figure"),
    Input("country2_id", "value"),
)
def update_education(country_dict):

    if "All Countries" in country_dict:
        df_1_ = Education
    else:
        df_1_ = Education[Education.Country.isin(country_dict)]

    df_1_ = df_1_.groupby(['Demographics Response', 'Gender'])["Value"] \
            .agg(["median", "max", "min", "mean"]).reset_index()
    df_1_ = df_1_.sort_values(by=['median'], ascending=False)
    fig = px.bar(df_1_, x='Demographics Response',
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
        showlegend=False,
        yaxis=dict(
            title='% Expected Violence (global Median)',
            titlefont_size=16,
            tickfont_size=14,
            color='crimson', ),

        xaxis=dict(
            title='',
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
    Input("country2_id", "value"),
)
def update_marital(country_dict):
    if "All Countries" in country_dict:
        df_1_ = Marital_status
    else:
        df_1_ = Marital_status[Marital_status.Country.isin(country_dict)]

    df_1_ = df_1_.groupby(['Demographics Response', 'Gender'])["Value"] \
        .agg(["median", "max", "min", "mean"]).reset_index()
    df_1_ = df_1_.sort_values(by=['median'], ascending=False)

    fig = px.bar(df_1_, x='Demographics Response',
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
        showlegend=False,
        yaxis=dict(
            title='',
            titlefont_size=16,
            tickfont_size=14,
            color='crimson', ),

        xaxis=dict(
            title='',
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
    Input("country2_id", "value"),
)
def update_residence(country_dict):

    if "All Countries" in country_dict:
        df_1_ = Residence
    else:
        df_1_ = Residence[Residence.Country.isin(country_dict)]

    df_1_ = df_1_.groupby(['Demographics Response', 'Gender'])["Value"] \
        .agg(["median", "max", "min", "mean"]).reset_index()
    df_1_ = df_1_.sort_values(by=['median'], ascending=False)
    fig = px.bar(df_1_, x='Demographics Response',
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
            title='',
            titlefont_size=16,
            tickfont_size=14,
            color='crimson', ),
        legend_title_text="gender of the surveyed",
        showlegend=True,
        xaxis=dict(
            title='',
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
    Input("country2_id", "value"),
)
def update_age(country_dict):

    if "All Countries" in country_dict:
        df_1_ = Age
    else:
        df_1_ = Age[Age.Country.isin(country_dict)]

    df_1_ = df_1_.groupby(['Demographics Response', 'Gender'])["Value"] \
        .agg(["median", "max", "min", "mean"]).reset_index()
    df_1_ = df_1_.sort_values(by=['median'], ascending=False)

    fig = px.bar(df_1_, x='Demographics Response',
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
        ),
        showlegend=False,
        xaxis=dict(
            title='',
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
