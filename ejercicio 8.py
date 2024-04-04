'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

def calcularIMC  (peso,altura):
    imc=round(peso/(altura*altura),2)
    print (f"Su índice de masa corporal es : {imc}")

peso = input("Indique su peso en kg: ")
altura= input ("Indique su altura en metros: ") 

calcularIMC (int(peso),float(altura))


