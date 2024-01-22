
def palindromo_numero(n):
    return str(n) == str(n)[::-1]

def primo(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        
        return True

def siguiente_palindromo_primo():
    n = int(input("Ingrese numero: "))
    while True:
        if primo(n) and palindromo_numero(n):
            return n
        n += 1

prueba = siguiente_palindromo_primo()
print(prueba)