css_scatter_plot = """
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
    }

    .scatter-plot-content {
        text-align: center;
        padding: 40px;
    }

    .scatter-plot-content img {
        max-width: 100%;
        height: auto;
    }

    .scatter-plot-content h2 {
        margin-bottom: 20px;
        font-size: 24px;
    }
         .navbar {
        background-color: #d66767;
        overflow: hidden;
        padding: 10px 20px;
    }

    .navbar a {
        float: right;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
        font-size: 17px;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    .footer {
        background-color: #d66767;
        color: white;
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    """

# CSS para la página
def scatter_page_styles():
    return css_scatter_plot