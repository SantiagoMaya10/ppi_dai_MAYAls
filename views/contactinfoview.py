from fasthtml.common import *
from views.styles.contactinfostyle import contact_info_style
import os


def build_about_page():
    # Create the navbar
    navbar = Div(cls='navbar')(
        A('Home', href='/')  # Link back to homepage
    )

    # Create the footer
    footer = Div(cls='footer')(
        P('© 2024. All rights reserved.')
    )

    # Create the about page content
    about_content = Div(cls='about-content')(
        H1('About the Creator'),
        P('Name: Luis Santiago Maya Restrepo'),
        P('Undergraduate: 9th semester of Systems Engineering at the National University of Colombia'),
        P('LinkedIn: ', A('Luis Santiago Maya Restrepo on LinkedIn', href=os.getenv("LINKEDIN"), target='_blank')),
        P(f'Forma de contacto: {os.getenv("EMAIL")}')
        
    )

    # Build the page with navbar, content, and footer
    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('About the Creator'),
            Style(contact_info_style())  # Add necessary styles
        ),
        Body(
            navbar,
            about_content,
            footer
        )
    )