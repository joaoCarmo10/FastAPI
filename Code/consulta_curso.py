from fastAPI import fastAPI

app = fastAPI()

cursos = {
    1:{
        "nome": "Dominando o Python",
        "nivel": "básico",
        "formacao": "Python Fundamentos"
    },
    2:{
        "nome": "Automação de tarefas",
        "nivel": "intermediário",
        "formacao": "Automação"
    },
    3:{
        "nome": "Automação com Selenium",
        "nivel": "intermediário",
        "formacao": "Automação"
    }
}

