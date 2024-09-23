find_distance_css= """
html, body {
    height: 100%;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.restaurant-table-container {
    flex: 1; /* Allow the container to expand and take up available space */
    overflow-y: auto;
}

.restaurant-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.restaurant-table th, .restaurant-table td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: left;
}

.restaurant-table th {
    background-color: #f2f2f2;
    font-weight: bold;
}

.restaurant-table td {
    background-color: #fff;
}

.restaurant-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

.compare-section {
    margin-top: 20px;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
}

footer {
    text-align: center;
    padding: 10px;
    background-color: #f2f2f2;
    position: relative;
    width: 100%;
    bottom: 0;
}

"""

def find_distance_style():
    return find_distance_css