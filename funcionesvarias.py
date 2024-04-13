def cadenainversa(cadena):
    return cadena[::-1]

def combinalista(lista1, lista2):
    listaNueva = lista1 + lista2
    lista_ordenada = sorted(listaNueva)
    
    return lista_ordenada


print("Funciones Varias")
print("1. Cadena Reversa")
print("2. Combinacion de lista")
op = input("Elija una funcion: ")

if op == "1":
    cadena = input("Digite una cadena de caracteres: ")
    print("Cadena invertida: ",cadenainversa(cadena))
elif op == "2":
    lista1=[]
    lista2=[]

    cant_num1 = int(input("Digite la cantidad de numeros de la lista 1: "))
    for i in range(cant_num1):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        lista1.append(numero)
    
    cant_num2 = int(input("Digite la cantidad de numeros de la lista 1: "))
    for i in range(cant_num2):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        lista2.append(numero)

    lista_numeros = combinalista(lista1, lista2)
    print("Lista de numeros combinados: ", lista_numeros)




