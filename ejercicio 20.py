'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario.'''

def sumar_lista_numeros(numeros):

    suma = 0
    for numero in numeros:
        suma += numero
    return suma


numeros = input("Ingrese una lista de números separados por espacios: ")

lista_numeros = [int(x) for x in numeros.split()]

resultado = sumar_lista_numeros(lista_numeros)

print("La suma de los números en la lista es:", resultado)


