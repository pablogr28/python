"""1. Design a function called charactersInString that has a character string and a character
as input parameters and returns how many times that character appears in the string. It
should do it no matter if the string and character are lower case or upper case characters."""
def charactersInString(string, character):
    contador = 0
    for char in string:
        if char.lower() == character.lower():
            contador += 1
    return contador
result = charactersInString("Buenas Antonio", "o")
print(result)


"""2. Design a function called lowCaseInString that has a string of characters as parameter,
the method should return how many of those characters are lowercase letters."""
def lowCaseInString(cadena_frase):
    contador=0
    for i in cadena_frase:
        if i.islower():
            contador +=1
    return contador
resultado=lowCaseInString(input("Dime una frase cualquiera: "))
print(result)

"""3. Design a function called upperCaseInString that has a string of characters as parameter
and the method should return how many are uppercase letters."""
def upperCaseInString(cadena_frase):
    contador=0
    for i in cadena_frase:
        if i.isupper():
            contador +=1
    return contador
resultado=upperCaseInString(input("Dime una frase cualquiera: "))
print(result)

"""4. Design a function called numberInString that receives a string of characters as
parameter and returns how many of them are numbers."""
def numberInString(cadena_frase):
    contador=0
    for i in cadena_frase:
        if i.isdigit():
            contador +=1
    return contador
cadenaFrase=(input("Dime una frase cualquiera: "))
resultado=numberInString(cadenaFrase)
print(resultado)

"""5. Design a function called palindrome that has a string of characters as input parameter,
and returns True if it is a palindrome or False in other cases. A word is a palindrome if it
can be read the same from left to right or right to left, ignoring whites. For example:
"anilina" or "Dabale arroz a la zorra el abad" To simplify the problem, you can assume
that simple characters are used, that is, without tildes or diresis."""
def palindromo(cadenaPalabra):
    cadenaSinEspacios = []
    for i in cadenaPalabra:
        if i.isalpha():
            cadenaSinEspacios.append(i)
    cadenaSinEspacios = ''.join(cadenaSinEspacios).lower()
    cadenaPalabraReves = cadenaSinEspacios[::-1]
    if cadenaSinEspacios == cadenaPalabraReves:
        return True
    else:
        return False
    
cadenaPalabra = input("Dime una frase cualquiera: ")
final = palindromo(cadenaPalabra)
print(final)
"""6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo,
si la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False. Las letras
de la palabra escondida deben aparecer en el orden correcto en la cadena que la oculta:
shybaoxlna ⇒ hola: True
soybahxlna ⇒ hola: False"""
def buscar_palabra(texto, palabra):
    indice_palabra = 0
    for i in texto:
        if i == palabra[indice_palabra]:
            indice_palabra += 1
            if indice_palabra == len(palabra):
                return True
    return False

texto = "shybaoxlna"
palabra = "hola"
resultado = buscar_palabra(texto, palabra)
print(resultado)
    
"""7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase
y deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla
por la tercera."""
def replace(cadena_frase, palabraSustituir, palabraNueva):
    cadena_1=cadena_frase
    cadenaIntermedia=""
    cadenaFinal=""
    for i in cadena_1:
        if i == palabraSustituir:
            cadenaIntermedia+=i
            if len(palabraSustituir) == len(cadenaIntermedia):
                cadenaFinal+=palabraNueva
        else:
            cadenaFinal+=i
    return cadenaFinal

cadena_frase=(input("Dime una frase cualquiera: "))
palabraSustituir=(input("Dime que palabra quieres sustituir de la frase anterior: "))
palabraNueva=(input("Dime por cual palabra quieres sustituir por la anterior: "))
resultado=replace(cadena_frase, palabraSustituir, palabraNueva)
print(resultado)

    
"""8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una
palabra o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2."""
def vocalesDiferentes(palabra):
    palabra.lower()
    contadorA=0
    contadorE=0
    contadorI=0
    contadorO=0
    contadorU=0
    for i in palabra:
        if i == "a":
            contadorA=1
        elif i == "e":
            contadorE=1
        elif i == "i":
            contadorI=1
        elif i == "o":
            contadorO=1
        elif i == "u":
            contadorU=1
    contadorFinal=contadorA+contadorE+contadorI+contadorO+contadorU
    return contadorFinal

palabra=(input("Dime una palabra cualquiera: "))
resultado=vocalesDiferentes(palabra)
print(resultado)

"""9. Crear una función que, tomando una cadena de texto como entrada, construya y
devuelva otra cadena formada de la siguiente manera: todas las consonantes estarán al
principio y todas las vocales al final de la misma, eliminando los blancos. Por ejemplo,
pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio’."""
def consonantesPrimero (cadenaFrase):
    cadenaFrase.lower()
    listaConsonantes=""
    listaEspacios=""
    listaVocales=""
    for i in cadenaFrase:
        if i == "q" or i == "w" or i == "r" or i == "t" or i == "y" or i == "p" or i == "s" or i == "d" or i == "f" or i == "g" or i == "h" or i == "j" or i == "k" or i == "l" or i == "ñ" or i == "z" or i == "x" or i == "c" or i == "v" or i == "b" or i == "n" or i == "m":
            listaConsonantes+=i
        elif i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            listaVocales+=i
        else:
            listaEspacios+=i


    listaFinal=listaConsonantes+listaVocales
    return listaFinal

cadenaFrase=(input("Dime una frase cualquiera: "))
resultado=consonantesPrimero(cadenaFrase)
print(resultado)

"""10. Escribir una función que devuelva el número de palabras que hay en una cadena que
recibe como parámetro. Ten en cuenta que entre dos palabras puede haber más de un
blanco. También al principio y al final de la frase puede haber blancos redundantes. Por
ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3."""
def contarPalabra (cadena_Palabra):
    cadena_Espacios=""
    cadena_PalabraFinal=""
    cadena_Intermedia=""
    contadorPalabras=1
    contadorEspacio=0
    for i in cadena_Palabra:
        if i.isalpha() and contadorEspacio != 0:
            cadena_Intermedia+=i
            contadorEspacio=0 
        elif i.isalpha():
            cadena_Intermedia+=i
        elif i == " " and contadorEspacio == 0:
            cadena_Espacios+=i
            cadena_PalabraFinal=cadena_Intermedia
            contadorPalabras+=1
            contadorEspacio+=1
        elif i == " " and contadorEspacio != 0:
            contadorEspacio+=1
    return contadorPalabras

cadena_Palabra=(input("Dime una frase cualquiera: "))
resultado=contarPalabra(cadena_Palabra)
print(resultado)