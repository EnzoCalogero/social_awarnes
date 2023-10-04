
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

from app import app


df_ = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")

# List questions
questions_list = list(df_["Question"].unique())
demographic_questions_list = list(df_["Demographics Question"].unique())
demographic_response_list = list(df_["Demographics Response"].unique())
# /List questions

###############
##  Layout  ###
###############
layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='How Violence on Woman is Tolerate?'),
        html.H3(children='Are Man and Woman aware of it?'),
        ], style={'width': '20%',
                  'padding': '0px 10px 15px 10px',
                   'marginLeft': 'auto',
                   'marginRight': 'auto',
                  'display': 'inline-block'}),

    html.Div(children=[
        dcc.Dropdown(
            options=questions_list,
            value='... for at least one specific reason',
            id='questions_list'),
        dcc.Dropdown(
            options=demographic_questions_list,
            value='Age',
            id='demographic_questions_list'),
        dcc.Dropdown(
            id='demographic_answer_list'),
    ], style={'width': "70%", 'float': 'top', 'display': 'inline-block',
              'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'}),

    html.Div(children=[
         #html.Div(children=''' What the Female Thinks.'''),
         dcc.Graph(id='Female_Questions'),
         ], style={#'width': '40%',
                   'padding': '0px 10px 15px 10px',
                   'marginLeft': 'auto',
                   'marginRight': 'auto',
                   'width': "75vh",
                   'display': 'inline-block',
                   'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
                    }
    ),

    html.Div(children=[
         dcc.Graph(id='Male_Questions'),
        ], style={#'width': '40%',
                  'padding': '0px 10px 15px 10px',
                  'marginLeft': 'auto',
                  'marginRight': 'auto',
                  'width': "75vh",
                  'display': 'inline-block',
                  'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
                  }
    ),

    html.Div(children=[
        dcc.Graph(id='Delta_Questions'),
        ], style={
          'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto',
          'marginRight': 'auto',
          'width': "75vh",
          'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)',
          'display': 'inline-block',
            }),
    ], style={'font-family': 'Glacial Indifference', 'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "160vh",
          'boxShadow': '0px 0px 5px 5px rgba(37, 52, 113, 0.4)'})

###################
## Call Backs  ###
##################


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
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
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

    fig.update_layout(xaxis={'categoryorder': 'total descending'})
    return fig


@app.callback(
    Output('Delta_Questions', 'figure'),
    Input('demographic_answer_list', 'value'),
    Input('questions_list', 'value'))
def update_figure(demographic_value, question_value):
    filtered_df = df_[df_["Question"] == question_value].copy()
    filtered_df = filtered_df[filtered_df["Demographics Response"] == demographic_value].copy()
    M = filtered_df[filtered_df["Gender"] == "M"].copy()
    M = M[["Country", "Value"]]
    M = M.set_index("Country")

    F = filtered_df[filtered_df["Gender"] == "F"].copy()
    F = F[["Country", "Value"]]
    F = F.set_index("Country")

    MF = M.join(F, how='right', lsuffix='_M')
    MF["Delta"] = MF.Value_M - MF.Value
    MF["Country"] = MF.index
    MF["Gender"] = "aa"
    MF["Color"] = np.where(MF["Delta"] < 0, '#ff97ff', '#19d3f3')

    fig = px.bar(MF,
                 y="Delta",
                 x="Country",
                 #color_discrete_sequence=['#bab0ac'],
                 #color="Gender"
                 )
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
    fig.update_layout(showlegend=False, title="What the Male vs Female Thinks. (Male % - Female%)")
    fig.update_traces(marker_color=MF["Color"])
    return fig


if __name__ == '__main__':
    # app.run_server(port= 8050, host="0.0.0.0") # docker
    app.run_server(port=8050, debug=True)  # interactive
