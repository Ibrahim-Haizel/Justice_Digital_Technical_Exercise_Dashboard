import pandas as pd

import dash
from dash import html, Output, Input, dcc

from figures.receptions_releases_line_chart import create_receptions_releases_chart
from figures.receptions_releases_stacked_bar_chart import create_stacked_bar_chart

from uk_gov_dash_components.Dropdown import Dropdown
import dash_oflog_components as doc

dash.register_page(__name__, path='/overview', order=1)

data = pd.read_csv('data/prison_data.csv')

# Ensure 'month' is ordered correctly
months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
data['month'] = pd.Categorical(data['month'], categories=months_order, ordered=True)

# Create a list of unique prison names for the dropdown options
prison_options = [{'label': 'All Prisons', 'value': 'All'}] + \
                 [{'label': prison, 'value': prison} for prison in sorted(data['prison_name'].unique())]

# Options for grouping field selection
group_field_options = [
    {'label': 'Prison Region', 'value': 'prison_region'},
    {'label': 'Prison Category', 'value': 'prison_category'}
]

layout = html.Div([
    html.H1('Prison Receptions and Releases'),
    html.Div([
        html.Div([
            Dropdown(
            id='prison-dropdown',
            label = 'Select a single prison from dropdown [optional]:',
            source=prison_options,
            placeholder="Select a specfic prison...",
            errorMessage="Enter a valid local authority",
            value='All'  # Default value is 'All Prisons'
            )
        ]),
        html.Div(
            dcc.Graph(id='receptions-releases-chart'), style={'width': '100%'}
        )
    ], style={'width': '100%'}),
    html.Div([
        html.Label('Select Category Grouping Field [for charts below]:', className="govuk-label"),  # Add the grouping field selection
        doc.RadioButton(
            id='group-field-radio',  # Make sure this ID matches with the State in your callback
            defaultValue='prison_region',
            options=group_field_options,
        ),
        html.H1('Receptions Breakdown by Category'),
    ]),
        dcc.Graph(id='receptions-chart'),
        html.H1('Releases Breakdown by Category'),
        dcc.Graph(id='releases-chart')], style={'width': '100%'})


# Define the callback to update the line chart
@dash.callback(
    Output('receptions-releases-chart', 'figure'),
    Input('prison-dropdown', 'value')
)
def update_chart(selected_prison):
    if selected_prison == 'All':
        filtered_data = data.copy()
    else:
        filtered_data = data[data['prison_name'] == selected_prison]
    
    # Call the chart creation function
    fig = create_receptions_releases_chart(filtered_data, selected_prison, months_order)
    return fig

# Define the callback to update the stacked bar chart
@dash.callback(
    # Output('receptions-releases-chart', 'figure'),
    Output('receptions-chart', 'figure'),
    Output('releases-chart', 'figure'),
    # Input('prison-dropdown', 'value'),
    Input('group-field-radio', 'value')
)
def update_charts(group_field): #could add selected_prison as first argument to function
    # if selected_prison == 'All':
    #     filtered_data = data.copy()
    #     title_suffix = 'All Prisons'
    # else:
    #     filtered_data = data[data['prison_name'] == selected_prison]
    #     title_suffix = selected_prison
    
    # # Create the receptions and releases line chart
    # fig_line = create_receptions_releases_chart(filtered_data, title_suffix, months_order)
    
    filtered_data = data.copy()

    # Titles for bar charts
    group_field_title = group_field.replace('_', ' ').title()
    title_receptions = f'Number of Receptions by Month (Grouped by {group_field_title})'
    title_releases = f'Number of Releases by Month (Grouped by {group_field_title})'
    
    # Create the receptions stacked bar chart
    fig_receptions = create_stacked_bar_chart(
        filtered_data, group_field, months_order, 'receptions', title_receptions)
    
    # Create the releases stacked bar chart
    fig_releases = create_stacked_bar_chart(
        filtered_data, group_field, months_order, 'releases', title_releases)
    
    return fig_receptions, fig_releases #could add fig_line as first argument to return statement