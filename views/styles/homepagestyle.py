
css= """ body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
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

        .title {
            text-align: center;
            padding: 40px 0;
            background-color: #bb5151;
            color: white;
            font-size: 60px;
            font-weight: bold;

        }

        .functionalities {
            display: flex;
            justify-content: space-around;
            margin: 150px 0;
            padding: 0 100px;
        }

        .functionality {
            background-color: white;
            padding: 20px;
            margin: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 30%;
            text-align: center;
        }

        .functionality h3 {
            margin: 0 0 10px;
        }

        .functionality p {
            color: #666;
        }

        .functionality button {
            padding: 10px 20px;
            background-color: #d66767;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .functionality button:hover {
            background-color: #924f4f;
        } """

def home_page_styles():
    return css

