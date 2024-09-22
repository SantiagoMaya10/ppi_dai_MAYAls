from fasthtml.common import FastHTML, serve
from  views.homepage import build_home_page
from  views.signup import build_sign_up_page
import os
from databaseobjects.dbconfig import MySqLConnectionCreator

app = FastHTML()

@app.get("/")
def home():
    return build_home_page()

@app.get("/current-scope")
def get_current_scope():
    return os.getenv("SCOPE")

@app.get("/sign-up")
def sing_up():
    return build_sign_up_page();

@app.post("/create-user")
def create_user():
    return 

@app.get("/is-db-connected")
def test_db_connection():
    connector = MySqLConnectionCreator()
    connection = connector.db_conn
    connector.close_db_connection(connection)
    return "DB connection is succesfull"

serve()
