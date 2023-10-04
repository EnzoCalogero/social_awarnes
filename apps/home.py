# -*- coding: utf-8 -*-
import flask
from dash import Dash, html, dcc, Input, Output
from app import app

colors = {
    'background': '#111111',
    'text': '#253471'}

layout = html.Div([
    html.Div([
        html.Div([
             html.H2(
                children="Violent Agains Woman Around the World",
                id="h2_come",
                style={
                    'textAlign': 'center',
                    'text': colors['text'],
                    'font-family':'Glacial Indifference',
                    'color': colors['text'],
                    'bgcolor': colors['background']}
            )
        ], className='ten columns'),
    ], className="row"),
    ###########################################################################################################
    html.Div([
        html.P(id='intermediate-value_home', style={'float': 'right'}),
    ], className="row"),
    html.Div([
        html.P(dcc.Link('Full Details', href='/Full_Details'), ),
        html.P(dcc.Link('First Overview', href='/First_Overview'), ),
html.P(dcc.Link('First', href='/First'), ),

        #html.Iframe(src='/sparkline', height="450", width="35%", style={'border': '3', 'float': 'right'}),
        #html.P(dcc.Link('Go to Channels Analytics', href='/channel_heatmap')),

    ]),
], style={
    'font-family': 'Glacial Indifference',
    'padding': '0px 10px 15px 10px',
    'marginLeft': 'auto',
    'marginRight': 'auto',
    'width': '160vh',
    'color': colors['text'],
    'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'}
)


