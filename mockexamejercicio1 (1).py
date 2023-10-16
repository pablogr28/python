menuprincipal='''
#############################################################
A) Añadir cliente
B) Mostrar los % de clientes premium y normales
G) Salir
#############################################################
'''
print(menuprincipal)
opcion=(input("Dime una de las tres opciones: "))
contadorPremium=0
contadorNoPremium=0
contadorTotal=0
while opcion != "G":
    if opcion !="A" and opcion != "B":
        print("Esta opción no es la correcta.")
        opcion=(input("Dime una opción correcta: "))
    if opcion == "A":
        cliente=(input("Dime tu nombre: "))
        clientePremium=(input("¿Eres cliente premium? "))
        correoElectronico=(input("Dime tu correo electronico: "))
        contadorTotal+=1
        if clientePremium == "S":
            contadorPremium+=1
            opcion=(input("Dime que opcion quieres: "))
        else:
            contadorNoPremium+=1
            opcion=(input("Dime que opción quieres: "))
    elif opcion == "B":
        porcentajeNoPremium= (contadorNoPremium / contadorTotal) * 100
        print(f"El porcentaje de clientes normales es {porcentajeNoPremium}%")
        porcentajePremium= (contadorPremium / contadorTotal) * 100
        print(f"El porcentaje de clientes Premium es {porcentajePremium}%")