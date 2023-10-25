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
        mayor=listaAleatorios[i]
print(f"El número menor es {menor}")

suma=listaAleatorios[0]
for i in range(len(listaAleatorios)):
    suma+=listaAleatorios[i]
print(f"La suma da {suma}")







