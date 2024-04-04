'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que 
de derecha a izquierda).'''

def veriPalindromo (palabra):
   
    palabra = palabra.lower ()

    return palabra == palabra [::-1]

palabra = input ('Ingrese la palabra para comprobar si es un palíndromo: ')

if veriPalindromo(palabra):
    print("Es palindromo")
else:
    print("No es palindromo")


# Podría simplificarse solo si quitamos el if y el else , arrojando solo true o false.



