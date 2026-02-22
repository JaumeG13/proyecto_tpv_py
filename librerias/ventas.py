import pandas as pd
import json
import logging
from datetime import datetime
import os



RUTA_CSV = "datos/productos.csv"
SEPARADOR = ";"
RUTA_LOG = "logs/ventas.log"

#Logs para ventas (1.4)
ventas_logger = logging.getLogger("ventas")
if not ventas_logger.hasHandlers():
    handler = logging.FileHandler(RUTA_LOG, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    ventas_logger.addHandler(handler)
    ventas_logger.setLevel(logging.INFO)

ventas_logger.propagate = False #Hace que solo se registre en ventas.log y no en panel.log


#1.2 Logica de pedido
def leerMenu():
    #2.4 Gestion de errores y logs
    if not os.path.exists(RUTA_CSV):
        mensaje = f"Error: No se encuentra el archivo {RUTA_CSV}"
        print(mensaje)
        ventas_logger.error(mensaje)
        return None

    df_menu=pd.read_csv(RUTA_CSV, sep=SEPARADOR, decimal=",")
    df_menu.set_index("id", inplace=True)
    return df_menu


def hacerPedido():
    df_menu=leerMenu()  

    if df_menu is None:
        return []
    
    print(df_menu)  #imprime el menu segun el csv
    pedido=[]       #inicializa una lista para guardar los id del pedido

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
    ventas_logger.info(f"Venta realizada con exito. Total: {total} EUR")