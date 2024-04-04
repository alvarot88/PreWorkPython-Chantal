'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.'''

def contadorVocales ():

    texto = input('Ingrese una palabra para conocer cuantas vocales tiene: ')
    vocales = "aeiouAEIOU"
    j=0

    for letra in texto :
        if letra in vocales:
            j=j+1

    print(f"La palabra tiene {j} vocales")

contadorVocales ()
