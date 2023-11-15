from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import arquivos_base.functionBD as bd

# Criando API Local
app = FastAPI()

# Criação classe de teste
class Inputs(BaseModel):
    id_sala: int
    capacidade: int

# Rotas testes
@app.get('/exemplo')
def example() -> str:
    bd.create_sala(6, 45)

    return "Sala adicionada!"

@app.post('/exemplo2')
def example_2(inputs:Inputs) -> str:
    bd.create_sala(inputs.id_sala, inputs.capacidade)
    return "Sala adicionada com sucesso!"

@app.get('/atualizarCSV')
def example() -> str:
    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\agenda.csv'
    table_name = 'agenda'
    bd.update_csv_from_database(file_path, table_name)

    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\sala.csv'
    table_name = 'sala'
    bd.update_csv_from_database(file_path, table_name)

    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\disciplina.csv'
    table_name = 'disciplina'
    bd.update_csv_from_database(file_path, table_name)

    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\turma.csv'
    table_name = 'turma'
    bd.update_csv_from_database(file_path, table_name)

    return "arquivos .csv atualizados!"

@app.get('/atualizarBD')
def example() -> str:
    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\sala.csv'
    table_name = 'sala'
    bd.update_database_from_csv(file_path, table_name)

    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\disciplina.csv'
    table_name = 'disciplina'
    bd.update_database_from_csv(file_path, table_name)

    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\turma.csv'
    table_name = 'turma'
    bd.update_database_from_csv(file_path, table_name)
    
    file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\agenda.csv'
    table_name = 'agenda'
    bd.update_database_from_csv(file_path, table_name)

    return "Banco de dados atualizado com sucesso!"

if __name__ == "__main__":
    uvicorn.run(app, port=8000)

# Configurações do seu banco de dados
# Caminho para o arquivo .csv que você deseja atualizar
#file_path = 'C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\agenda.csv'

# Nome da tabela que você deseja exportar/importar do banco de dados
#table_name = 'agenda'

# Chamar a função
#bd.update_csv_from_database(file_path, table_name)
#bd.update_database_from_csv(file_path, table_name)