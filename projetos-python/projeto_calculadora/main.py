from fastapi import FastAPI
from calculadora import calculadora

app = FastAPI()

@app.get("/")
async def rota_inicial():
    return {"status": "API da Calculadora Online", "instrucao": "Use a rota /calcular"}

@app.get("/calcular")
async def rodar_calculo(a: float, b: float, operacao: str):
    resultado = calculadora(a, b, operacao)
    return {
        "numero_1": a,
        "numero_2": b,
        "operacao": operacao,
        "resultado": resultado
    }