'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.'''

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número {} es par.".format(numero)
    else:
        return "El número {} es impar.".format(numero)

numero = int(input ("Indique un número para saber si es par o impar: "))
print (es_par_o_impar(numero))

