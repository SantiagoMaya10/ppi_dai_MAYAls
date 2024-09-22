from fasthtml.common import *
from views.styles.signupstyle import sign_up_styles

def build_sign_up_page():

    return Html(lang='en')(
            Head(
                Meta(charset='UTF-8'),
                Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
                Title('Sign Up'),
                Style('body {\r\n            font-family: Arial, sans-serif;\r\n            margin: 0;\r\n            padding: 20px;\r\n            background-color: #f4f4f4;\r\n        }\r\n        .container {\r\n            max-width: 400px;\r\n            margin: 0 auto;\r\n            padding: 20px;\r\n            background-color: white;\r\n            border-radius: 5px;\r\n            box-shadow: 0 0 10px rgba(0,0,0,0.1);\r\n        }\r\n        input[type="text"], input[type="email"], input[type="password"] {\r\n            width: 100%;\r\n            padding: 10px;\r\n            margin: 10px 0;\r\n            border: 1px solid #ccc;\r\n            border-radius: 4px;\r\n        }\r\n        input[type="submit"] {\r\n            background-color: #28a745;\r\n            color: white;\r\n            padding: 10px;\r\n            border: none;\r\n            border-radius: 4px;\r\n            cursor: pointer;\r\n            margin-top: 10px;\r\n        }\r\n        input[type="submit"]:hover {\r\n            background-color: #218838;\r\n        }\r\n        .checkbox-container {\r\n            display: flex;\r\n            align-items: center;\r\n            margin-top: 10px;\r\n        }\r\n        .checkbox-container input {\r\n            margin-right: 10px;\r\n        }\r\n        #register-btn:disabled {\r\n            background-color: #cccccc;\r\n            cursor: not-allowed;\r\n        }\r\n        .message {\r\n            margin-top: 20px;\r\n            font-size: 14px;\r\n        }'),
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
                            Input(type='checkbox', id='session_active', name='session_active'),
                            Label('Keep me signed in', fr='session_active')
                        ),
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
                Script("// Enable register button only when privacy policy is checked\r\n        document.getElementById('privacy_policy').addEventListener('change', function() {\r\n            document.getElementById('register-btn').disabled = !this.checked;\r\n        });\r\n\r\n        // Function to redirect to the sign-in page after successful registration\r\n        function redirectToSignIn() {\r\n            setTimeout(function() {\r\n                window.location.href = '/sign-in';\r\n            }, 1000); // 1-second delay before redirect\r\n        }")
            )
        )