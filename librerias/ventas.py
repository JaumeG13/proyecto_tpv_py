import pandas as pd
import json

#1.2 Lógica de pedido
RUTA_CSV="datos/productos.csv"
SEPARADOR=";"

df_menu=pd.read_csv(RUTA_CSV, sep=SEPARADOR, decimal=",")

print(df_menu)      #imprime el menu segun el csv
pedido=[]           #inicializa una lista para guardar los id del pedido
producto=0          #inicializa variable para el bucle

while True:
    producto=int(input("Pide un producto: (-1 para salir) "))
    if producto == -1:  #si el pedido es -1 cierra el bucle, antes de añadirlo a la lista
        break
    pedido.append(producto)

#1.3 Procesado de la venta
subtotal=df_menu.loc[pedido, "Precio"].sum()
iva=subtotal*0.10
total=subtotal+iva

ticket = {
    "productos": "nombre",
    "subtotal": round(subtotal, 2),
    "iva": round(iva, 2),
    "total": round(total, 2)
}