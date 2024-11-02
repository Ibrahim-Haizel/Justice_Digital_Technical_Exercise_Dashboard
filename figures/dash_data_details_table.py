import dash_table
import pandas as pd

# Load your data
data = pd.read_csv('data/prison_data.csv')

def create_data_table(data):
    # Define the columns for the DataTable
    columns = [
        {'name': 'Year', 'id': 'year', 'type': 'numeric'},
        {'name': 'Month', 'id': 'month'},
        {'name': 'Prison Name', 'id': 'prison_name'},
        {'name': 'Prison Region', 'id': 'prison_region'},
        {'name': 'Prison Category', 'id': 'prison_category'},
        {'name': 'Prison Gender', 'id': 'prison_gender'},
        {'name': 'Receptions', 'id': 'receptions', 'type': 'numeric'},
        {'name': 'Releases', 'id': 'releases', 'type': 'numeric'},
    ]

    # Create the DataTable
    data_table = dash_table.DataTable(
        id='prison-data-table',
        columns=columns,
        data=data.to_dict('records'),
        sort_action='native',   # Enables sorting
        filter_action='native', # Enables filtering on all columns
        page_size=20,           # Number of rows per page
        style_table={'overflowX': 'auto'},
        style_cell={
            'minWidth': '150px', 'width': '150px', 'maxWidth': '150px',
            'whiteSpace': 'normal'
        },
    )

    return data_table