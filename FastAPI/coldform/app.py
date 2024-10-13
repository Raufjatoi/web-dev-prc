from fastapi import FastAPI, Form, Request 
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("cold_form.html", {"request":request})

@app.get("/diabeties", response_class=HTMLResponse)
def dia(request:Request):
    return templates.TemplateResponse("diabeties.html", {"request":request})

@app.post("/submit",response_class=HTMLResponse)
def submit_form(request: Request, q1: str = Form(...), q2: str = Form(...), q3: str = Form(...), q4: str = Form(...), q5: str = Form(...)):
    answers = [q1, q2, q3, q4, q5]
    yes_count = sum(1 for answers in answers if answers.lower() == "yes")

    if yes_count >= 3:
        result = "you might have a cold! 🤒"
    else:
        result = "you probably dont have cold!"
    
    return templates.TemplateResponse("result.html", {"request":request , "result": result})

@app.post("/submit_diabeties",response_class=HTMLResponse)
def submit_form(request: Request, q1: str = Form(...), q2: str = Form(...), q3: str = Form(...), q4: str = Form(...), q5 : str = Form(...)):
    answers = [q1, q2, q3, q4, q5]
    yes_count = sum(1 for answers in answers if answers.lower() == "yes")

    if yes_count >= 3:
        result = "yes you might have a diabeties! 😓"
    else:
        result = "you probably dont have diabeties!"
    return templates.TemplateResponse("result.html", {"request" : request , "result": result})