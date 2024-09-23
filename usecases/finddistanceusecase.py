from scipy.spatial import distance
from databaseconfig.dbconfig import MySqLConnectionCreator
from fasthtml.common import *

def find_distance_use_case(id_one, id_two):
    connector = MySqLConnectionCreator()
    conn = connector.db_conn

    # First restaurant location query
    cursor = conn.cursor()
    query = "SELECT location_lat, location_lon FROM restaurant WHERE id = %s"
    cursor.execute(query, (id_one,))
    restaurant_one_location = cursor.fetchone()
    cursor.close()

    # Second restaurant location query
    cursor = conn.cursor()
    cursor.execute(query, (id_two,))
    restaurant_two_location = cursor.fetchone()
    cursor.close()

    connector.close_db_connection(conn)

    # Calculate the Manhattan distance using scipy
    distance_between = distance.cityblock(restaurant_one_location, restaurant_two_location)

    # Return the distance wrapped in a Div element
    return Div(f"Manhattan distance between restaurant {id_one} and {id_two}: {distance_between:.2f} units")
