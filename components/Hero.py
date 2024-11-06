import dash
from dash import html
from dash_svg import Svg, Path

# Create the ONS Hero Section component
def Hero(
    title="Design and build digital services for the ONS",
    text="Everything you need to make accessible, consistent digital products",
    button_text="Get started",
    button_link="#0",  # Default link when the button is included
    show_button=True   # Parameter to control button visibility
):
    container_class = "ons-hero__container ons-container"
    # Add specific class based on whether the button is shown or not
    container_class += " ons-hero__container--has-button" if show_button else " ons-hero__container--no-button"

    return html.Section(
        className="ons-hero ons-grid--gutterless ons-hero--dark",
        children=[
            html.Div(
                className=container_class,
                children=[
                    html.Div(
                        className="ons-hero__details ons-grid__col ons-col-8@m ons-col-10@s@m",
                        children=[
                            html.Header(
                                children=[
                                    html.H1(
                                        className="ons-hero__title ons-u-fs-3xl",
                                        children=title,
                                    )
                                ]
                            ),
                            html.P(
                                className="ons-hero__text",
                                children=text,
                            ),
                            # Conditionally render the button based on show_button
                            html.A(
                                href=button_link,
                                role="button",
                                className="ons-btn ons-btn--ghost ons-btn--link ons-js-submit-btn",
                                children=[
                                    html.Span(
                                        className="ons-btn__inner",
                                        children=[
                                            html.Span(
                                                className="ons-btn__text",
                                                children=button_text,
                                            ),
                                            Svg(
                                                className="ons-icon ons-u-ml-2xs",
                                                viewBox="0 0 17 13",
                                                xmlns="http://www.w3.org/2000/svg",
                                                fill="currentColor",
                                                role="img",
                                                children=Path(
                                                    d="m10 .2-.9.9c-.1.1-.1.4 0 .5l4 4H.6c-.2 0-.4.2-.4.4v1.2c0 .2.2.4.4.4h12.5l-3.9 3.7c-.2.2-.2.4 0 .6l.8.9c.2.2.4.2.6 0L16.8 7c-.2-.2.2-.4 0-.6L10.7.3c-.3-.2-.5-.2-.7-.1z"
                                                ),
                                            ),
                                        ],
                                    )
                                ],
                            ) if show_button else None,  # Only render if show_button is True
                        ],
                    )
                ],
            )
        ],
    )
