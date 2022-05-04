def PagoFinal(tipo):
    precio=int(input("Digite el monto que paga el cliente:"))
    if tipo==1:
        pagofinal=precio-(precio*0.30)
        return pagofinal,precio
    if tipo==2:
        pagofinal=precio-(precio*0.20)
        return pagofinal,precio
    if tipo==3:
        pagofinal=precio-(precio*0.10)
        return pagofinal,precio
    
nombre=input("Digite el nombre del cliente:")
tipo=int(input("Digite el tipo de cliente(1,2,3)"))
pagofinal, precio=PagoFinal(tipo)
print(pagofinal)
