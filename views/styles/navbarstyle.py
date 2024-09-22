
navbar_css = """
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

    /* Dropdown container */
    .dropdown {
        float: right;
        overflow: hidden;
    }

    /* Dropdown button */
    .dropdown .dropbtn {
        color: #f2f2f2;
        padding: 14px 16px;
        font-size: 17px;
        border: none;
        cursor: pointer;
        background-color: inherit;
        text-decoration: none;
    }

    .dropdown:hover .dropbtn {
        background-color: #ddd;
        color: black;
    }

    /* Dropdown content (hidden by default) */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        right: 0; /* Align to the right side */
    }

    /* Links inside the dropdown */
    .dropdown-content a {
        float: none;
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        text-align: left;
    }

    /* Change color of dropdown links on hover */
    .dropdown-content a:hover {
        background-color: #ddd;
        color: black;
    }

    /* Show the dropdown on hover */
    .dropdown:hover .dropdown-content {
        display: block;
    }
"""

def navbar_style():
    return navbar_css