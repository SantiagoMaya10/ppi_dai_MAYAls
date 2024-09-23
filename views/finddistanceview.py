from fasthtml.common import *
from views.styles.homepagestyle import home_page_styles
from views.styles.footerstyle import site_footer
from views.styles.finddistancestyle import find_distance_style
from usecases.findallrestaurantsusecase import find_all_restaurants

def build_find_restaurants_distance_page():
    restaurants = find_all_restaurants()

    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Explore Restaurants'),
            Style(home_page_styles(), site_footer(), find_distance_style()),
            Script(src="https://unpkg.com/htmx.org")  # Add htmx script to enable htmx functionality
        ),
        Body(
            Div(cls='navbar')(
                A('Home', href='/')
            ),
            Div(cls='explore-title')(
                H1('Explore Restaurants in Medellin')
            ),
            Div(cls='restaurant-table-container')(
                H3('List of Restaurants'),
                Table(cls='restaurant-table')(
                    Thead(
                        Tr(
                            Th('ID'),
                            Th('Name'),
                            Th('Latitude'),
                            Th('Longitude'),
                            Th('Address'),
                            Th('Average price USD'),
                            Th('Average user rating')
                        )
                    ),
                    Tbody(
                        *[
                            Tr(
                                Td(str(restaurant['id'])),
                                Td(restaurant['name']),
                                Td(str(restaurant['location_lat'])),
                                Td(str(restaurant['location_lon'])),
                                Td(restaurant['address']),
                                Td(restaurant['average_price_usd']),
                                Td(restaurant['visitors_average_rating']),


                            )
                            for restaurant in restaurants
                        ]
                    )
                )
            ),
            Div(cls='compare-section')(
                H3('Find the Manhatan distance between two restaurants'),
                Form(
                    hx_post='/find-distance-restaurants',  # htmx attribute to send AJAX request
                    hx_target='#distance-result',  # Target div where the result will be injected
                    hx_swap='innerHTML',  # Swap the inner content of the target div
                    method='POST'
                )(
                    Label('Enter first restaurant ID:'),
                    Input(type='number', name='restaurant1_id', required=True),
                    Br(),
                    Label('Enter second restaurant ID:'),
                    Input(type='number', name='restaurant2_id', required=True),
                    Br(),
                    Input(type='submit', value='Calculate')
                )
            ),
            Div(id='distance-result'),  # This div will be updated with the server response
            Br(),
            Br(),
            Br(),
            Br(),
            Br(),
            Br(),
            Br(),
            Div(cls='footer')(
                P('© 2024 Gastro Tour Medellin. All rights reserved.')
            )
        )
    )
