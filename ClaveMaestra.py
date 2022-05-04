
while True:
    try:
        Maestra=input("Ingrese la clave maestra:")
        Clave1=""
        Clave2=""
        tamano=len(Maestra)
        for x in range(0,tamano):
            comparacion=int(Maestra[x])%2
            if comparacion==0:
                Clave2=Clave2+Maestra[x]
            else:
                Clave1=Clave1+Maestra[x]
        print("La clave maestra es:", Maestra)
        print("Los numero impares de la clave maestra son:", Clave1)
        print("Los numero pares de la clave maestra son:", Clave2)
        break
    except ValueError:
        print("La clave Maestra solo debe contener numeros, ingresela nuevamente...")
