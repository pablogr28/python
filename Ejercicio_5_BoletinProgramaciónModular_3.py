"""5. Design a function called palindrome that has a string of characters as input parameter,
and returns True if it is a palindrome or False in other cases. A word is a palindrome if it
can be read the same from left to right or right to left, ignoring whites. For example:
"anilina" or "Dabale arroz a la zorra el abad" To simplify the problem, you can assume
that simple characters are used, that is, without tildes or diresis"""
def palindromo(cadenaPalabra):
    cadenaPalabra=cadenaPalabra.lower()
    cadenaPalabraReves=cadenaPalabra[::-1]
    if cadenaPalabra == cadenaPalabraReves:
        return "Es palindromo"
    else:
        return "No es palindromo"
    
cadenaPalabra=(input("Dime una frase cualquiera: "))
final=palindromo(cadenaPalabra)
print(final)