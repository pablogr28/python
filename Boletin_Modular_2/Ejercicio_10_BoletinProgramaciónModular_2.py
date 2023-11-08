"""10. Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa"""
def obtenerNumerosAmigos(numero_1,numero_2):
    contadorDivisores=0
    for i in range(1, numero_1):
        if numero_1 % i == 0:
            contadorDivisores+=i
    
    if contadorDivisores == numero_2:
        return True
    else:
        return False



numero_1=int(input("Dime un numero cualquiera: "))
numero_2=int(input("Dime un numero cualquiera: "))
resultado=obtenerNumerosAmigos(numero_1,numero_2)
print(resultado)