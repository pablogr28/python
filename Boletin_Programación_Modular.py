"""Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000)."""
from random import randint
listaAleatorios=[]
for i in range(0,100):
    numeros= randint (0,1000)
    listaAleatorios.append(numeros)
print(listaAleatorios)

mayor=listaAleatorios[0]
for i in range(len(listaAleatorios)):
    if listaAleatorios[i]> mayor:
        mayor=listaAleatorios[i]
print(f"El número mayor es {mayor}")

menor=listaAleatorios[0]
for i in range(len(listaAleatorios)):
    if listaAleatorios[i]< menor:
        menor=listaAleatorios[i]
print(f"El número menor es {menor}")

suma=listaAleatorios[0]
for i in range(len(listaAleatorios)):
    suma+=listaAleatorios[i]
print(f"La suma da {suma}")

"""2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.)"""
lista=[1,2,3,4,5,6,7,8,9,10]
contadorPosicionLista=lista[0]
for i in range(len(lista)):
    contadorPosicionLista=lista[i+1]
print(lista)

"""3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo."""
dia=int(input("Dime un dia: "))
mes=(input("Dime el mes: "))
año=int(input("Dime un año: "))
while dia>0:
    if año % 4 ==0 and año % 100==0 and año % 400==0:
        print("Este año es bisiesto")
        if (dia > 0 and dia <= 31) and mes == "Enero":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 29) and mes == "Febrero":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Marzo":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Abril":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Mayo":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Junio":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Julio":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Agosto":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Septiembre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Octubre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Noviembre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Diciembre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
    else:
        print("Este año no es bisiesto")
        if (dia > 0 and dia <= 31) and mes == "Enero":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 28) and mes == "Febrero":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Marzo":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Abril":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Mayo":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Junio":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Julio":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Agosto":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Septiembre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Octubre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 30) and mes == "Noviembre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
        if (dia > 0 and dia <= 31) and mes == "Diciembre":
            print(f"La fecha en formato largo es {dia} de {mes} de {año}")
    dia=int(input("Dime un dia: "))
    mes=(input("Dime el mes: "))
    año=int(input("Dime un año: "))

"""4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares."""
listaNumeros=[]
numero=int(input("Dime un número: "))
if numero % 2==0:
    print(f"El número {numero} es par ")
else:
    print(f"El número {numero} es impar")
listaNumeros.append(numero)
mayor=listaNumeros[0]
while numero >= 0:
    numero=int(input("Dime un número: "))
    if numero % 2==0:
        print(f"El número {numero} es par ")
    else:
        print(f"El número {numero} es impar")
    listaNumeros.append(numero)
print(listaNumeros)
for i in range(len(listaNumeros)):
    if listaNumeros[i] > mayor:
        mayor=listaNumeros[i]
print(f"El número mayor es {mayor}") 

