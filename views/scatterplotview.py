from fasthtml.common import *
from usecases.scatterplotusecase import generate_scatter_plot
from views.styles.scatterplotstyle import scatter_page_styles

# Generar la página que muestra el gráfico
def build_scatter_plot_page():
    # Generar el gráfico scatter
    image_base64 = generate_scatter_plot()

    navbar = Div(cls='navbar')(
        A('Home', href='/')  # Link back to homepage
    )

    footer = Div(cls='footer')(
        P('© 2024 Gastro Tour Medellin. All rights reserved.')
    )

    # Contenido de la página con el gráfico
    scatter_plot_content = Div(cls='scatter-plot-content')(
        H2('Precio vs Rating en Restaurantes de Medellín'),
        Img(src=f"data:image/png;base64,{image_base64}", alt="Scatter plot of price vs rating"),
    )

    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Scatter Plot - Precio vs Rating'),
            Style(scatter_page_styles())
        ),
        Body(
            navbar,
            scatter_plot_content,
            footer
        )
    )



