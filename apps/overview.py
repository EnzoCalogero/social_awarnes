from dash import  dcc, html

import plotly.graph_objects as go
import pandas as pd

from app import app

dataset = pd.read_csv("C:/gits_folders/social_awarnes/data/violence_data.csv")
country_df = pd.read_csv("C:/gits_folders/social_awarnes/data/wikipedia-iso-country-codes.csv")
country_df.columns = ["Country", "A2C", "A3C", "Num", "ISO"]
country_df.columns = ["Country", "A2C", "A3C", "Num", "ISO"]
datac_df = dataset.merge(country_df)


df = datac_df.groupby(["Country", "A3C"])["Value"].agg(["median", "max", "min", "mean"]).reset_index()

fig = go.Figure(data=go.Choropleth(
        locations=df['A3C'],
        z=df['max'],
        text=df['Country'],
        colorscale='Rainbow',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
    ))


fig.update_layout(
        title_text="World Map Female Violence",
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )


layout = html.Div([

       html.H4('Violence Against Women and Girls'),
       html.P("Survey data from 70 countries on the topic of violence against women and girls"),


       dcc.Graph(
             id='example-graph',
             figure=fig
         ),
       html.P(dcc.Link('Next Page', href='/First')), ], style={
                                                          'padding': '0px 10px 15px 10px',
                                                          'marginLeft': 'auto',
                                                          'marginRight': 'auto',
                                                          'width': "150vh",
                                                          'display': 'inline-block',
                                                          'boxShadow': '0px 0px 5px 5px rgba(37,52,113,0.4)'
                                                          },
)


if __name__ == '__main__':

    app.run_server(port=8050, debug=True)
