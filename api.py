from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import arquivos_base.functionBD as bd

# Criando API Local
app = FastAPI()

# Criação classe de teste
class Inputs(BaseModel):
    inp: int
    inp2: str

# Rotas testes
@app.get('/exemplo')
def example() -> str:
    bd.create_sala(45)

    return "Sala adicionada!"

@app.post('/exemplo2')
def example_2(inputs:Inputs) -> float:
    
    return 2*inputs.inp/17


if __name__ == "__main__":
    uvicorn.run(app, port=8000)

