from fasthtml.common import *
from views.styles.updatepasswordstyle import update_password_style

def build_change_password_page():
    navbar = Div(cls='navbar')(
        A('Home', href='/')  # Link back to homepage
    )

    footer = Div(cls='footer')(
        P('© 2024. All rights reserved.')
    )

    password_change_form = Div(cls='password-change-form')(
        H2('Change Password'),
        Form(action='/update-password', method='POST')(
            Label('New Password:'),
            Input(type='password', name='new_password', required=True),
            Br(),
            Input(type='submit', value='Update Password')
        )
    )

    return Html(
        Head(
            Meta(charset='UTF-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Title('Change Password'),
            Style(update_password_style())
        ),
        Body(
            navbar,
            password_change_form,
            footer
        )
    )