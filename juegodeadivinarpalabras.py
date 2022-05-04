import random

foo = ["casa", "papel", "arbol", "perro", "gato", "avion", "mar", "cisne", "lago", "camino"]

palabrarandom = random.choice(foo)
print(palabrarandom)
    
nombre=input("cual es su nombre: ")
print("hola, el juego trata de adivinar una palabra. solo se aceptan mayores de 12 anios, cual es tu nombre: ")

for i in range (1,6):
    intento = str(input("elija alguna de las palabras: "))
    if intento == palabrarandom:
        print("Ganaste 100 puntos!")
    if intento != palabrarandom:
        print("ingresa una nueva palabra si quieres intentarlo otra vez, o cualquier otra tecla para finalizar el juego!")
    else:
        break

    if intento == palabrarandom:
        print("felicidades! adivinaste la palabra!")
        if i ==1:
            print("ganaste 100 puntos!")
        if i ==2:
            print("ganaste 80 puntos!")
        if i ==3:
            print("ganaste 60 puntos!")
        if i ==4:
            print("ganaste 40 puntos!")
        if i ==5:
            print("ganaste 20 puntos!")
terminar=input("presione enter para jugar una vez mas o cualquier otro boton para terminar el juego")

