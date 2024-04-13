import random

adivinado = False
minNumero = 1
maxNumero = 99

print("¡Bienvenido!")
print("Estoy pensando en un número entre 1 y 99.")
print("¿Podrás adivinar el número en el que estoy pensando?")

number = random.randint(minNumero, maxNumero)
intentos = int(input("¿Cuántas veces usted quiere jugar hoy?: "))
guesess = intentos

while not adivinado and intentos > 0:
    guess = int(input("¿Cuál cree usted que es el número?: "))
    
    if guess != number:
        intentos -= 1  # Reducir los intentos restantes solo si la suposición es incorrecta
        print("Su posición es falsa. Por favor, inténtelo de nuevo, usted tiene", intentos, "intentos restantes para adivinar.")
    else:
        adivinado = True

if adivinado:
    print("¡Increíble, su posición fue correcta! ", str(number), " es el número correcto!")
else:
    print("Usted ha agotado sus ", guesess , " conjeturas. El número real era", str(number))
