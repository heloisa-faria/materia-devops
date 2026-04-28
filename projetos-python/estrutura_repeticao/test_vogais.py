from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_extrair_vogais_comum():
    response = client.get("/filtrar?frase=DevOps")
    assert response.status_code == 200
    assert "e" in response.json()["vogais_encontradas"].lower()

def test_texto_sem_vogais():
    response = client.get("/filtrar?frase=kjt")
    assert response.status_code == 200
    assert response.json()["vogais_encontradas"] == ""