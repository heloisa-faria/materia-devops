from fastapi import FastAPI
from vogais import informar_vogais  

app = FastAPI()

@app.get("/")
async def inicio():
    return {"projeto": "Filtro de Vogais", "status": "Operacional"}

@app.get("/filtrar")
async def filtrar(frase: str):
    # API recebe o texto pela URL e manda para a logica
    resultado = informar_vogais(frase)
    return {
        "entrada": frase,
        "vogais_encontradas": resultado,
        "total": len(resultado)
    }