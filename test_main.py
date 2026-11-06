from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_raiz():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API funcionando com sucesso!"}


def test_somar():
    response = client.get("/somar/2/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_multiplicar():
    response = client.get("/multiplicar/2/2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 4} 
     # Falha intencional: 2 * 2 = 4, não 5
