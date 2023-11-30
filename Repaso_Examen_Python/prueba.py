"""3. Write a Python program to convert seconds to day, hour, minutes and seconds."""
def convertidorDias(segundos):
    horas=segundos/360
    minutos=(segundos%360)/60
    segundos=minutos%60
    return f"{horas}horas,{minutos}min y {segundos} segundos"

segundos=int(input("Dime los segundos: "))
resultado=convertidorDias(segundos)
print(resultado)