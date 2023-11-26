from fastapi import FastAPI

app = FastAPI()

#Localhost:8000/

@app.get('/')
def inicio():
    return {"Menssagem": "Olá Mundo!"}