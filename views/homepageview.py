from fasthtml.common import *
from views.styles.homepagestyle import home_page_styles
from views.styles.footerstyle import site_footer
from views.styles.navbarstyle import navbar_style



def build_home_page(navbar = Div(
            A('Login', href='/sign-in-page'),
            A('Sign Up', href='/sign-up'),
            cls='navbar'
        )):
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('Gastro Tour Medellin'),
        Style(home_page_styles(), site_footer(), navbar_style())
    ),
    Body(
        navbar,
        Div('Gastro Tour Medellin', cls='title'),
        Div(
            Div(
                H3('Explore Restaurants Distance'),
                P('Discover the best restaurants in Medellin and find Manhatan distances between them'),
                Button('Explore Now', onclick="window.location.href='/find-distance-page';"),
                cls='functionality'
            ),
            Div(
                H3('Find Restaurants Location and Their Address in Medellin'),
                P('Find the top restaurants in Medellin with an amazing interactive map'),
                Button('View Map', onclick="window.location.href='/restaurants-map';"),
                cls='functionality'
            ),
            Div(
                H3('Compare Prices and Ratings'),
                P('Compare prices vs ratings with an exclusive plot with all top restaurants'),
                Button('See Offers', onclick="window.location.href='/scatter-plot';"),
                cls='functionality'
            ),
            cls='functionalities'
        ),
        Div(
            P('© 2024 Gastro Tour Medellin. All rights reserved.'),
            P(
                A('Privacy Policy', href='/privacy-policy'),
                '|',
                A('Contact Us', href='/contact-info')
            ),
            Div(
                A('Contribute on Patreon', href='https://patreon.com/user?u=122587768&utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink', target='_blank'),
                cls='social-icons'
            ),
            cls='footer'
)
    ),
    lang='en')