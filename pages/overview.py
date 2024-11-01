import dash
from dash import html

dash.register_page(__name__, path='/overview', order = 1)

layout = html.Div([
    html.H1('This is our overview page'),
    html.Div('This is our overview content.'),
])