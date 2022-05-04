def factorial(n):
       fact = 1
       for num in range(n, 1, -1):
              fact *= num

       return fact

while True:
       x= int(input('Digite el numero para averiguar su factorial:'))
       f = factorial(x)
       print('El factorial es: ', f)
       t = input("digite 't' para continuar, sino, PLP")
       if t != "t":
              break
       else:
              print("continue")

       



       
