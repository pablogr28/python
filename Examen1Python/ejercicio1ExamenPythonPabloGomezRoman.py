#ejercicio 1

numero_1=int(input("Dime un número: "))
numero_2=int(input("Dime un número: "))
numero_3=int(input("Dime un número: "))
while (numero_1>0 and numero_2>0) or (numero_3>0 and numero_2>0) or (numero_3>0 and numero_1>0):
    if numero_1 < numero_2 and numero_2 < numero_3 and numero_1 < numero_3:
        print(f"{numero_1}, {numero_2}, {numero_3}")
        numero_1=int(input("Dime un número: "))
        numero_2=int(input("Dime un número: "))
        numero_3=int(input("Dime un número: "))
    elif numero_1 < numero_2 and numero_2 > numero_3 and numero_2 > numero_1:
        print(f"{numero_1}, {numero_3}, {numero_2}")
        numero_1=int(input("Dime un número: "))
        numero_2=int(input("Dime un número: "))
        numero_3=int(input("Dime un número: "))
    elif numero_3 < numero_1 and numero_1 > numero_2 and numero_1 > numero_3:
        print(f"{numero_3}, {numero_2}, {numero_1}")
        numero_1=int(input("Dime un número: "))
        numero_2=int(input("Dime un número: "))
        numero_3=int(input("Dime un número: "))
    elif numero_3 < numero_2 and numero_2 > numero_1 and numero_1 > numero_3:
        print(f"{numero_3}, {numero_1}, {numero_2}")
        numero_1=int(input("Dime un número: "))
        numero_2=int(input("Dime un número: "))
        numero_3=int(input("Dime un número: "))
    elif numero_2 < numero_1 and numero_1 > numero_3 and numero_1 > numero_2:
        print(f"{numero_2}, {numero_3}, {numero_1}")
        numero_1=int(input("Dime un número: "))
        numero_2=int(input("Dime un número: "))
        numero_3=int(input("Dime un número: "))
    elif numero_2 < numero_3 and numero_3 > numero_1 and numero_3 > numero_2:
        print(f"{numero_2}, {numero_1}, {numero_3}")
        numero_1=int(input("Dime un número: "))
        numero_2=int(input("Dime un número: "))
        numero_3=int(input("Dime un número: "))


    

    
