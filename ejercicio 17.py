'''Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.'''

def conversorMillasaKM():
    millas = input ('ingrese la distancia en millas para convertirla en kilometros: ')

    kilometros = int(millas) * 1.60934
    print (f'{millas} millas es equivalente a {kilometros} kilometros')

conversorMillasaKM ()