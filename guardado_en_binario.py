import os.path
import random
import pickle


def Llenado():
    lista=[]
    for x in range(0,5):
        y=random.randint(0,9999999999999)
        lista.append(y)
    archivo=open("numeros.txt","wb")
    pickle.dump(lista,archivo)
    archivo.close()
    lista=[]
    
def Mostrar():
    if(os.path.exists("numeros.txt")):
        archivo=open("numeros.txt","rb")
        lista=pickle.load(archivo)
        lista.sort(reverse=True)
        alista=sorted(lista)
        print(alista)
        print(lista)
    else:
        print("El archivo: numeros.txt no existe")

while True:
    opcion=input("llenado:1,mostrar:2,salir:3")
    if opcion=="1":
        Llenado()        
        opcion=""
    if opcion=="2":
        Mostrar()
        opcion=""
    if opcion=="3":
        print("programa terminado")
        break
        
