"""1. Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None."""
from math import factorial


def computeFactorial (numeroOperacion):
    if numeroOperacion < 0:
        return None
    elif numeroOperacion == 0:
        return 1
    elif numeroOperacion < 0:
        return numeroOperacion*factorial(numeroOperacion-1)
    
numeroOpercion=int(input("Dime un número cualquiera: "))
resultado=factorial(numeroOpercion)
print(resultado)
        

"""2. Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400."""
def isLeapYear(año):
    if año % 4 ==0 and año % 100 != 0 or año % 400==0:
        return True
    else:
        return False
    
año=int(input("Dime un año: "))
calculo=isLeapYear(año)
print(calculo)

"""3. Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1."""
def isLeapYear(año):
    if año % 4 ==0 and año % 100 != 0 or año % 400==0:
        return True
    else:
        return False
    

def computeDaysInMonth(año,mes):
    if isLeapYear(año) == True:
        if mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
            return 31
        elif mes == "Febrero":
            return 29
        elif mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
            return 30
    else:
        if mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
            return 31
        elif mes == "Febrero":
            return 28
        elif mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
            return 30

año=int(input("Dime un año cualquiera: "))
calcularaño=isLeapYear(año)
mes=(input("Dime un mes cualquiera: "))
resultado=computeDaysInMonth(año,mes)
print(resultado)

"""4. Design a method called getDayOfWeek that receives a list containing three integers
(day, month and year) and returns the day of the week for that date (Monday,
Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).
You can use the following algorithm to get a number between 0 (Sunday) and 6
(Saturday) corresponding to the day in the week for a given date:
a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7"""
def getDayofWeek(dia,mes,año):
    if dia > 0 and mes > 0 and año > 0:
        a=(14-mes)/12
        y = año - a
        m = mes + 12 * a - 2
        d = (dia + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
        if d == 0:
            return "Domingo"
        elif d == 1:
            return "Lunes"
        elif d == 2:
            return "Martes"
        elif d == 3:
            return "Miércoles"
        elif d == 4:
            return "Jueves"
        elif d == 5:
            return "Viernes"
        elif d == 6:
            return "Sábado"
    
dia=int(input("Dime un día cualquiera: "))
mes=int(input("Dime un mes cualquiera: "))
año=int(input("Dime un año cualquiera: "))
calculo=getDayofWeek(dia,mes,año)
print(calculo)


"""5. Design a method called powerIt that receives two integers and raises the first
number to the second. You may use the product or recursion and check the values. If
no exponent is provided the first number is raised to 0."""
def powerIt (numero_1,numero_2):
    if numero_2 == 0:
        return 1
    elif numero_2 == 1:
        return numero_1
    else:
        resultado=numero_1**numero_2
        return resultado

numero_1=int(input("Dime un número: "))
numero_2=int(input("Dime otro número: "))
resultado=powerIt(numero_1,numero_2)
print(resultado)


"""6. Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal)."""
def getNumberOfDigits(cadenaNumero):
    if not cadenaNumero.isdigit():
        return None
    
    contadorDigitos = len(cadenaNumero)
    return contadorDigitos

numero = input("Dime un número cualquiera: ")
resultado = getNumberOfDigits(numero)
print(resultado)

"""7. Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None."""
def isPrime(numero):
    if numero > 0:
        for i in range(2,numero):
            if numero % i == 0:
                return False
            else:
                return True
    else:
        return None
    
numero=int(input("Dime un número cualquiera: "))
resultado=isPrime(numero)
print(resultado)
            
"""8. Design a method called solveSecondOrderEquation that receives three integer
positive numbers corresponding to the coefficients of a second order equation
(ax2+bx+c=0) and computes its possible solutions. If the parameters are not valid the
method should return None."""
import math

def solveSecondOrderEquation(incognitaA, incognitaB, incognitaC):
    discriminante = (incognitaB**2) - (4*incognitaA*incognitaC)
    
    if discriminante < 0:
        return None
    
    else:
        solucion_1 = (-incognitaB + math.sqrt(discriminante)) / (2*incognitaA)
        solucion_2 = (-incognitaB - math.sqrt(discriminante)) / (2*incognitaA)

    return solucion_1, solucion_2

incognitaA = int(input("Dime la primera incógnita: "))
incognitaB = int(input("Dime la segunda incógnita: "))
incognitaC = int(input("Dime la tercera incógnita: "))

final = solveSecondOrderEquation(incognitaA, incognitaB, incognitaC)
print(final)

    


    
"""9. Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None"""
def isPrime(numero):
    if numero > 0:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
    else:
        return None
    
def getPrimeDivisors(numero):
    divisoresNumero = []
    if numero > 0:
        for i in range(2, numero+1):
            if numero % i == 0 and isPrime(i):
                divisoresNumero.append(i)
        return divisoresNumero
    else:
        return "None"

numero = int(input("Dime un número cualquiera: "))
resultado = getPrimeDivisors(numero)
print(resultado)

"""10. Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa"""