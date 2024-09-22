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
                H3('Explore Restaurants'),
                P('Discover the best restaurants in Medellin with detailed reviews and ratings.'),
                Button('Explore Now', onclick="window.location.href='#explore-restaurants';"),
                cls='functionality'
            ),
            Div(
                H3('Food Events'),
                P('Stay updated with the latest food events and festivals happening around the city.'),
                Button('View Events', onclick="window.location.href='#food-events';"),
                cls='functionality'
            ),
            Div(
                H3('Special Offers'),
                P('Get exclusive discounts and special offers from partnered restaurants.'),
                Button('See Offers', onclick="window.location.href='#special-offers';"),
                cls='functionality'
            ),
            cls='functionalities'
        ),
        Div(
            Div(
                H3('Find How Far Your Favorite Place Is From You'),
                P('Enter your desired place and we´ll tell you how far you are'),
                Button('Where Is It', onclick="window.location.href='#explore-restaurants';"),
                cls='functionality'
            ),
            Div(
                H3('Rate Places You Have Visited'),
                P('Give your feedback and opinion on the places we recommend'),
                Button('Rate Places', onclick="window.location.href='#food-events';"),
                cls='functionality'
            ),
            Div(
                H3('Get Your Guide'),
                P('We have some recommended guides for you,\
                   book one of them if you want and prepare a nice tour!'),
                Button('Contact Guide', onclick="window.location.href='#special-offers';"),
                cls='functionality'
            ),
            cls='functionalities'
        ),
        Div(
            P('© 2024 Gastro Tour Medellin. All rights reserved.'),
            P(
                A('Privacy Policy', href='#privacy'),
                '|',
                A('Terms of Service', href='#terms'),
                '|',
                A('Contact Us', href='#contact')
            ),
            Div(
                A('Contribute on Patreon', href='https://patreon.com/user?u=122587768&utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink', target='_blank'),
                cls='social-icons'
            ),
            cls='footer'
)
    ),
    lang='en')