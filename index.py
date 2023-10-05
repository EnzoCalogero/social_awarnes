# -*- coding: utf-8 -*-
from dash import Dash, html, dcc, Input, Output
from app import app
from apps import home, Full_Details, First_Overview, overview, second_Question

# Dash Variables
colors = {
    'background': '#111111',
    'text': '#253471'
}

#############################################
###  Starting the Layout                 ####
##############################################
app.layout = html.Div([
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
    elif pathname == '/First_Overview':
        return First_Overview.layout
    elif pathname == '/First':
        return overview.layout
    elif pathname == '/Second':
        return second_Question.layout
    else:
        return '404'


if __name__ == '__main__':
     app.run_server(port=8061, debug=True)

