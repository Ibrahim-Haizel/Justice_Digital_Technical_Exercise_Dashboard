import dash
from dash import html
from constants import EMAIL_ADDRESS

dash.register_page(__name__)

layout = html.Div([
    html.Br(),
    html.Br(),
    html.Main(className="govuk-main-wrapper govuk-main-wrapper--l", role="main", children=[
        html.Div(className="govuk-grid-row", children=[
            html.Div(className="govuk-grid-column-two-thirds", children=[
                html.H1("Page not found", className="govuk-heading-l"),
                html.Br(),
                html.P("If you typed the web address, check it is correct.", className="govuk-body"),
                html.P("If you pasted the web address, check you copied the entire address.", className="govuk-body"),
                html.P(
                    [
                        "If the web address is correct or you selected a link or button, try refreshing the page, or going back to ",
                        html.A("Return to dashboard home", href="/", className="govuk-link"),
                        "."
                    ],
                    className="govuk-body",
                ),
                html.P(
                    [
                        "Contact the team on ",
                        html.A(EMAIL_ADDRESS, href=f"mailto:{EMAIL_ADDRESS}", className="govuk-link"),
                        " if this keeps happening."
                    ],
                    className="govuk-body",
                ),
            ])
        ])
    ])
]) 