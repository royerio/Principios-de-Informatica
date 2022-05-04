nota1 = int(input("ingrese la primera nota: "))
nota2 = int(input("ingrese la segunda nota: "))
nota3 = int(input("ingrese la tercera nota: "))
nota4 = int(input("ingrese la cuarta nota: "))

promedio = int((nota1 + nota2 + nota3 + nota4)/4)
print(promedio)

if 0<=promedio<70:
    print("Obtuvo E")
elif 60<=promedio<70:
    print("Obtuvo D")
elif 70<=promedio<80:
    print("Obtuvo C")
elif 80<=promedio<90:
    print("Obtuvo B")
elif 90<=promedio<=100:
    print("Obtuvo A")

