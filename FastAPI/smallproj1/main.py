from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Set up Jinja2 templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_data(request: Request, option: str = Form(...), answer: int = Form(...)):
    if answer == 90:
        result = f"Yes, you have the disease related to {option}."
    else:
        result = "No, you do not have the disease."
    return templates.TemplateResponse("index.html", {"request": request, "result": result, "option": option})
