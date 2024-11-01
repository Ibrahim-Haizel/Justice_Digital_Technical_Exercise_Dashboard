import dash
from dash import html

dash.register_page(__name__, path='/data-details', order = 2)

layout = html.Div([
    html.H1('This is our data details page'),
    html.Div('This is our data details content.'),
])