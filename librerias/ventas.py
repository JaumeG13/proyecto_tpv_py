import pandas as pd
import json

#1.2 Lógica de pedido
RUTA_CSV="datos/productos.csv"
SEPARADOR=";"

df_menu=pd.read_csv(RUTA_CSV, sep=SEPARADOR, decimal=",")
df_menu.set_index("id", inplace=True)

print(df_menu)      #imprime el menu segun el csv
pedido=[]           #inicializa una lista para guardar los id del pedido
producto=0          #inicializa variable para el bucle

while True:
    producto=int(input("Pide un producto: (-1 para salir) "))
    if producto == -1:  #si el pedido es -1 cierra el bucle, antes de añadirlo a la lista
        break
    
    if producto in df_menu.index:  #si el producto existe en el menu lo añade a la lista, si no, muestra un mensaje de error
        pedido.append(producto)
    else:
        print("Producto no disponible")

#1.3 Procesado de la venta
productos_seleccionados=df_menu.loc[pedido]

subtotal=productos_seleccionados["Precio"].sum()
iva=subtotal*0.10
total=subtotal+iva

ticket = {
    "productos": productos_seleccionados.reset_index().to_dict(orient="records"),
    "subtotal": round(subtotal, 2),
    "iva": round(iva, 2),
    "total": round(total, 2)
}

with open("ticket.json", "w") as f:
    json.dump(ticket, f, indent=4)

print("Ticket guardado correctamente.")