from librerias.ventas import hacerPedido, procesarVenta, guardarTicket, registrarLog
from librerias.panel import accesoPanel


def main():
    while True:
        opcion = int(input("Seleccione una opción:\n1. Hacer un pedido\n2. Acceder al panel de control\n3. Salir\n"))
        match opcion:
            case 1:
                pedido = hacerPedido()

                if len(pedido) == 0:
                    print("No se ha realizado ningun pedido.")
                    return

                ticket = procesarVenta(pedido)

                guardarTicket(ticket)
                registrarLog(ticket["total"])

                print("Venta realizada correctamente.")
                print("Total a pagar:", ticket["total"], "€")
            case 2:
                accesoPanel()
            case 3:
                print("Saliendo del programa.")
                return
            case _: 
                print("Error: Introduzca una opción correcta.")

if __name__ == "__main__":
    main()

# Fin de la estructura lógica