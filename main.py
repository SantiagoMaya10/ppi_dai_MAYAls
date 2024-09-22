from fasthtml.common import FastHTML, serve, HTMLResponse, Form, Div, Head, Html,Body
from  views.homepage import build_home_page
from  views.signup import build_sign_up_page
import os
from databaseconfig.dbconfig import MySqLConnectionCreator

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

@app.get("/is-db-connected")
def test_db_connection():
    connector = MySqLConnectionCreator()
    connection = connector.db_conn
    connector.close_db_connection(connection)
    return "DB connection is succesfull"

@app.post("/create-user")
async def create_user(
    name: str = Form(...),
    lastname: str = Form(...),
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    session_active: bool = Form(...),
    privacy_policy: bool = Form(...)
):
    # Process the user registration (e.g., save to the database)
    print(name)
    print(lastname)
    print(email)
    print(username)
    print(password)
    print(privacy_policy)

    
    # Respond with a success message
    message = Div(
        f"User {username} successfully registered! Redirecting to sign-in...",
        cls="message"
    )
    
    return Html(
        Head(),
        Body(
            message
        )
    )
serve()
