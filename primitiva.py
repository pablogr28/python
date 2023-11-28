
def eliminarRepetidos(combinacion):
    apuestaSinRepetidos=[]
    for i in combinacion:
        if i not in apuestaSinRepetidos:
            apuestaSinRepetidos.append(i)
    return apuestaSinRepetidos

def sonValoresValidos(combinacion):
    validos = True
    for numero in combinacion:
        if numero<1 or numero>49:
            validos=False
    return validos

def sonDatosValidos(apuesta, ganadora):
    return sonValoresValidos(apuesta) and sonValoresValidos(ganadora) and len(apuesta)==6 and len(ganadora)==6  and len(eliminarRepetidos(apuesta))==6 and len(eliminarRepetidos(ganadora))==6 

def comprobar_resultado(apuesta, ganadora):
    aciertos = 0

    if not sonDatosValidos(apuesta, ganadora):
        aciertos = -1


    else:
        for numero in apuesta:
            if numero in ganadora:
                aciertos+=1

    return aciertos

def numeroAleatorio():
    import random
    contadorNumeros=0
    listaNumeros=[]
    listaNumerosRepetidos=[]
    while contadorNumeros <=5:
        numero=random.randint(1,49)
        if numero in listaNumeros:
            listaNumerosRepetidos.append(numero)
        else:
            listaNumeros.append(numero)
            contadorNumeros+=1
    return listaNumeros

def numeroApuesta():
    listaApuesta=[]
    contadorNumeros=0
    while contadorNumeros < 6:
        numero=int(input("Dime un número: "))
        if numero > 1 and numero <= 49: 
            if numero in listaApuesta:
                print("Numero repetido")
            else:
                listaApuesta.append(numero)
                contadorNumeros+=1


    
    return listaApuesta


def primitiva(listaGanadora, listaApuesta):
    listaGanadora=eliminarRepetidos(listaGanadora)
    listaApuesta=eliminarRepetidos(listaApuesta)
    listaGanadoraValida=sonValoresValidos(listaGanadora)
    listaApuestaValida=sonValoresValidos(listaApuesta)
    aciertos=comprobar_resultado(listaApuesta,listaGanadora)
    if aciertos < 3:
        return "No ha ganado ningún premio"
    elif aciertos >= 3:
        return "Ha ganado algún premio"
    elif aciertos == 6:
        return "ENHORABUENA. TIENES EL PLENO"

listaGanadora=numeroAleatorio()
listaApuesta=numeroApuesta()
print(listaApuesta)
resultado=primitiva(listaGanadora,listaApuesta)
print(resultado)
print(f"El boleto ganador es {listaGanadora}")



    

    













