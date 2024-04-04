'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos'''

def conversorTiempo (minutos):
    horas = minutos/60
    minutos_restantes = int(round((horas-int(horas))*60,0))
    horas=int(horas)
    print (horas,"horas", minutos_restantes,"minutos")

minutos= int(input("Ingrese la cantidad de minutos a convertir: "))

conversorTiempo (minutos)
