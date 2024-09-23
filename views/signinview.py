from fasthtml.common import *
from views.styles.signinstyle import sign_in_style

def build_sign_in_page(login_message = Div()):
    return Html(lang='en')(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Sign In'),
            Style(sign_in_style()),
        ),
        Body(
            Div(cls='container')(
                H2('Sign In'),
                Form(action='/log-in-user-logic', method="POST")(
                    Label('Username:', fr='username'),
                    Input(type='text', id='username', name='username', required=''),
                    Label('Password:', fr='password'),
                    Input(type='password', id='password', name='password', required=''),
                    Input(type='submit', value='Sign In'),
                    A("Don't have an account? Sign up here", href='/sign-up')
                ),
                login_message
            )
        )
    )
