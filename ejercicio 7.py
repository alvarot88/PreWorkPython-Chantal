'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.'''

def suma (valorA,valorB):
    resultado = int(valorA) + int(valorB)
    print (resultado)

def resta (valorA,valorB):
    resultado = int(valorA) - int(valorB)
    print (resultado)

def multiplicacion (valorA, valorB):
    resultado = int(valorA) * int(valorB)
    print (resultado)

def division (valorA, valorB):
    resultado = int(valorA) / int(valorB)
    print (resultado)

valorA = input ("Ingrese un número: ")
valorB = input ("Ingrese un número: ")
operacion = input("Indique la operacion a realizar: ")

if operacion.lower() in "suma, +":
    suma(valorA,valorB)

if operacion.lower()in "resta, -":
    resta(valorA,valorB)

if operacion.lower() in "multiplicación, multiplicacion, *":
    multiplicacion (valorA,valorB)

if operacion.lower () in "division, división, /":
    division (valorA, valorB) 



