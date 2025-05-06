def somarnumeros(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

numeros = [8, 12, 28, 10, 6]  
resultado = somarnumeros(numeros)
print(resultado)
