"""Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
cateto_1= float(input("Dime la longitud de un cateto en cm: "))
cateto_2= float(input("Dime la longitud del otro cateto: "))
resultado_operacion= (cateto_1 **2) + (cateto_2 ** 2)
resultado_operacion

"""Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""
grado_Celsius= float(input("Dime cuantos grados hace: "))
grado_Fahrenheit= (grado_Celsius * (9/5)) + 32
print(grado_Fahrenheit)

"""Calcular la media de tres números pedidos por teclado"""
numero_1= float(input("Dime un número: "))
numero_2= float(input("Dime un número: "))
numero_3= float(input("Dime un número: "))
media_numero= ((numero_1 + numero_2 + numero_3) / 3)
print(media_numero)

"""Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra"""
precio_compra= float(input("Dime cuanto te ha costado la compra: "))
precio_descuento= precio_compra * 0.15
precio_final= precio_compra - precio_descuento
print(precio_final)

"""Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)"""
numero_1= float(input("Dime un número: "))
numero_2= float(input("Dime otro numero: "))
distancia_numeros= numero_1 - numero_2
if distancia_numeros >= 0:
    print(distancia_numeros)
elif distancia_numeros < 0:
    distancia_numeros: -(distancia_numeros)
    print(distancia_numeros)
else:
    print("Esta distancia no existe")