import plotly.express as px

def create_receptions_releases_chart(filtered_data, selected_prison, months_order):
    # Group data by 'month' and sum 'receptions' and 'releases'
    grouped = filtered_data.groupby('month').agg({'receptions': 'sum', 'releases': 'sum'}).reset_index()
    
    # Melt the DataFrame for plotting
    melted = grouped.melt(id_vars='month', value_vars=['receptions', 'releases'],
                          var_name='Type', value_name='Count')
    
    #Use custom color palette for color blind friendly colors
    custom_palette = px.colors.qualitative.Set1
    
    # Create the line chart
    fig = px.line(melted, x='month', y='Count', color='Type', markers=True,
                  title=f'Number of Receptions and Releases by Month ({selected_prison})',
                  color_discrete_sequence= custom_palette) #['#636EFA', '#EF553B'])  # Modern color palette
    
    # Update layout for a clean look
    fig.update_layout(
        autosize=True,
        xaxis_title='Month',
        yaxis_title='Number',
        legend_title='Category',
        xaxis=dict(categoryorder='array', categoryarray=months_order, showgrid=False),
        yaxis=dict(showgrid=False),
        font=dict(family='Arial, sans-serif', size=14, color='#4A4A4A'),
        title=dict(font=dict(size=20), y=0.95),  # Adjust title position
        plot_bgcolor='white',
        margin=dict(l=40, r=40, t=80, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.99,
            xanchor="center",
            x=0.8,
            font=dict(size=12)
        )
    )
    
    # Rotate x-axis labels for clarity
    fig.update_xaxes(tickangle=-45)
    
    # Update marker style
    fig.update_traces(marker=dict(size=8, line=dict(width=1, color='DarkSlateGrey')))
    
    return fig

