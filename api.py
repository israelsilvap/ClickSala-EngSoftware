from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from backend_ClickSalas.database.classBD import BancoDeDados

bd = BancoDeDados()

# Criando API Local
app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app, port=8000)