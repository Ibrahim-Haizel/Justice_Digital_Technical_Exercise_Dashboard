import dash
from dash import html
from components.Hero import Hero

dash.register_page(__name__, path='/', order = 0)

layout = html.Div([
    Hero(
        title="Prison Receptions and Releases Data Explorer",
        text="Gain insights into prison receptions and releases across the system. Navigate to the overview page for visual trends by month, region, and category, or explore the detail page for in-depth data filtering and sorting options.",
        button_text="Get started",
        button_link="/overview",
        show_button=True
    )

])