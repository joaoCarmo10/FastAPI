from fastapi import FastAPI

app = FastAPI()

jogadores = {
    1:{
        "nome":"Dudu",
        "idade":30,
        "time":"Palmeiras"
    },
    2:{
        "nome":"Vinicius Jr",
        "idade":28,
        "time":"Real Madrid"
    },
    3:{
        "nome":"João Pedro",
        "idade":28,
        "time":"Chealsea"
    }
}

#Localhost:8000/

@app.get('/')
def inicio():
    return {"Menssagem": "Olá Mundo!"}

@app.get('/jogadores')
def lista_jogadores():
    return jogadores

#path parameter
@app.get('/busca/jogador/{jogador_id}')
def busca_jogador(jogador_id:int):
    return jogadores[jogador_id]

#Query parameter
@app.get('/busca-jogador-nome')
def busca_jogador_nome(nome:str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]['nome'] == nome:
            return jogadores[jogador_id]
    return {"Dados": "Não foi encontrado nenhum jogador"}