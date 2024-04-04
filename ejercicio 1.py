'''Ejercicio 1: Conversor de Temperatura 
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.'''

def conversor():
    temp = input ('Ingrese la temperatura en grados celsius: ')
  
    temp_conv = int(temp) * (9/5) + 32
    print (f'{temp}°c es equivalente a {temp_conv}° F')

conversor ()