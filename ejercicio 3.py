'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no. '''

def edadUsuario ():
    edad = input ('Ingrese su edad: ')
    if int(edad) >= 18:
        print('Es mayor de edad')
    else: 
        print ('Es menor de edad')

edadUsuario ()  