from librerias.ventas import hacerPedido, procesarVenta, guardarTicket, registrarLog


def main():
    pedido = hacerPedido()

    if len(pedido) == 0:
        print("No se ha realizado ningun pedido.")
        return

    ticket = procesarVenta(pedido)

    guardarTicket(ticket)
    registrarLog(ticket["total"])

    print("Venta realizada correctamente.")
    print("Total a pagar:", ticket["total"], "€")


if __name__ == "__main__":
    main()

# Fin de la estructura lógica