def jacaBet():
    import random
    MENU='''
    1.Apostar
    2.Añadir saldo
    3.Mostrar saldo
    4.Retirarse'''
    print(MENU)
    saldo=0
    opcion=int(input("Dime que opcion quieres: "))
    while opcion <=4:
        if opcion == 1:
            numeroApuesta=int(input("Dime tu numero con el que quieres apostar: "))
            if numeroApuesta >= 2 and numeroApuesta <=12:
                cantidadApostar=float(input("Dime cuanto dinero quieres apostar: "))
                numeroGanador=random.randint(2,12)
                if cantidadApostar>saldo:
                    print("No tienes saldo suficiente.")
                else:
                    if numeroApuesta == numeroGanador:
                        saldo+=cantidadApostar*2
                    else:
                        saldo-=cantidadApostar
                        print("No has ganado")
            else:
                print("Este numero no es valido.")


            opcion=int(input("Dime que opcion quieres: "))

        elif opcion == 2:
            cantidadMeter=float(input("Dime cuanto dinero quieres meter: "))
            saldo+=cantidadMeter

            opcion=int(input("Dime que opcion quieres: "))

        elif opcion == 3:
            print(f"Tu saldo es de {saldo} euros")
            opcion=int(input("Dime que opcion quieres: "))

        elif opcion == 4:
            retirarse=input("¿Estas seguro que quieres retirarse?")
            retirarse.lower()
            if retirarse == "no":
                opcion=int(input("Dime que opcion quieres: "))
            elif retirarse == "si":
                return "Saliendo del sistema"
            
print(jacaBet())

