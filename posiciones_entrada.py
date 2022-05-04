import pickle
import jugadores
posiciones=[]
while True:
    try:
        continuar=input("Ingrese t si desea ingresar un jugador:")
        if continuar=="t":
            nuevo=jugadores.jugadores
            nuevo.nombre=input("Ingrese el nombre del jugador:")
            print(nuevo.nombre)
            nuevo.tiempo=input("Ingrese el tiempo del jugador:")
            print(nuevo.tiempo)
            nuevo.resultado=input("Ingrese el resultado boleano del jugador:")
            print(nuevo.resultado)
            posiciones.append(nuevo)
        else:
            for x in posiciones:
                print("nombre:",nombre,"tiempo:",tiempo,"Resultado:",resultado)

            print("Programa terminado")
            break
    except ValueError:
        print("Oooooops, error al digitar")

archivo=open("tabla de posiciones.txt","wb")
pickle.dump(posiciones,archivo)
archivo.close()

