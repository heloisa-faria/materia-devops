def informar_vogais(texto):
    VOGAIS = "AEIOU"
    resultado = ""
    for letra in texto:
        if letra.upper() in VOGAIS:
            resultado += letra
    return resultado