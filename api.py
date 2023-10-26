from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Inputs(BaseModel):
    inp: int
    inp2: str

@app.get('/exemplo')
def example() -> str:
    return "Olá mundo!"

@app.post('/exemplo2')
def example_2(inputs:Inputs) -> float:
    
    return 2*inputs.inp/17
 
if __name__ == "__main__":
    uvicorn.run(app, port=8000)

