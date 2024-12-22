import os
import dash
from dash import Dash, html, dcc, Input, Output

from gov_uk_dashboards.lib.logging import configure_logging
from gov_uk_dashboards.lib.http_headers import setup_application_http_response_headers

from gov_uk_dashboards.template import read_template
from uk_gov_dash_components.ChangeLogBanner import ChangeLogBanner

from gov_uk_dashboards.components.plotly.phase_banner import phase_banner_with_feedback
from gov_uk_dashboards.components.plotly.footer import footer

from components.side_navbar import side_navbar, side_navbar_link, side_navbar_link_active
from components.header import header

app = Dash(
    __name__, 
    use_pages=True,  
    update_title=None,
)

# from constants import EMAIL_ADDRESS

cookie_link = html.Div([
    html.A("Cookies",
        href="/cookies-page",
        className="govuk-link govuk-footer__link",
        id="cookies-page-link")
    ])

privacy_policy_link = html.Div([
    html.A("Privacy Policy",
        href="/privacy-policy-page",
        className="govuk-link govuk-footer__link",
        id="privacy-policy-link")
    ])

accessibility_link = html.Div([
    html.A("Accessibility Statement",
        href="/accessibility-statement-page",
        className="govuk-link govuk-footer__link",
        id="accessibility-statement-link")
    ])

footer_links = [accessibility_link, cookie_link, privacy_policy_link]

layout = html.Div(
    [ 
        html.A(
            "Skip to main content",
            href="#main-content",
            className="govuk-skip-link",
        ),
        header("Prison Receptions & Releases Data Explorer"),
        html.Div(id="page_title", style={"display": "none"}, **{"aria-hidden": "true"}),
        html.Div(
            id="trigger_page_title_callback",
            style={"display": "none"},
            **{"aria-hidden": "true"},
        ),
        html.Div(
            children = ChangeLogBanner(
                updates=[
                    {
                        "date": "11-06-2024",
                        "heading": "This data explorer has recently been released as a prototype.",
                        "link": None,
                        "linkTitle": None,
                        "type": "Update",
                    }
                ]
            ),
            id="generate_update_banner"),
        html.Div(
            [
                phase_banner_with_feedback(
                    phase="beta",
                    feedback_link=f"mailto:?"
                    f"subject=Feedback on {app.title}",
                    link_id="feedback-link",
                ),
                    html.Div(
                        id="nav-section",
                        style={"display": "none"},
                    ),                  
                html.Div(
                    [
                        dcc.Location(id="url", refresh=False),
                        html.Div(
                            id="container_navbar_placeholder",
                            style={"margin-right": "20px"}
                        ),
                        html.Div( # Main content
                            children=dash.page_container,
                            id="page-content",
                            style={"width": "100%"}
                        ),
                    ],
                    className="govuk-main-wrapper--auto-spacing govuk-!-padding-top-2",
                    style={"display": "flex", "flex-direction": "row"},
                ),
            ],
            className=("govuk-width-container "),
        ),
        footer(footer_links),
    ]
)

# from configuration import sentry

# if os.environ.get("STAGE") == "production":
#     sentry.configure_sentry()

# configure_logging()

app.layout = layout
app.config.suppress_callback_exceptions = True
app.index_string = read_template()
server = app.server

# Callback to update navigation sections
@app.callback(
    [
        Output("nav-section", "children"),
        Output("container_navbar_placeholder", "children"),
    ],
    [Input("url", "pathname")]
)
def update_navbars(pathname):
    # Normalize the pathname by removing trailing slashes
    normalized_pathname = pathname.rstrip('/')

    # Get nav links from the page registry, excluding the not_found_404 page
    nav_links = []
    for page in dash.page_registry.values():
        # Skip the not_found_404 page
        if page["module"] == "pages.not_found_404":
            continue
            
        page_path = page["path"].rstrip('/')
        if page_path == normalized_pathname:
            nav_links.append(side_navbar_link_active(page["name"], page["path"]))
        else:
            nav_links.append(side_navbar_link(page["name"], page["path"]))

    # Create mobile and container navbar components
    mobile_nav = side_navbar(
        nav_links,
        identifier="mobile-navigation-items",
        nav_id="mobile-nav-section"
    )
    container_nav = side_navbar(
        nav_links,
        identifier="navigation-items"
    )

    return mobile_nav, container_nav

if __name__ == '__main__':
    app.run(debug=True)