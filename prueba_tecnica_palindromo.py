
def palindromo_numero():
    numero = int(input("Ingrese numero: "))
    return str(numero) == str(numero)[::-1]

prueba = palindromo_numero()
print(prueba)