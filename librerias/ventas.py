import pandas as pd

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

#print(pedido)

#1.3 Procesado de la venta
total = df_menu.loc[pedido, "Precio"].sum()
print(total)
#for id in pedido:
 #   precio=df_menu[df_menu["id"]==id]
  #  print(precio)