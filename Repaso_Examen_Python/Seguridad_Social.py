def generar_digito_control():
    import random
    numero=random.randint(0,1000000000)
    listaNumero=[]
    listaNumero.append(numero)
    listaNumeroControl=[]
    listaCompleta=[]
    numeroControl=numero%97
    if numeroControl < 10:
        listaNumeroControl.append(numeroControl)
        listaNumeroControl.insert(0,0)
    else:
        listaNumeroControl.append(numeroControl)

    listaCompleta.append(numero)
    listaCompleta.append(numeroControl)
    cadenaCompleta=str(listaCompleta)
    cadenaCompleta="".join(cadenaCompleta)

    return cadenaCompleta

print(generar_digito_control())

def es_emitido_andalucia(cadenaSeguridad):
   SEGURIDAD_SOCIAL=[["Almeria",4],["Cadiz",11],["Cordoba",14],["Granada",18],["Huelva",21],["Jaen",23],["Malaga",29],["Sevilla",41]]
   NumeroSeguridad=int(cadenaSeguridad[0:2])
   NumeroControl=int(cadenaSeguridad[2:])
   for i in SEGURIDAD_SOCIAL:
       if i[1] == NumeroSeguridad:
           return f"Tu numero de la seguridad social {cadenaSeguridad} pertenece a la comunidad autonoma {i[0]}"
   return "Este numero de la seguridad social no es correcto"

listaSeguridadSocial=[]
cadenaSeguridad=input("Dime tu numero de la seguridad social: ")
listaSeguridadSocial.append(cadenaSeguridad)
resultado=es_emitido_andalucia(cadenaSeguridad)
print(resultado)



    


