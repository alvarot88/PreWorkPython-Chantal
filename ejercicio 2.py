'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

def cuentaRestaurant ():
    menuAdulto = 14
    menuNiño = 8
    comensalesAdulto = input ('numero de comensales adultos: ')
    comensalesNiño = input  ('numero de comensales niño: ') 
    
    cuentaRestaurant = menuAdulto * int(comensalesAdulto) + menuNiño * int(comensalesNiño)
    propina= cuentaRestaurant*0.15
    print(f'Total de menú: {cuentaRestaurant}')
    print(f'Total de propina: {propina}')
    print(f'Total Cuenta Restaurant: {cuentaRestaurant+propina}')



cuentaRestaurant()  
    