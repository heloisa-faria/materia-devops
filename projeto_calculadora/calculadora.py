
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

# Calculadora Finalizada para o projeto de DevOps
def calculadora(a, b, operacao):
    if operacao == "+": return somar(a,b)
    if operacao == "/": return divisao(a, b)
    if operacao == "*": return multiplicacao(a, b)
    if operacao == "-": return subtracao(a, b)
