def conversion_entero_romano(num1):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while num1 > 0:
        for _ in range(num1 // numeros[i]):
            numeral += numerales[i]
            num1 -= numeros[i]
        
        i += 1
    
    return numeral

print("<----Numeros Romanos---->")
bandera = True


while True:
    num1 = int(input("Digite un numero entero positivo: "))
    if num1 > 0 and num1 <= 1000:
        print("El numero entero en romano es: ", conversion_entero_romano(num1))
        break
    else:
        print("Digite un numero entero mayor a 0 y menor o igual a 1000.")
        
    