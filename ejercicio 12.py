'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.'''

def CalcularArea (longitud,ancho):
    area=longitud*ancho
    print (area)

longitud= int(input("Ingrese la longitud del rectángulo: "))
ancho= int(input("Ingrese el ancho del rectángulo: "))

CalcularArea (longitud,ancho)




