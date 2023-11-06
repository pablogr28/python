"""Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los numeros
d. Obtener la media
e. Sustituir el valor de un elemento por otro numero introducido por teclado
f. Mostrar todos los numeros
 Realiza cada una de las opciones con funciones.
 Utiliza la funcion siguiente para generar numeros aleatorios (entre 0 y 1000)."""
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


"""5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. 
Así, dada la lista [Di, buen, día, a, papa], deberá devolver [papa, a, día, buen, Di]."""

def revertir(lista):
    reversa_lista = []
    for i in range(len(lista)-1, -1, -1):
        reversa_lista.append(lista[i])
    return reversa_lista

original_lista = ["Di", "buen", "día", "a", "papa"]
reversa_lista = revertir(original_lista)
print(reversa_lista)

"""6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario."""

lista=[7,8,9,10,14,13]

def estaOrdenada(lista):
    return lista == sorted(lista)

resultado = estaOrdenada(lista)

if resultado:
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")


"""7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]"""

def encajan(ficha1, ficha2):
    numero1 = int(ficha1[1])
    numero2 = int(ficha1[3])
    numero3 = int(ficha2[1])
    numero4 = int(ficha2[3])
    
    if numero1 == numero3 or numero1 == numero4 or numero2 == numero3 or numero2 == numero4:
        return True
    else:
        return False



ficha1 = "[3,5]"
ficha2 = "[2,4]"
if encajan(ficha1, ficha2):
    print("Las fichas encajan")
else:
    print("Las fichas no encajan")


"""8. Realiza un programa que añada números enteros a una lista hasta que se introduzca un número negativo. 
Haciendo uso de esta lista, elabora funciones que devuelvan:

a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números."""


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def obtener_Lista_numeros_primos():
    numeros = []
    num = int(input("Ingresa un número entero (negativo para detener): "))
    while num >= 0:
        numeros.append(num)
        num = int(input("Ingresa un número entero (negativo para detener): "))
    
    primos = []
    for num in numeros:
        if es_primo(num):
            primos.append(num)
    
    return primos

numeros_primos = obtener_Lista_numeros_primos()
print("Números primos:", numeros_primos)




def obtener_Lista_Sumatorio():
    numeros2 = []
    num2 = int(input("Ingresa un número entero (negativo para detener): "))
    while num2 >= 0:
        numeros2.append(num2)
        num2 = int(input("Ingresa un número entero (negativo para detener): "))
    return numeros2


def sumatorio(numeros2):
    contadorNumero2 = 0
    for num2 in numeros2:
        contadorNumero2 += num2
    return contadorNumero2

numeros2 = obtener_Lista_Sumatorio()
total = sumatorio(numeros2)
print("La suma total es:", total)




def obtener_Lista_promedio():
    numeros3 = []
    num3 = int(input("Ingresa un número entero (negativo para detener): "))
    while num3 >= 0:
        numeros3.append(num3)
        num3 = int(input("Ingresa un número entero (negativo para detener): "))
    return numeros3

def obtenerPromedio(numeros3):
    promedio= sum(numeros3) / len(numeros3)
    return promedio

lista_numeros = obtener_Lista_promedio()
promedio = obtenerPromedio(lista_numeros)
print("El promedio es:", promedio)



def obtener_Lista_Factorial():
    numeros4 = []
    num4 = int(input("Ingresa un número entero (negativo para detener): "))
    while num4 >= 0:
        numeros4.append(num4)
        num4 = int(input("Ingresa un número entero (negativo para detener): "))
    return numeros4

def factorial(numeros4):
   if numeros4==0 or numeros4==1:
            resultado=1
   elif numeros4>1:
            resultado=numeros4*factorial(numeros4-1)
   return resultado

numeros4 = obtener_Lista_Factorial()
for num in numeros4:
    total = factorial(num)
    print("El factorial de", num, "es:", total)


"""9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k."""

listaNumeros=[3,6,7,9,8,33,7,33,7,34,2,8,2,7,3,11,2,72,9,5]
listaMenores=[]
listaMayores=[]
listaMultiplo=[]
k=int(input("Dime un número cualquiera:"))
for numerosLista in listaNumeros:
    if numerosLista < k:
        listaMenores.append(numerosLista)
print(listaMenores)

for numerosLista in listaNumeros:
    if numerosLista > k:
        listaMayores.append(numerosLista)
print(listaMayores)

for numerosLista in listaNumeros:
    if numerosLista % k== 0:
        listaMultiplo.append(numerosLista)
print(listaMultiplo)

"""10. Diseña una función conversor que convierta un número de binario a decimal o de decimal a binario. 
Esta función recibirá un número en formato de cadena de texto cuya última posición 
indica que el sistema numérico utilizado es: (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1. """


def conversor(numeroCadena):
    defineUltimoCarcter=numeroCadena[-1]
    cadena=numeroCadena[:1]
    if defineUltimoCarcter =="D":
        if cadena.isdigit():
            return bin(int(cadena)).replace("0b", " ")
        else:
            return "Numero decimal invalido"
    elif defineUltimoCarcter =="B":
        for i in cadena:
            if i != "0" or i != "1":
                return "Este numero binaro no es valido"
        return str(int(cadena))
    
print(conversor("101001001011B"))


"""11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno."""

def intersect (lista_1,lista_2):
    comunes=[]
    for elemento in lista_1:
        if elemento in lista_2 and elemento not in comunes:
            comunes.append(elemento)

    return comunes

lista_1 = [1,3,5,45,555,665,4434]
lista_2 = [1,3,5,8,9,99,66,4456]
print(intersect(lista_1,lista_2))


"""12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos)."""

def unionListas(lista_1, lista_2):
    listaUnida = []
    for elemento in lista_1:
        if elemento not in listaUnida:
            listaUnida.append(elemento)
    for elemento in lista_2:
        if elemento not in listaUnida:
            listaUnida.append(elemento)
    return listaUnida


lista_1 = [8,6,4,3,5,6,3,6,367,8,5,8,4]
lista_2 = [1,2,3,3,4,2,1,5,2,1,5,12,5,51,5,6,64,]
print(unionListas(lista_1, lista_2))


"""13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos."""
def nombresEmpiezaletra(nombres, letra):
    listaFinal = []
    for i in nombres:
        if i[0].lower() == letra.lower():
            listaFinal.append(i)
    return listaFinal

listaNombre = ["Pablo","Antonio","Paula","Maria","Pedro"]
letraEmpieza = "P"

print(nombresEmpiezaletra(listaNombre, letraEmpieza))

"""14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos."""

def cadenaMasLarga(lista_1,lista_2):
    if len(lista_1) > len(lista_2):
        return lista_1
    elif len(lista_1) < len(lista_2):
        return lista_2
    elif len(lista_1) == len(lista_2):
        contadorCaracteresRepetidos_1=0
        contadorCaracteresRepetidos_2=0
        for i in lista_1:
            if i == lista_1[0]:
                contadorCaracteresRepetidos_1+=1
        for i in lista_2:
            if i == lista_2[0]:
                contadorCaracteresRepetidos_2+=1
        if contadorCaracteresRepetidos_1 > contadorCaracteresRepetidos_2:
            return lista_1
        else:
            return lista_2

   
lista_1=[1,1,3,1]
lista_2=[1,5,6,7]
print(cadenaMasLarga(lista_1, lista_2))









