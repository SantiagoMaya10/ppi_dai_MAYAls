from fasthtml.common import *  # Import FastHTML components for building HTML elements
from usecases.scatterplotusecase import generate_scatter_plot  # Import the function to generate the scatter plot image
from views.styles.scatterplotstyle import scatter_page_styles  # Import CSS styles specific to the scatter plot page

# Generar la página que muestra el gráfico
def build_scatter_plot_page():
    """
    Builds the 'Scatter Plot - Precio vs Rating' page displaying a scatter plot of restaurant prices versus user ratings.

    The page includes:
    - A navbar with a link back to the homepage.
    - A main content section that displays the scatter plot image.
    - A footer with copyright information.

    The scatter plot image is generated by fetching data from the database, creating the plot,
    encoding it in base64, and embedding it directly into the HTML as an image source.

    Returns:
        Html: The HTML structure for the scatter plot page.
    """
    # Generar el gráfico scatter
    image_base64 = generate_scatter_plot()  # Generate the scatter plot and encode it in base64

    # Create the navbar with a link to the homepage
    navbar = Div(cls='navbar')(
        A('Home', href='/')  # Link back to homepage
    )

    # Create the footer with copyright information
    footer = Div(cls='footer')(
        P('© 2024 Gastro Tour Medellin. All rights reserved.')  # Footer text
    )

    # Contenido de la página con el gráfico
    scatter_plot_content = Div(cls='scatter-plot-content')(
        H2('Precio vs Rating en Restaurantes de Medellín'),  # Page heading
        Img(src=f"data:image/png;base64,{image_base64}", alt="Scatter plot of price vs rating"),  # Embed the scatter plot image
    )

    # Build and return the complete HTML structure
    return Html(
        Head(
            Meta(charset='UTF-8'),  # Meta tag for character encoding
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),  # Meta tag for responsive design
            Title('Scatter Plot - Precio vs Rating'),  # Page title
            Style(scatter_page_styles())  # Include the scatter plot specific CSS styles
        ),
        Body(
            navbar,  # Navbar section
            scatter_plot_content,  # Main content section with the scatter plot
            footer  # Footer section
        )
    )