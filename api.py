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

# Configurações do seu banco de dados
# Caminho para o arquivo .csv que você deseja atualizar
file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\agenda.csv'

# Nome da tabela que você deseja exportar/importar do banco de dados
table_name = 'agenda'

# Chamar a função
bd.update_csv_from_database(file_path, table_name)
#bd.update_database_from_csv(file_path, table_name)