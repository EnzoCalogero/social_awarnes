# -*- coding: utf-8 -*-
from dash import html, dcc

colors = {
    'background': '#111111',
    'text': '#253471'}

layout = html.Div([
    html.Div([
        html.Div([
            html.H2(
                children="Violent Against Woman Around the World",
                id="h2_come",
                style={
                    'textAlign': 'center',
                    'text': colors['text'],
                    'font-family': 'Glacial Indifference',
                    'color': colors['text'],
                    'bgcolor': colors['background']}
            )
        ], className='ten columns'),
    ], className="row"),

    html.Div([
        html.P(id='intermediate-value_home', style={'float': 'right'}),
    ], className="row"),
    html.Div([
        html.P(dcc.Link('Overview', href='/')),
        html.P(dcc.Link('First', href='/First')),
        html.P(dcc.Link('Second', href='/Second')),
        html.P(dcc.Link('Third', href='/Third')),

        html.P(dcc.Link('Appendix_Full Details', href='/Full_Details')),
        html.P(dcc.Link('Index Pages', href='/index')),
    ])], style={
    'font-family': 'Glacial Indifference',
    'padding': '0px 10px 15px 10px',
    'marginLeft': 'auto',
    'marginRight': 'auto',
    'width': '160vh',
    'color': colors['text'],
    'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'}
)
