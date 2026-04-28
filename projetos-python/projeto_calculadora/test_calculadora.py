from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_soma():
    assert client.get("/calcular?a=10&b=5&operacao=soma").json()["resultado"] == 15

def test_subtracao():
    assert client.get("/calcular?a=10&b=5&operacao=subtracao").json()["resultado"] == 5

def test_multiplicacao():
    assert client.get("/calcular?a=10&b=5&operacao=multiplicacao").json()["resultado"] == 50