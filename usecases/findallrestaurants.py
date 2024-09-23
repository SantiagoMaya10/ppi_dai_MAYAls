from databaseconfig.dbconfig import MySqLConnectionCreator

def find_all_restaurants():
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, location_lat, location_lon, address FROM restaurant")
    restaurants = cursor.fetchall()
    cursor.close()

    connector.close_db_connection(conn)

    return restaurants