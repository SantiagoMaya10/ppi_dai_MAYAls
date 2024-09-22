from fasthtml.common import Main, FastHTML, H1, P, A, Form, Button, serve, Title
from databaseobjects.dbconfig import SqLiteConnector
from  views.homepage import build_home_page
import os

app = FastHTML()

@app.get("/")
def home():
    return build_home_page()

@app.get("/dummy")
def increment():

    db_conf = SqLiteConnector()
    conn = db_conf.get_db_connection()
    with conn:
        data = conn.cursor().execute("select * from ping")

    return P(data.fetchone())

@app.get("/current-scope")
def getCurrentScope():
    return os.getenv("SCOPE")


serve()
