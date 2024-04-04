'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

def Diadelasemana (numero):
    if numero==1:
        print ("lunes")
    elif numero==2:
        print ("martes")
    elif numero ==3:
        print ("miercoles")
    elif numero==4:
        print ("jueves")
    elif numero ==5:
        print ("viernes")
    elif numero ==6:
        print ("sabado")
    elif numero ==7:
        print ("domingo")
    else: 
        print ("el número ingresado no corresponde a un día de la semana")

numero= int (input ("Ingrese un número del 1 al 7: ")) 

Diadelasemana (numero)