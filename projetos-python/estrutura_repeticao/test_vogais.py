from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_extrair_vogais_comum():
    response = client.get("/vogais?texto=DevOps")
    assert "e" in response.json()["apenas_vogais"].lower()

def test_texto_sem_vogais():
    response = client.get("/vogais?texto=kjt")
    assert response.json()["apenas_vogais"] == ""