nombre=input("Hola, cual es su nombre? ")
print("Buenas", nombre, "que tipo de cliente es usted. Cliente tipo 1, tipo 2 o tipo 3?")

Tipo=int(input(""))


if Tipo==1:
    print("entendido, los clientes tipo", Tipo, "reciben descuentos de un 30 porciento de descuento por sus compras")
elif Tipo==2:
    print("entendido, los clientes tipo", Tipo, "reciben descuentos de un 20 porciento de descuento por sus compras")
else:
    print("entendido, los clientes tipo 3 reciben descuentos de un 10 porciento de descuento por sus compras")


monto=int(input("Cual es el monto a pagar?"))

def pago_final(Tipo):

    if Tipo==1:
        pago_final=monto-monto*(30/100)
        return pago_final,monto
    elif Tipo==2:
        pago_final=monto-monto*(20/100)
        return pago_final,monto
    else:
        pago_final=monto-monto*(10/100)
        return pago_final,monto

pago_final, monto=pago_final(Tipo)
print("el monto a pagar despues del descuento es:", pago_final)

