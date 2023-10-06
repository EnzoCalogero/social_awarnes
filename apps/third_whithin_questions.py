from dash import Dash, html, dcc, Input, Output

import plotly.express as px
import pandas as pd
import numpy as np


app = Dash(__name__)
dataset = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")
Education = dataset[dataset["Demographics Question"] == "Education"]
Education = Education.groupby(['Demographics Response','Gender'])["Value"].agg(["median", "max", "min", "mean"]).reset_index()

Education = Education.sort_values(by=['median'], ascending=False)


app.layout = html.Div(    [
        html.H4("Graphing Light/Dark Mode with BooleanSwitch"),
        html.P("light | dark", style={"textAlign": "center"}),
        dcc.Checklist(
        id='x-axis',
        options=['country', 'day'],
        value=['time'],
        inline=True),
        dcc.Graph(id="pb-result")
    ]
)

@app.callback(
    Output("pb-result", "figure"),
    Input("x-axis", "value"),
)
def update_output(on):
    fig = px.bar(Education, x='Demographics Response', y='median', color='Gender')
    fig.update_layout(barmode='group')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)