import plotly.express as px

def create_stacked_bar_chart(filtered_data, group_field, months_order, y_column, title):
    # Group data by month and the selected group_field, summing the y_column
    grouped = filtered_data.groupby(['month', group_field])[y_column].sum().reset_index()

    #Use custom color palette for color blind friendly colors
    custom_palette = px.colors.qualitative.Set3
    
    # Create the stacked bar chart
    fig = px.bar(
        grouped, 
        x='month', 
        y=y_column, 
        color=group_field, 
        barmode='stack',
        title=title,
        category_orders={'month': months_order},
        color_discrete_sequence=custom_palette
    )
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='white',
        xaxis_title='Month',
        yaxis_title=f'Number of {y_column.capitalize()}',
        legend_title=group_field.replace('_', ' ').title(),
    )
    return fig