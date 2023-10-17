#Realizar un programa que lea un número entero por teclado e informe de si el número es par o impar (el cero se considera par)
numero= int(input("Dime un número: "))

if numero % 2 == 0:

    print("Este número es par")

else:
    
    print("Este número es impar")


#Realizar un programa que solicite dos números por teclado e imprima en pantalla si son iguales, el primero mayor que el segundo o el primero más pequeño que el segundo 
numero_1= int(input("Dime un número: "))
numero_2= int(input("Dime otro número: "))

if numero_1 == numero_2:
    print("Estos número son iguales")

elif numero_1 > numero_2:
    print("El primer número es mayor que el segundo")

else:
    print("El primer número es menor que el segundo")


"""Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje."""
numero= int(input("Dime un número: "))

if ((numero % 2) == 0 and (numero % 3 == 0)):
    print("Este número es múltiplo de 2 y de 3")


elif numero % 3 == 0:
    print("Este número es múltiplo de 3")

elif numero % 2 == 0:
    print("Este número es múltilplo de 2")

"""Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto."""
edad= int(input("Dime tu edad: "))
edad < 100
if ((edad >= 0) and (edad <= 12)):
    print("Eres un niño")
elif((edad >= 13)and (edad <= 17)):
    print("Eres un adolescente")
elif((edad >= 18) and (edad <= 29)):
    print("Eres un joven")
else:
    print("Eres un adulto")

"""Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media"""
numero_1= int(input("Dime un numero: "))
numero_2= int(input("Dime un numero: "))
numero_3= int(input("Dime un numero: "))
numero_4= int(input("Dime un numero: "))
nota_media= ((numero_1 + numero_2 + numero_3 + numero_4) / 4)
print(nota_media)
if numero_1 > nota_media:
    print(numero_1)
elif numero_2 > nota_media:
    print(numero_2)
elif numero_3 > nota_media:
    print(numero_3)
elif numero_4 > nota_media:
    print(numero_4)

"""Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc."""
caracter= str(input("Dime un carácter: "))
if caracter == "A":
    print("Esta es la primera vocal (A)")
elif caracter == "E":
    print("Esta es la primera vocal (E)")
elif caracter == "I":
    print("Esta es la primera vocal (I)")
elif caracter == "O":
    print("Esta es la primera vocal (O)")
elif caracter == "U":
    print("Esta es la primera vocal (U)")
else:
    print("Esta letra no es una vocal.")

"""Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%"""
estadoCivil= str(input("Dime tu estado civil: "))
edad= int(input("Dime tu edad: "))

if (estadoCivil == "Soltero" or estadoCivil == "Divorciado" and edad < 35):
    print("12%")
elif edad > 50:
    print("8.5%")
elif (estadoCivil == "Viudo" or estadoCivil == "Casado" and edad < 35):
    print("11.3")
else:
    print("10.5%")

"""Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor”"""
hora_1= int(input("Dime una hora: "))
min_1= int(input("Dime un min. "))
seg_1= int(input("Dime un seg: "))
hora_2= int(input("Dime otra hora: "))
min_2= int(input("Dime otro min: "))
seg_2= int(input("Dime otro seg: "))

if (((hora_1 >= 0 and hora_1 <= 23) and (min_1 >= 0 and min_1 <= 59) and (seg_1 >= 0 and seg_1 <= 59)) and ((hora_2 >= 0 and hora_2 <= 23) and (min_2 >= 0 and min_2 <= 59) and (seg_2 >= 0 and seg_2 <= 59))):
    hora_completa1= hora_1 * 3600 + min_1 * 60 + seg_1
    hora_completa2= hora_2 * 3600 + min_2 * 60 + seg_2
    
    if hora_completa1 > hora_completa2:
        print("la primera hora es mayor.")
    else:
        print("La segunda hora es la mayor")

else:
    print("Esta hora no existe")

"""En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se
aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se
aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y
precio original) y calcule el precio rebajado. Debe comprobarse que los
datos de entrada son correctos, y si no lo son mostrar un mensaje de error"""
producto_pedido= str(input("Dime un producto: "))
precio_pedido= float(input("Dime cuanto vale este producto: "))


if producto_pedido == ("A"):
   precio_descuento= precio_pedido - (precio_pedido * 0.07)
   print(precio_descuento)
    
elif producto_pedido == ("C") and (precio_pedido < 500):
   precio_descuento= precio_pedido - (precio_pedido * 0.12)
   print(precio_descuento)

elif producto_pedido == ("B") or producto_pedido == ("C") and (precio_pedido > 500):  
   precio_descuento= precio_pedido - (precio_pedido * 0.09) 
   print(precio_descuento)
else:
   print("Error de sistema")

"""Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error."""
caracter= str(input("Dime un carácter: "))
numero_1= int(input("Dime un número: "))
numero_2= int(input("Dime otro número: "))
if caracter == "+":
    operador_aritmetico= numero_1 + numero_2
    print(operador_aritmetico)
elif caracter == "-":
    operador_aritmetico= numero_1 - numero_2
    print(operador_aritmetico)
elif caracter == "*":
    operador_aritmetico= numero_1 * numero_2
    print(operador_aritmetico)
elif caracter == "/":
    operador_aritmetico= numero_1 / numero_2
    print(operador_aritmetico)
elif caracter == "**":
    operador_aritmetico= numero_1 ** numero_2
    print(operador_aritmetico)
elif caracter == "%":
    operador_aritmetico= numero_1 % numero_2
    print(operador_aritmetico)
else: 
    print("Error de cálculo.")

          
