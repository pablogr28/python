menuprincipal='''
#############################################################
A) Añadir cliente
B) Mostrar los % de clientes premium y normales
C) Visualizar todos los cálculos para clientes premium, debiendo mostrar:
    -% clientes Premium
    -importe máximo gastado por pedido y correo del cliente 
    -datos del artículo más caro entre los premiums
D) Visualizar todos los cálculos para clientes normales
    -% clientes normal
    -codigo del artículo más vendido entre todos los clientes normales
E) Mostrar correo de nuestro mejor cliente y el importe gastado (el que mas haya comnprado ya sea premium o normal)
G) Salir
#############################################################
'''
print(menuprincipal)
opcion=(input("Dime una de las tres opciones: "))
contadorPremium=0
contadorNoPremium=0
contadorTotal=0
importeMaximo=0
articuloMasCaro=0
while opcion != "G":
    while opcion !="A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E":
        print("Esta opción no es la correcta.")
        opcion=(input("Dime una opción correcta: "))
    if opcion == "A":
        cliente=(input("Dime tu nombre: "))
        clientePremium=(input("¿Eres cliente premium? "))
        correoElectronico=(input("Dime tu correo electronico: "))
        codigoArticulo=(input("Dime tu código de artículo: "))
        unidadesArticulo=int(input("Dime cuantas unidades has comprado: "))
        precioUnitarioArticulo=int(input("Dime cuanto vale el artículo: "))
        if clientePremium == "S":
            contadorPremium+=1
            contadorTotal+=1
            opcion=(input("Dime que opcion quieres: "))
        else:
            contadorNoPremium+=1
            contadorTotal+=1
            opcion=(input("Dime que opción quieres: "))
    elif opcion == "B":
        porcentajeNoPremium= (contadorNoPremium / contadorTotal) * 100
        print(f"El porcentaje de clientes normales es {porcentajeNoPremium}%")
        porcentajePremium= (contadorPremium / contadorTotal) * 100
        print(f"El porcentaje de clientes Premium es {porcentajePremium}%")
        opcion=(input("Dime una opción: "))
    elif opcion == "C":
        porcentajePremium= (contadorPremium / contadorTotal) * 100
        print(f"El porcentaje de clientes Premium es {porcentajePremium}%")
        importeCliente= unidadesArticulo * precioUnitarioArticulo
        if importeCliente > importeMaximo:
            importeMaximo= importeCliente
            print(f"El importe más grande es {importeMaximo} y el correo es {correoElectronico}")
        elif precioUnitarioArticulo > articuloMasCaro:
            articuloMasCaro= precioUnitarioArticulo
            print(f"El articulo mas caro vale {articuloMasCaro} y su código es {codigoArticulo}")
    elif opcion == "D":
        porcentajeNoPremium= (contadorNoPremium / contadorTotal) * 100