from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Home route to show the form
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("cold_form.html", {"request": request})

# Process the form data
@app.post("/submit", response_class=HTMLResponse)
def submit_form(request: Request, q1: str = Form(...), q2: str = Form(...), q3: str = Form(...), q4: str = Form(...), q5: str = Form(...)):
    answers = [q1, q2, q3, q4, q5]
    yes_count = sum(1 for answer in answers if answer.lower() == "yes")
    
    if yes_count >= 3:
        result = "You might have a cold! 🤒"
    else:
        result = "You probably don't have a cold! 😊"

    return templates.TemplateResponse("result.html", {"request": request, "result": result})
