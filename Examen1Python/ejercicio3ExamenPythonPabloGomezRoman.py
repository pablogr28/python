#ejercicio3
opcion=(input("Deseas añadir un nuevo parte de accdiente: "))
contadortotal=0
contadorAccidenteLeve=0
contadorAccidenteModerado=0
contadorAccidenteGrave=0
contadorEso=0
contadorPost=0
while opcion == "S" and opcion != "N":
    tipoAccidente=(input("Dime que tipo de parte ha ocurrido: "))
    tituloMatriculado=(input("Dime en que estas matriculado: "))
    if tipoAccidente == "L":
        if tituloMatriculado == "E":
            contadorAccidenteLeve+=1
            contadorEso+=1
            contadortotal+=1
        elif tituloMatriculado == "P":
            contadorAccidenteLeve+=1
            contadorPost+=1
            contadortotal+=1
        opcion=(input("Deseas añadir un nuevo parte de accdiente: "))
    elif tipoAccidente == "M":
        if tituloMatriculado == "E":
            contadorAccidenteModerado+=1
            contadorEso+=1
            contadortotal+=1
        elif tituloMatriculado == "P":
            contadorAccidenteModerado+=1
            contadorPost+=1
            contadortotal+=1
        opcion=(input("Deseas añadir un nuevo parte de accdiente: "))
    elif tipoAccidente == "G":
        if tituloMatriculado == "E":
            contadorAccidenteGrave+=1
            contadorEso+=1
            contadortotal+=1
        elif tituloMatriculado == "P":
            contadorAccidenteGrave+=1
            contadorPost+=1
            contadortotal+=1
        opcion=(input("Deseas añadir un nuevo parte de accdiente: "))

porcentajeEso=(contadorEso / contadortotal) * 100
porcentajePost=(contadorPost / contadortotal) * 100
print(f"Se han producido {contadortotal} incidentes en el centro: {contadorAccidenteLeve} de ellos leves, {contadorAccidenteModerado} Moderados y {contadorAccidenteGrave} Graves, siendo el {porcentajeEso} en ESO y el {porcentajePost} en Post-Obligatoria.")


    
    

        
