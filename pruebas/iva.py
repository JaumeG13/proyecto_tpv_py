#para poder importar leerMenu de librerias hace falta todo esto
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from librerias.ventas import leerMenu

pedido=[2,6] #insertando manualmente un pedido

print(leerMenu())
df_menu=leerMenu()
productos_seleccionados=df_menu.loc[pedido]

total=productos_seleccionados["Precio"].sum()
iva=total*0.10
subtotal=total-iva

print(f"Subtotal: {round(subtotal,2)}")
print(f"IVA: {round(iva,2)}")
print(f"Total: {round(total,2)}")

#2 y 6 son 6.0 + 6.0 EUR