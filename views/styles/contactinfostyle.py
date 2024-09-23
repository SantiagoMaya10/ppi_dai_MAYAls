contact_info_css = """
body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
    }

    .about-content {
        text-align: center;
        padding: 40px;
        margin: 20px auto;
        width: 80%;
    }

    .title {
        text-align: center;
        padding: 40px 0;
        background-color: #bb5151;
        color: white;
        font-size: 60px;
        font-weight: bold;
    }

    .functionality {
        background-color: white;
        padding: 20px;
        margin: 10px auto;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 50%;
        text-align: center;
    }

    .functionality p {
        color: #666;
        font-size: 18px;
        margin: 10px 0;
    }

    .functionality a {
        color: #d66767;
        text-decoration: none;
        font-weight: bold;
    }

    .functionality a:hover {
        color: #924f4f;
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

def contact_info_style():
    return contact_info_css