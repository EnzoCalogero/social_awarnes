# -*- coding: utf-8 -*-

from dash import Dash, html, dcc, Input, Output
import pandas as pd
from app import app
#app = Dash(__name__)
from apps import home, Full_Details

# Dash Variables
colors = {
    'background': '#111111',
    'text': '#253471'
}
#df = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")

#############################################
###   Starting the Layout                ####
##############################################
app.layout= html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Div(id='my-div'),
], style={
    'font-family': 'Glacial Indifference',
    'width': '12%',
    'display': 'inline-block',
    'color': colors['text']
}
)
# End Layout


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/Full_Details':
        return Full_Details.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)

