from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
app = Dash(__name__)

df = pd.read_csv("data/violence_data.csv")
df = df[df["Demographics Response"] == "25-34"].copy()

# List questions
questions_list = list(df["Question"].unique())
# /List questions

###############
##  Layout  ###
###############

app.layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='Are Woman Created Equal?'),
        html.H3(children='Are Man and Woman aware of it?'),
        dcc.Dropdown(
            options=questions_list,
            value='... for at least one specific reason',
            id='questions_list')
        ], style={'width': '30%'}),

    html.Div(children=[
         #html.Div(children=''' What the Female Thinks.'''),
         dcc.Graph(id='Female_Questions'),
         ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div(children=[
        #html.Div(children='''  What the Male Thinks.'''),
        dcc.Graph(id='Male_Questions'),
        ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div(children=[
        html.Div(children='''  What is the Delta.'''),
        dcc.Graph(id='Delta_Questions'),
    ], style={'width': '49%', 'display': 'inline-block'}),
    ])

###################
## Call Backs  ###
##################

@app.callback(
    Output('Female_Questions', 'figure'),
    Input('questions_list', 'value'))
def update_figure(value):
    filtered_df = df[df["Question"] == value].copy()
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
    Input('questions_list', 'value'))
def update_figure(value):
    filtered_df = df[df["Question"] == value].copy()
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
    Input('questions_list', 'value'))
def update_figure(value):
    filtered_df = df[df["Question"] == value].copy()
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

    fig = px.bar(MF,
                 y="Delta",
                 x="Country",
                 color_discrete_sequence=['#bab0ac'],
                 color="Gender")
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
    fig.update_layout(showlegend=False, title="What the Female Thinks.")
    return fig


if __name__ == '__main__':
    # app.run_server(port= 8050, host="0.0.0.0") # docker
    app.run_server(port=8050, debug=True)  # interactive
