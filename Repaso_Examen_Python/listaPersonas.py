def caracteristicasPersona():
    listaPersonas=[]
    contadorPersonas=0
    while contadorPersonas<=5:
        peso=float(input("Dime cuanto pesas: "))
        altura=float(input("Dime tu altura en metros: "))
        imc=peso/(altura**2)
        listaPersonas.append([peso,altura,imc])
        contadorPersonas+=1

    return listaPersonas

print(caracteristicasPersona())


    