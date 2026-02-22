import pandas as pd
import json
import logging
from datetime import datetime


RUTA_CSV="datos/productos.csv"
SEPARADOR=";"
RUTA_LOG="logs/ventas.log"


#1.2 Logica de pedido
def leerMenu():
    df_menu=pd.read_csv(RUTA_CSV, sep=SEPARADOR, decimal=",")
    df_menu.set_index("id", inplace=True)
    return df_menu


def hacerPedido():
    print(leerMenu())  #imprime el menu segun el csv
    pedido=[]          #inicializa una lista para guardar los id del pedido
    producto=0         #inicializa variable para el bucle

    while True:
        producto=int(input("Pide un producto: (-1 para salir) "))
        if producto == -1:  #si el pedido es -1 cierra el bucle, antes de añadirlo a la lista
            break
        pedido.append(producto)
    
    return pedido


#1.3 Procesado de la venta
def procesarVenta(pedido):
    df_menu=leerMenu()
    productos_seleccionados=df_menu.loc[pedido]

    total=productos_seleccionados["Precio"].sum()
    iva=total*0.10
    subtotal=total-iva

    ticket = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "productos": productos_seleccionados.reset_index().to_dict(orient="records"),
        "subtotal": round(subtotal, 2),
        "iva": round(iva, 2),
        "total": round(total, 2)
    }

    return ticket


def guardarTicket(ticket):
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo=f"datos/ticket_{timestamp}.json"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(ticket, f, indent=4, ensure_ascii=False)


#1.4 Registro de venta
def registrarLog(total):
    logging.basicConfig(
        filename=RUTA_LOG,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info(f"Venta realizada con exito. Total: {total} EUR")