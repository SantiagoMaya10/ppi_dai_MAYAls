from fasthtml.common import FastHTML, serve, Form
from  views.homepage import build_home_page
from  views.signup import build_sign_up_page
from views.signin import build_sign_in_page
from databaseconfig.dbconfig import MySqLConnectionCreator
from usecases.saveuser import save_user_info
from usecases.privacypolicy import build_privacy_policy
from usecases.signinusecase import sign_in_user
from usecases.navbarusecase import build_navbar
from fastapi import Request



app = FastHTML()

@app.get("/")
def home(request: Request):
    session_user = request.cookies.get("session_user")
    return build_home_page(build_navbar(session_user))

@app.get("/sign-up")
def sing_up():
    return build_sign_up_page();

@app.post("/create-user")
def create_user(
    name: str = Form(...),
    lastname: str = Form(...),
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    privacy_policy: bool = Form(...)
):
    return save_user_info(name, lastname, email, username, password, privacy_policy)


@app.get("/sign-in-page")
def sign_in_page():
    return build_sign_in_page()

@app.post("/log-in-user-logic")
def sign_in(
    username: str = Form(...),
    password: str = Form(...)):

    return sign_in_user(username, password)
    
@app.get("/privacy-policy")
def get_privacy_policy():
    return build_privacy_policy()


@app.get("/is-db-connected")
def test_db_connection():
    connector = MySqLConnectionCreator()
    connection = connector.db_conn
    connector.close_db_connection(connection)
    return "DB connection is succesfull"

    
serve()
