'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.'''

def Calcudesc (precio):
    descuento = precio*0.20
    precioFinal = precio - descuento
    print (precioFinal)

precio= int(input("Ingrese un precio: "))

Calcudesc (precio)
    
    