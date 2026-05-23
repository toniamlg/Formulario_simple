from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/ingresar")
def ingresar(usuario: str = Form(), contraseña: str = Form()):

    if contraseña == "1234":

        return HTMLResponse(
            f"<h1>Bienvenido {usuario}</h1>"
        )

    return RedirectResponse(
        url="/",
        status_code=302
    )