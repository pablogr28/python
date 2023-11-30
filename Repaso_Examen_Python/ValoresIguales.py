def get_posicion_eq_valor(cadenaNumeros):
    listaFinal=[]
    listaBasura=[]
    for i in range(len(cadenaNumeros)):
        if i+1 == cadenaNumeros[i]:
            listaFinal.append(cadenaNumeros[i])
        else:
            listaBasura.append(i)

    return listaFinal

cadenaNumeros=[1,3,4,4]
resultado=get_posicion_eq_valor(cadenaNumeros)
print(resultado)

def frecuencia(cadenaNumeros):
    listaNumerosRepetidos=[]
    for i in cadenaNumeros:
        if i in listaNumerosRepetidos:
            listaNumerosRepetidos.append([i])
        else:
            listaNumerosRepetidos.append(i)

    return listaNumerosRepetidos

cadenaNumeros=[1,1,3,4,5,4,6,6,6,4,3,3]
resultado=frecuencia(cadenaNumeros)
print(resultado)
