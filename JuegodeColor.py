

def juego(intento=1):
       while True: 
              respuesta = input("De que color es la naranja?")

              if respuesta!= "naranja":
                     if 0<intento<3:
                            print("fallo hagale de nuevo")
                            intento += 1
                            juego(intento)
                     else:
                            print("Fallo por completo")
                            comienzo=input("presione t si quiere jugar de nuevo sino plp")
                            if comienzo=="t":
                                   
                                   juego()
                            else:
                                   print("plp")
                                   break
                     

              else:
                     print("Usted gano")
                     comienzo=input("presione t si quiere jugar de nuevo sino plp")
                     if comienzo=="t":
                            
                            juego()
                     else:
                            print("plp")
                            break
                     
       
juego()
