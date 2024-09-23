from fasthtml.common import FastHTML, serve, Form

from fastapi import Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from views.homepageview import build_home_page
from views.signupview import build_sign_up_page
from views.signinview import build_sign_in_page
from views.finddistanceview import build_find_restaurants_distance_page
from views.contactinfoview import build_about_page

from usecases.saveuser import save_user_info
from usecases.privacypolicy import build_privacy_policy
from usecases.signinusecase import sign_in_user
from usecases.navbarusecase import build_navbar
from usecases.finddistanceusecase import find_distance_use_case
from usecases.createmapusecase import create_map

from databaseconfig.dbconfig import MySqLConnectionCreator



app = FastHTML()

@app.get("/")
def home(request: Request):
    session_user = request.cookies.get("session_user")
    return build_home_page(build_navbar(session_user))

@app.get("/find-distance-page")
def find_distance_page(request: Request):
    session_user = request.cookies.get("session_user")
    return build_find_restaurants_distance_page()

@app.post("/find-distance-restaurants")
async def find_distance_two_restaurants(request: Request):
    form_data = await request.form()  # Access form data
    restaurant1_id = int(form_data['restaurant1_id'])  # Retrieve Restaurant 1 ID
    restaurant2_id = int(form_data['restaurant2_id'])
    return find_distance_use_case(restaurant1_id, restaurant2_id)
    
@app.get("/restaurants-map")
async def get_restaurants_map():
    # Generate the map HTML
    map_html = create_map()
    # Return the map as HTML to the front end
    return HTMLResponse(content=map_html)

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

@app.get("/sign-out")
async def sign_out():
    # Remove the session cookie
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("session_user")  # Deletes the session cookie
    return response

@app.get("/contact-info")
def get_contact_info():
    return build_about_page()

@app.get("/is-db-connected")
def test_db_connection():
    connector = MySqLConnectionCreator()
    connection = connector.db_conn
    connector.close_db_connection(connection)
    return "DB connection is succesfull"

    
serve()
