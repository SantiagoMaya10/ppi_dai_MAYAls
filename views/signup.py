from fasthtml.common import *
from views.styles.signupstyle import sign_up_styles
from views.jsbehaviour.signupscripts import sign_up_js_scripts

def build_sign_up_page():

    return Html(lang='en')(
            Head(
                Meta(charset='UTF-8'),
                Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
                Title('Sign Up'),
                Style(sign_up_styles()),
                Script(src='https://unpkg.com/htmx.org')
            ),
            Body(
                Div(cls='container')(
                    H2('Sign Up'),
                    Form(hx_post='/create-user', hx_on='htmx:afterRequest: redirectToSignIn()', hx_target='.message', hx_swap='outerHTML')(
                        Label('First Name:', fr='name'),
                        Input(type='text', id='name', name='name', required=''),
                        Label('Last Name:', fr='lastname'),
                        Input(type='text', id='lastname', name='lastname', required=''),
                        Label('Email:', fr='email'),
                        Input(type='email', id='email', name='email', required=''),
                        Label('Username:', fr='username'),
                        Input(type='text', id='username', name='username', required=''),
                        Label('Password:', fr='password'),
                        Input(type='password', id='password', name='password', required=''),
                        Div(cls='checkbox-container')(
                            Input(type='checkbox', id='privacy_policy', name='privacy_policy', required=''),
                            Label(fr='privacy_policy')(
                                'I agree to the',
                                A('Privacy Policy', href='/privacy-policy', target='_blank'),
                                'and Personal Information Treatment'
                            )
                        ),
                        Input(type='submit', id='register-btn', value='Register', disabled='')
                    ),
                    Div(cls='message')
                ),
                Script(sign_up_js_scripts())
            )
        )