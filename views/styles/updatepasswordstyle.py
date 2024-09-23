css_update_pssw = """
body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
    }

    .password-change-form {
        max-width: 400px;
        margin: 50px auto;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .password-change-form h2 {
        text-align: center;
        margin-bottom: 20px;
    }

    .password-change-form label {
        display: block;
        margin: 10px 0 5px;
        font-weight: bold;
    }

    .password-change-form input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }

    .password-change-form input[type="submit"] {
        width: 100%;
        padding: 10px;
        background-color: #d66767;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .password-change-form input[type="submit"]:hover {
        background-color: #924f4f;
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

def update_password_style():
    return css_update_pssw