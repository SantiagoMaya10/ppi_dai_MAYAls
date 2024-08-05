from fasthtml.common import *


def build_home_page():
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('Gastro Tour Medellin'),
        Link(rel='stylesheet', href='styles.css'),
        Style('body {\n            font-family: Arial, sans-serif;\n            margin: 0;\n            padding: 0;\n            background-color: #f9f9f9;\n        }\n\n        .navbar {\n            background-color: #333;\n            overflow: hidden;\n            padding: 10px 20px;\n        }\n\n        .navbar a {\n            float: right;\n            color: #f2f2f2;\n            text-align: center;\n            padding: 14px 16px;\n            text-decoration: none;\n            font-size: 17px;\n        }\n\n        .navbar a:hover {\n            background-color: #ddd;\n            color: black;\n        }\n\n        .title {\n            text-align: center;\n            padding: 40px 0;\n            background-color: #333;\n            color: white;\n            font-size: 36px;\n        }\n\n        .functionalities {\n            display: flex;\n            justify-content: space-around;\n            margin: 20px 0;\n            padding: 0 20px;\n        }\n\n        .functionality {\n            background-color: white;\n            padding: 20px;\n            margin: 10px;\n            border-radius: 8px;\n            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n            width: 30%;\n            text-align: center;\n        }\n\n        .functionality h3 {\n            margin: 0 0 10px;\n        }\n\n        .functionality p {\n            color: #666;\n        }\n\n        .functionality button {\n            padding: 10px 20px;\n            background-color: #333;\n            color: white;\n            border: none;\n            border-radius: 5px;\n            cursor: pointer;\n        }\n\n        .functionality button:hover {\n            background-color: #555;\n        }') 
    ),
    Body(
        Div(
            A('Login', href='#login'),
            A('Sign Up', href='#signup'),
            cls='navbar'
        ),
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
        )
    ),
    lang='en')