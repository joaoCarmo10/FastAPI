from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# localhost:8000/
@app.get('/')
async def index(request: Request, usuario: str = "João Pedro"):
    context = {
        "request": request,
        "usuario": usuario
    }
    
    return templates.TemplateResponse ('index.html', context=context)

@app.get('/servicos')
async def servicos(request: Request):
    context = {
        "request": request,
    }
    
    return templates.TemplateResponse ('servicos.html', context=context)