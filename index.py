# -*- coding: utf-8 -*-
from dash import html, dcc, Input, Output
from app import app
from apps import home, Full_Details, First_Overview, overview, second_Question, third_whithin_questions

# Dash Variables
colors = {
    'background': '#111111',
    'text': '#253471'
}

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


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return overview.layout
    elif pathname == '/overview':
        return overview.layout
    elif pathname == '/First':
        return First_Overview.layout
    elif pathname == '/Second':
        return second_Question.layout
    elif pathname == '/Third':
        return third_whithin_questions.layout
    elif pathname == '/Full_Details':
        return Full_Details.layout
    elif pathname == '/index':
        return home.layout
    else:
        return home.layout


if __name__ == '__main__':

    app.run_server(port=8061, debug=True)
