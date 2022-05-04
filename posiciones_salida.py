import os.path
import pickle

if(os.path.exists("tabla de posiciones.txt")):
    archivo=open("tabla de posiciones.txt","rb")
    lista=pickle.load(archivo)
    print("  Tabla de posiciones:  ")
    print(lista)
    for x in lista:        
        print("nombre:",nombre,"tiempo:",tiempo,"Resultado:",resultado)

else:
    print("El archivo: tabla de posiciones.txt no existe")
