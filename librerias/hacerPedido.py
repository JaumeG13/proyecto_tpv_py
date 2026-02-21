#1.2 Lógica de pedido
from . import leerMenu

def hacerPedido():
    print(leerMenu.leerMenu())  #imprime el menu segun el csv
    pedido=[]                   #inicializa una lista para guardar los id del pedido
    producto=0                  #inicializa variable para el bucle

    while True:
        producto=int(input("Pide un producto: (-1 para salir) "))
        if producto == -1:  #si el pedido es -1 cierra el bucle, antes de añadirlo a la lista
            break
        pedido.append(producto)
    
    return pedido