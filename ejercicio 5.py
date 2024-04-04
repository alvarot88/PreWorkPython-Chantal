'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

x = 1
suma=0
while x <= 100:
    if x % 2 == 0:
        suma= suma + x
    x = x + 1
    
print (f"La suma de todos los numeros pares del 1 al 100 es: {suma}")

