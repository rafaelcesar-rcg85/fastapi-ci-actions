from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "API funcionando com sucesso!"}


@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a - b}

