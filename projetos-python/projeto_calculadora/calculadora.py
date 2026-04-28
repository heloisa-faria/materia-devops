
def somar(a, b):
    return a + b

def divisao(a, b):
    if b == 0:
        return "divisão por zero"
    return a / b

def multiplicacao(a, b):
    return a * b

def subtracao(a, b):
    return a - b

def calculadora(a, b, operacao):
    if operacao in ["+", "soma"]: return somar(a, b)
    if operacao in ["-", "subtracao"]: return subtracao(a, b)
    if operacao in ["*", "multiplicacao"]: return multiplicacao(a, b)
    if operacao in ["/", "divisao"]: return divisao(a, b)
