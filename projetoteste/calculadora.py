# calculadora.py
def somar(a, b):
    return a + b

print(f"Soma: {somar(10, 5)}")

def divisao(a, b):
    return a / b

print(f"Divisão: {divisao(10, 5)}")

def multiplicacao(a, b):
    return a * b

print(f"Multiplicação: {multiplicacao(10, 5)}")

def subtracao(a, b):
    return a - b

print(f"Subtração: {subtracao(10, 5)}")

# Calculadora Finalizada para o projeto de DevOps
def calculadora(a, b, operacao):
    if operacao == "+": return a + b
    if operacao == "/": return a / b
    if operacao == "*": return a * b
    if operacao == "-": return a - b
