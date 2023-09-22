# -*- coding: utf-8 -*-
import flask
from dash import Dash, html, dcc, Input, Output
from app import app
#app = Dash(__name__)
from apps import home, overview

colors = {
    'background': '#111111',
    'text': '#253471'}

layout = html.Div([
    html.Div([
        html.Div([
             html.H2(
                children="Dashboard Menu",
                id="h2_come",
                style={
                    'textAlign': 'center',
                    'text': colors['text'],
                    'font-family':'Glacial Indifference',
                    'color': colors['text'],
                    'bgcolor': colors['background']}
            )
        ], className='ten columns'),
        html.Div([
            html.A('Set the Focus DB', href='/setdb', target="_blank")
        ], className='two columns'),
    ], className="row"),
    ###########################################################################################################
    html.Div([
        html.P(id='intermediate-value_home', style={'float': 'right'}),
    ], className="row"),
    html.Div([
        html.P(dcc.Link('Go to Sessions Summary', href='/summary'), ),
        html.Iframe(src='/sparkline', height="450", width="35%", style={'border': '3', 'float': 'right'}),
        html.P(dcc.Link('Go to Channels Analytics', href='/channel_heatmap')),
        html.P(dcc.Link('Go to Connections Analytics', href='/connections')),
        html.P(dcc.Link('Go to Network Analytics', href='/network')),
        html.P(dcc.Link('Go to Templates Analytics', href='/templates_timeseries')),
        html.P(dcc.Link('Go to Tasks Analytics', href='/tasks_timeseries')),
        html.P(dcc.Link('Go to Failed Password Analytics (ELK)', href='/failpasswords')),
        html.P(dcc.Link('Go to Revealed Password Analytics (ELK)', href='/revealed')),
        html.P(dcc.Link('Go to Long Running Sessions Analytics (ELK)', href='/longrun')),
        #html.P(dcc.Link('Go to User Behavior Analytics', href='/uba')),

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


