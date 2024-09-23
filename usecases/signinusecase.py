from databaseconfig.dbconfig import MySqLConnectionCreator
from mysql.connector import Error
from fastapi.responses import RedirectResponse
from views.signinview import build_sign_in_page
from fasthtml.common import Div



def sign_in_user(username: str, password: str):
        # Verify the user credentials
    user = _verify_user_exists(username, password)

    if user:
        # Set a session cookie with the username (or user ID)
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_user", value=username, httponly=True)

        # Redirect to home page if successful
        return response

    else:
        # Invalid credentials, display an error message
        return build_sign_in_page(Div(("Invalid username or password! Please try again."), cls="message"))
          


def _verify_user_exists(username: str, password: str):
    connector= MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()
    try:
        
        query = """
                SELECT * FROM user WHERE username = %s AND password = %s
            """
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        return user  # Return user data if found, otherwise None
    except Error as e:
        print(f"Error fetching user: {e}")
        return None
    finally:
        connector.close_db_connection(conn)