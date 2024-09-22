from fasthtml.common import FastHTML, serve
from  views.homepage import build_home_page
import os

app = FastHTML()

@app.get("/")
def home():
    return build_home_page()

@app.get("/current-scope")
def getCurrentScope():
    return os.getenv("SCOPE")


serve()
