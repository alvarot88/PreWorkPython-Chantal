'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.'''

def ContadorPalabras ():
    oracion = input ("Ingrese una oración: ")
    palabras = oracion.split()
    print(len(palabras))

ContadorPalabras()


