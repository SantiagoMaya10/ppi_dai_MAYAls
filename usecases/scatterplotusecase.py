import matplotlib.pyplot as plt
from io import BytesIO
import base64
from databaseconfig.dbconfig import MySqLConnectionCreator
import matplotlib

# Establish 'Agg' (Anti-Grain Geometry) backend attribute
# to avoid GUI problems. It is a noninteractive backend
# since we dont want to render the plots in backned,
# just create a file to render in front end
matplotlib.use('Agg')

def generate_scatter_plot():
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()
    
    query = """SELECT name, average_price_usd, visitors_average_rating
               FROM restaurant
               WHERE average_price_usd IS NOT NULL
               AND visitors_average_rating IS NOT NULL
            """
    cursor.execute(query)
    # Fetch results as tuples
    restaurants = cursor.fetchall()  
    cursor.close()
    connector.close_db_connection(conn)
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(25, 10))

    # Extraer datos de los restaurantes (usando índices de tupla)
    prices = [restaurant[1] for restaurant in restaurants]  # Índice 1 para `average_price_usd`
    ratings = [restaurant[2] for restaurant in restaurants]  # Índice 2 para `visitors_average_rating`
    names = [restaurant[0] for restaurant in restaurants]    # Índice 0 para `name`

    # Crear el scatter plot
    scatter = ax.scatter(prices, ratings)

    # Etiquetas para cada punto
    for i, name in enumerate(names):
        ax.annotate(name, (prices[i], ratings[i]), textcoords="offset points", xytext=(0, 10), ha='center', rotation=90)

    # Etiquetas de los ejes
    ax.set_xlabel('Precio (USD)')
    ax.set_ylabel('Rating de Visitantes')
    ax.set_title('Precio vs Rating en Restaurantes de Medellín')

    # Guardar gráfico como imagen en base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    return image_base64
