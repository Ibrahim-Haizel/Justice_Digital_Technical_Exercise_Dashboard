"""navbar"""

from typing import Optional
from dash import html, dcc


def side_navbar(
    links, identifier: Optional[str] = None, nav_id: str = "navbar-section"
):
    """A navigation bar for switching between dashboards."""
    return html.Nav(
        html.Ul(
            links,
            id=identifier if identifier is not None else "",
            className="moj-side-navigation__list",
        ),
        className="moj-side-navigation" if "mobile" not in nav_id else "",
        role="navigation",
        id=nav_id,
        style = {"width":"100%"}
    )