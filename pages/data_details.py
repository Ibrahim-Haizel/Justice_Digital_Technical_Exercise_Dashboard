import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd

from figures.dash_data_details_table import create_data_table

dash.register_page(__name__, path='/data-details', order=2)

# Load your data
data = pd.read_csv('data/prison_data.csv')

# Get unique values for filters
prison_regions = [{'label': region, 'value': region} for region in sorted(data['prison_region'].unique())]
prison_categories = [{'label': category, 'value': category} for category in sorted(data['prison_category'].unique())]
prison_genders = [{'label': gender, 'value': gender} for gender in sorted(data['prison_gender'].unique())]

layout = html.Div([
    html.H1('Data Details'),
    html.Div([
        html.Div([
            html.Label('Filter by Prison Region:'),
            dcc.Dropdown(
                id='region-filter',
                options=prison_regions,
                multi=True,
                placeholder='Select prison regions...'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        html.Div([
            html.Label('Filter by Prison Category:'),
            dcc.Dropdown(
                id='category-filter',
                options=prison_categories,
                multi=True,
                placeholder='Select prison categories...'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'}),
        html.Div([
            html.Label('Filter by Prison Gender:'),
            dcc.Dropdown(
                id='gender-filter',
                options=prison_genders,
                multi=True,
                placeholder='Select prison genders...'
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top', 'marginLeft': '2%'}),
    ], style={'marginBottom': '20px'}),
    html.Div(
        id='data-table-container'
    )
])

@callback(
    Output('data-table-container', 'children'),
    Input('region-filter', 'value'),
    Input('category-filter', 'value'),
    Input('gender-filter', 'value')
)
def update_table(selected_regions, selected_categories, selected_genders):
    filtered_data = data.copy()
    
    if selected_regions:
        filtered_data = filtered_data[filtered_data['prison_region'].isin(selected_regions)]
    if selected_categories:
        filtered_data = filtered_data[filtered_data['prison_category'].isin(selected_categories)]
    if selected_genders:
        filtered_data = filtered_data[filtered_data['prison_gender'].isin(selected_genders)]
    
    data_table = create_data_table(filtered_data)
    
    return data_table
