import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output

from app import app

df_ = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")

# List questions
questions_list = list(df_["Question"].unique())
demographic_questions_list = list(df_["Demographics Question"].unique())
demographic_response_list = list(df_["Demographics Response"].unique())
# /List questions

layout = html.Div(children=[
    dbc.Row(
        dbc.Col(
            html.H1(children='How Violence on Woman is Tolerate?'),
            width={"size": 6, "offset": 2},
        )),
    dbc.Row([
        dbc.Col(
            html.H3(children='Are Man and Woman aware of it?'),
            width={"size": 4, "offset": 1}),
        dbc.Col([
            dcc.Dropdown(
                options=questions_list,
                value='... for at least one specific reason',
                id='questions_list'),
            dcc.Dropdown(
                options=demographic_questions_list,
                value='Age',
                id='demographic_questions_list'),
            dcc.Dropdown(
                id='demographic_answer_list')
        ], width={"size": 4, "offset": 1}),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='Female_Questions',
                      ), width={"size": 6}
        ),
        dbc.Col(
            dcc.Graph(id='Male_Questions'),
            width={"size": 6})
    ]),

    dbc.Row(
        dbc.Col(
            dcc.Graph(id='Delta_Questions'),
            width={"size": 6, "offset": 3}
        )),

    dbc.Row(
        dbc.Col([
            html.P(dcc.Link('Back Page', href='/Third')),
        ],
            width={"size": 6, "offset": 3},
        ))
], style={'font-family': 'Glacial Indifference',
          'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto',
          'marginRight': 'auto',
          'width': '160vh',
          'boxShadow': '0px 0px 5px 5px rgba(37, 52, 113, 0.4)'})


@app.callback(
    Output('demographic_answer_list', 'options'),
    Output('demographic_answer_list', 'value'),
    Input("demographic_questions_list", 'value'))
def set_response(value):
    temp = df_[df_["Demographics Question"] == value]
    options = list(temp["Demographics Response"].unique())
    return options, options[0]


@app.callback(
    Output('Female_Questions', 'figure'),
    Input('demographic_answer_list', 'value'),
    Input('questions_list', 'value'))
def update_figure(demographic_value, question_value):
    filtered_df = df_[df_["Question"] == question_value].copy()
    filtered_df = filtered_df[filtered_df["Demographics Response"] == demographic_value].copy()
    filtered_df = filtered_df[filtered_df["Gender"] == "F"].copy()
    fig = px.bar(filtered_df,
                 y="Value",
                 x="Country",
                 color_discrete_sequence=['#ff97ff'],
                 color="Gender")
    fig.update_layout(xaxis={'categoryorder': 'total descending', 'title': ''})
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(showlegend=False, title="What the Female Thinks.")
    return fig


@app.callback(
    Output('Male_Questions', 'figure'),
    Input('demographic_answer_list', 'value'),
    Input('questions_list', 'value'))
def update_figure(demographic_value, question_value):
    filtered_df = df_[df_["Question"] == question_value].copy()
    filtered_df = filtered_df[filtered_df["Demographics Response"] == demographic_value].copy()
    filtered_df = filtered_df[filtered_df["Gender"] == "M"].copy()

    fig = px.bar(filtered_df,
                 y="Value",
                 x="Country",
                 color_discrete_sequence=['#19d3f3'],
                 color="Gender")
    fig.update_layout(showlegend=False, title="What the Male Thinks.")
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(xaxis={'categoryorder': 'total descending',
                             'title': ''})
    return fig


@app.callback(
    Output('Delta_Questions', 'figure'),
    Input('demographic_answer_list', 'value'),
    Input('questions_list', 'value'))
def update_figure(demographic_value, question_value):
    filtered_df = df_[df_["Question"] == question_value].copy()
    filtered_df = filtered_df[filtered_df["Demographics Response"] == demographic_value].copy()
    m = filtered_df[filtered_df["Gender"] == "M"].copy()
    m = m[["Country", "Value"]]
    m = m.set_index("Country")

    f = filtered_df[filtered_df["Gender"] == "F"].copy()
    f = f[["Country", "Value"]]
    f = f.set_index("Country")

    mf = m.join(f, how='right', lsuffix='_M')
    mf["Delta"] = mf.Value_M - mf.Value
    mf["Country"] = mf.index
    mf["Gender"] = "aa"
    mf["Color"] = np.where(mf["Delta"] < 0, '#ff97ff', '#19d3f3')

    fig = px.bar(mf,
                 y="Delta",
                 x="Country",
                 )
    fig.update_layout(xaxis={'categoryorder': 'total descending', 'title': '', })
    fig.update_xaxes(tickangle=45,
                     tickfont=dict(
                         family='Rockwell',
                         color='crimson',
                         size=14))
    fig.update_layout(showlegend=False, title="What the Male vs Female Thinks. (Male % - Female%)")
    fig.update_traces(marker_color=mf["Color"])
    return fig


if __name__ == '__main__':
    # app.run_server(port= 8050, host="0.0.0.0") # docker
    app.run_server(port=8050, debug=True)  # interactive
