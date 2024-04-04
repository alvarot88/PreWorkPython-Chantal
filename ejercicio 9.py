'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.'''

def Conversordivisas (dolares):
    conversion= (dolares)*0.85
    print (conversion)

dolares = int(input ("¿Cuantos dolares quiere cambiar?: "))

Conversordivisas (dolares)
