def potencia(x, y):
       p=x**y
       return p

while True:
       try:
              x= int(input('Digite el numero:'))
              y= int(input('Digite la potencia:'))
              f = potencia(x, y)
              print('la potencia es: ', f)
              t = input("digite 't' para continuar")
              if t != "t":
                     break
              else:
                     print("siga")
       except ValueError:
              print("Error al digitar una letra por un numero")
