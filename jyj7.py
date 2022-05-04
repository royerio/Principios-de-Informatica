import random

lista=[]
for x in  range(0,5):
    y=str(random.randint(0,99999999999))
    lista.append(y)
    
saludo= open('saludo.txt', 'w')
txt="\n".join(lista)
saludo.write(txt)
saludo.close()

lista2=[]
saludo= open('saludo.txt', 'r')
for linea in saludo:
    linea=linea.rstrip("\n")
    lista2.append(linea)
saludo.close()

lista2.sort(reverse=True)
print(lista2)
