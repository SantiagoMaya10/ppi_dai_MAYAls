from fasthtml.common import Main, FastHTML, H1, P, A, Form, Button, Input, serve, Title

app = FastHTML()

count = 0

@app.get("/")
def home():
    return Title("Count Demo"), Main(
        H1("Count Demo"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="beforebegin")
    )

@app.post("/increment")
def increment():
    print("incrementing")
    global count
    count += 1
    return P(f"Count is set to {count}")

serve()