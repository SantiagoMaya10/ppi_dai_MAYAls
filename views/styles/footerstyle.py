
css = """
body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .footer {
            background-color: #bb5151;
            color: white;
            padding: 10px;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #f2f2f2;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .footer p {
            margin: 10px 0;
        }
        .footer .social-icons {
            margin: 10px 0;
        }
        .footer .social-icons a {
            margin: 0 10px;
            display: inline-block;
            color: #f2f2f2;
            font-size: 24px;
            text-decoration: none;
            text-decoration: underline;

        }
        .footer .social-icons a:hover {
            color: #ddd;
        }"""

def site_footer():
    return css