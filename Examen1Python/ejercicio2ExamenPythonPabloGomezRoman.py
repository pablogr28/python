#Ejercicio2
numero=int(input("Dime un número: "))
numeroAnterior=0
while numero !=0:
    if numero > numeroAnterior:
        numeroAnterior=numero
        print("Su orden es creciente.")
    elif numero< numeroAnterior:
        numeroAnterior=numero
        print("Están desordenados")
        numero=int(input("Dime un número: "))
    elif numero==numeroAnterior:
        numeroAnterior=numero
        print("Se repite algún número.")
        numero=int(input("Dime un número: "))
        

   