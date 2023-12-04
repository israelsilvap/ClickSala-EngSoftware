from utilitarios.algoritmoAlocacao import alocarTurmas
from fastapi.middleware.cors import CORSMiddleware
from database.classBD import BancoDeDados
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

bd = BancoDeDados.getInstance()

# Criando API Local
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Permite todas as origens
    allow_credentials=True,  # Permite cookies serem enviados com a solicitação
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Criação classe de teste
class ModelLocal(BaseModel):
    Nome: str
    Capacidade: int

class ModelDocente(BaseModel):
    Nome_Docente: str
    dias: list
    horarios: list

class ModelDisciplina(BaseModel):
    Nome_Disciplina: str
    Tipo: str
    Periodo: int

class ModelTurma(BaseModel):
    Nome_Disciplina: str
    Nome_Docente: str
    Num_Alunos: int
    Dias_Aula: str
    Horario_Aulas: str

#INSERIR DADOS NO BANCO DE DADOS
@app.post('/inserirLocal')
def inserirLocal(inputs:ModelLocal) -> str:
    if bd.inserirLocal(inputs.Nome, inputs.Capacidade):
        return "Sala adicionada com sucesso!"
    else:
        return "Erro"

@app.post('/inserirDocente')
def inserirDocente(inputs:ModelDocente) -> str:
    if bd.inserirDocente(inputs.Nome_Docente, inputs.dias, inputs.horarios):
        return "Docente adicionado com sucesso!"
    else:
        "Erro"

@app.post('/inserirDisciplina')
def inserirDisciplina(inputs:ModelDisciplina) -> str:
    if bd.inserirDisciplina(inputs.Nome_Disciplina, inputs.Tipo, inputs.Periodo):
        return "Disciplina adicionado com sucesso!"
    else:
        return "Erro"
    
@app.post('/inserirTurma')
def inserirTurma(inputs:ModelTurma) -> str:
    if bd.inserirTurma(inputs.Nome_Disciplina, inputs.Nome_Docente, inputs.Num_Alunos, inputs.Dias_Aula, inputs.Horario_Aulas):
        return "Turma adicionado com sucesso!"
    else:
        return "Erro"

#PEGAR DADOS NO BANCO DE DADOS
@app.get('/exibirSala/{Nome_Sala}')
def exibirSala(Nome_Sala: str):
    salas = bd.createSalaFromDB()
    for sala in salas:
        if sala.Nome == Nome_Sala:
            return sala.exibir_sala()
    return {"error": "Sala não encontrada"}

@app.get('/exibirTodasAsSalas')
def exibirTodasAsSalas():
    salas = bd.createSalaFromDB()
    salas_dict = {}
    for sala in salas:
        salas_dict[sala.Nome] = sala.exibir_sala()
    return salas_dict

@app.get('/gerarAlocacao')
def gerarAlocacao():
    alocarTurmas(bd)
    return "OK!"

@app.get('/reseteHorarios')
def reseteHorarios():
    bd.reseteHorarios()
    return "OK!"

@app.get('/resetarSala/{Nome_Sala}')
def resetarSala(Nome_Sala: str):
    bd.resetarSala(Nome_Sala)
    return "OK!"

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)