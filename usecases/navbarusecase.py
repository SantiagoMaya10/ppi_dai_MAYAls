from fasthtml.common import Div, A

def build_navbar(session_user=None):
    if session_user:
        # Display username with a dropdown for profile and logout
        return Div(
            Div(
                A(f'{session_user}', href='#', cls='dropbtn'),
                Div(
                    A('update-password', href='/update-password-page'),
                    A('Log Out', href='/sign-out'),
                    cls='dropdown-content'
                ),
                cls='dropdown'
            ),
            cls='navbar'
        )
    else:
        # Show Login and Sign Up links if user is not logged in
        return Div(
            A('Login', href='/sign-in-page'),
            A('Sign Up', href='/sign-up'),
            cls='navbar'
        )