from . import leerMenu

def hacerPedido():
    print(leerMenu.leerMenu())
    pedido=[]
    producto=0

    while True:
        producto=int(input("Pide un producto: (-1 para salir) "))
        if producto == -1:
            break
        pedido.append(producto)
    
    return pedido