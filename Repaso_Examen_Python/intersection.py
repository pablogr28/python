def intersection(cadena_1,cadena_2):
    listaComunes=[]
    listaNoComunes=[]
    for i in cadena_1:
        if i in cadena_2:
             listaComunes.append(i)
        else:
            listaNoComunes.append(i)

    return listaComunes

cadena_1=[1,3,5,7,9]
cadena_2=[8,15,24,9,3]
resultado=intersection(cadena_1,cadena_2)
print(resultado)

def diferencia(cadena_1,cadena_2):
    listaComunes_=[]
    listaNoComunes_=[]
    for i in cadena_1:
        if i in cadena_2:
            listaComunes_.append(i)
        else:
            listaNoComunes_.append(i)

    for j in cadena_2:
        if j in cadena_1:
            listaComunes_.append(j)
        else:
            listaNoComunes_.append(j)


    return listaNoComunes_

cadena_1=[1,3,5,7,9]
cadena_2=[8,15,24,9,3]
resultado=diferencia(cadena_1,cadena_2)
print(resultado)
