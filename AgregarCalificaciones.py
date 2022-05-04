def Guardado(lista,nombre,puntuacion):
    notas= open('notas.txt', 'a')    
    txt=nombre+":\n"+"\n".join(lista)+"\n"+puntuacion+"\n"
    notas.write(txt)
    notas.close()
def Nota(nombre):
    lista=[]    
    for i in range(0,4):
        nota=input("Ingrese la nota del estudiante")
        if 0>=int(nota)>=100:
            print("Ingrese una nota entre 0 y 100")
            Nota(nombre)
        else:
            lista.append(nota)
        
    return lista
def Puntuacion(promedio):
    puntuacion=""
    if 100>=promedio>=90:
        puntuacion="A"
    if 89>=promedio>=80:
        puntuacion="B"
    if 79>=promedio>=70:
        puntuacion="C"
    if 69>=promedio>=60:
        puntuacion="D"
    if 59>=promedio>=0:
        puntuacion="E" 
    return puntuacion

while True:
    lista=[]
    try:
        nombre=input("Ingrese el nombre del estudiante:")
        lista=Nota(nombre)
        c=0
        for p in lista:
            c=c+int(p)
        promedio=(c/4)
        puntuacion=Puntuacion(promedio)
        print("Su puntuacion es:",puntuacion)
        Guardado(lista,nombre,puntuacion)
        continuar=input("Digite t si desea continuar agregando notas de estudianes")
        if continuar=="t":
            print("Continue")
        else:
            print("Gracias por usar esta aplicasion, espero vuelva pronto")
            break


    except ValueError:
        print("Oooooooop,ha ocurrido un error intente nuevamente")
