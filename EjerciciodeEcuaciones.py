class ecuanciones:
    form1= 0
    form2= 0
    form3= 0

    def formula1():
        for X in range(-4,7):
           form1= (3*X+X*3-72)
           print("La formula es 3*X+X*3-72")
           print("El valor de x es:", X)
           print("El valor de y es:", form1)
    def formula2():
        for X in range(-4,7):
           form2=(X*X-37*X)
           print("La formula es X*X-37*X")
           print("El valor de x es:", X)
           print("El valor de y es:", form2)
    def formula3():
        for X in range(-4,7):
            if  X==-1:
                print("El valor de x es:", X)
                print("ERROR: No se realiza la division entre 0")
            else:
                form3= ((X-3)/(X+1))
                print("La formula es (X-3)/(X+1)")
                print("El valor de x es:", X)
                print("El valor de y es:", form3)

ecuacion1=ecuanciones
ecuacion1.formula1()

ecuacion2=ecuanciones
ecuacion2.formula2()

ecuacion3=ecuanciones
ecuacion3.formula3()    
