import random
import time

def Categoria():
    categoria=input(" Digite 1 para animales salvajes\n Digite 2 para animales domesticos\n Digite 3 para frutas\n Digite 4 para paises exoticos\n Digite 5 para vehiculos\n Tu respuesta es:")
    if categoria=="1":
        return(categoria)
    if categoria=="2":
        return(categoria)
    if categoria=="3":
        return(categoria)
    if categoria=="4":
        return(categoria)
    if categoria=="5":
        return(categoria)
    else:
        print("Digite una categoria apropiada(numero del 1 al 5)")
        Categoria()
        
def Instrucciones(nombre):
    print("Bienvenido al juego",nombre)
    print("Intrucciones:\n 1-Debe adivinar un palabra, letra por letra.\n 2-Escojer una categoria de inmediato.")
    categoria=Categoria()
    print(" 3-Si pierde se le añade una parte al dibujo del ahorcado, ejemplo:")
    print("Antes de fallar:")
    print(ahorcado[0])
    print("Despues de fallar:")
    print(ahorcado[1])
    print(" 4-El juego termina cuando el dibujo del muñeco esta completo, buena suerte")
    return categoria    

def Palabra(categoria):
    if categoria==1:
        return (lista1[random.randint(0,14)])
    if categoria==2:
        return (lista2[random.randint(0,14)])
    if categoria==3:
        return (lista3[random.randint(0,14)])
    if categoria==4:
        return (lista4[random.randint(0,14)])
    if categoria==5:
        return (lista5[random.randint(0,14)])
        
def inicio():
    adivina=""
    nombre=input("Digite su nombre para jugar:")
    categoria=int(Instrucciones(nombre))
    palabra=str(Palabra(categoria))
    tiempoi=time.time()
    for x in range(0, len(palabra)):
        adivina=adivina+"-"
    print(ahorcado[0])
    print(adivina)
    return adivina, palabra, nombre,tiempoi

def Ahorcado(palabra, adivina,intento):
    letra=input("Digite una letra:")
    temp=""
    if len(letra)==1:
        abc="abcdefghijklmnñopqrstuvwxyzáéíóú"
        sletras=abc.count(letra)        
        if sletras!=0:
            conteo=palabra.count(letra)            
            if conteo!=0:
                iletras=adivina.count(letra)
                if iletras!=0:
                    print("Ya ingreso esa letra pruebe con otra, gracias")
                    
                else:
                    for a in range(0, len(palabra)):
                        if letra==palabra[a]:
                            temp=temp+letra                
                        else:
                            temp=temp+adivina[a]
            else:
                intento+=1
                temp=adivina                
        else:
            print("No ingrese letras en mayuscula, tampoco numeros,solo estas: abcdefghijklmnñopqrstuvwxyz, gracias")
            intento+=1
            temp=adivina
                
    else:
        print("Ingrese letra por letra, una a la vez, gracias")
        intento+=1
        temp=adivina
        
    adivina=temp   
    temp=""
    
    print(ahorcado[intento-1])
    print(adivina) 
    return palabra, adivina, intento 
tiempoi=0.0        
tiempof=0.0
lista1=["león", "lobo", "elefante", "tiburón", "cocodrilo", "jirafa", "gorila", "leopardo", "canguro", "cebra", "rinoceronte", "avestruz", "oso","tigre", "jaguar"]
lista2=["perro", "gato", "pez", "hamster", "gallina", "pato", "vaca", "burro", "caballo", "gallo", "pollo", "cerdo", "oveja", "cabra","conejo"]
lista3=["mango", "sandia", "papaya", "manzana", "naranja", "kiwi", "jocote", "fresa", "limon", "melon", "carambola", "banano", "coco", "piña", "cereza"]
lista4=["australia","suecia","dinamarca","egipto","nigeria","croacia","ucrania","etiopia","tailandia","turquia","islandia","noruega","marruecos","madagascar","tanzania"]
lista5=["yate","submarino","velero","motocicleta","bicicleta","patineta","cuadraciclo","trailer","lancha","avion","avioneta","globo","autobus","tren","metro"]
ahorcado=[" +---+  \n !   |  \n     |  \n     |  \n     |  \n     |  \n========="," +---+  \n !   |  \n O   |  \n     |  \n     |  \n     |  \n========="," +---+  \n !   |  \n O   |  \n |   |  \n     |  \n     |  \n========="," +---+  \n !   |  \n O   |  \n |\  |  \n     |  \n     |  \n========="," +---+  \n !   |  \n O   |  \n/|\  |  \n     |  \n     |  \n========="," +---+  \n !   |  \n O   |  \n/|\  |  \n |   |  \n     |  \n========="," +---+  \n !   |  \n O   |  \n/|\  |  \n |   |  \n/    |  \n========="," +---+  \n !   |  \n O   |  \n/|\  |  \n |   |  \n/ \  |  \n========="," +---+  \n !   |  \n X   |  \n/|\  |  \n |   |  \n/ \  |  \n========="]
intento=0


while True:
    
    if intento == 0:
        intento=1
        adivina, palabra, nombre, tiempoi=inicio()
        palabra, adivina,intento=Ahorcado(palabra,adivina,intento)      
                
    if 1<=intento <9:
        palabra, adivina,intento=Ahorcado(palabra,adivina,intento)

    if palabra==adivina:
        tiempof=time.time()
        print("Felicidades",nombre," has GANADO en un tiempo de:",(tiempof-tiempoi),"s")
        
        continuar=input("Digite t si desea jugar nuevamente:")
        if continuar=="t":
            intento=0
        else:
            print("Muchas gracias por jugar, espero vuelva pronto")
            break
    if intento>=9:
        tiempof=time.time()
        print("Lo siento",nombre," has PERDIDO en un tiempo de:",(tiempof-tiempoi),"s")
        continuar=input("Digite t si desea jugar nuevamente:")
        if continuar=="t":
            intento=0
        else:
            print("Muchas gracias por jugar, espero vuelva pronto")
            break
        
        
    
