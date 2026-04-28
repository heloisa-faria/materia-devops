from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_vogais_simples():
    # testa se foi certo
    response = client.get("/vogais?texto=Python")
    assert response.status_code == 200
    assert "o" in response.json()["apenas_vogais"].lower()

def test_frase_sem_vogais():
    response = client.get("/vogais?texto=bcd")
    assert response.json()["apenas_vogais"] == ""