import json
import logging

RUTA_JSON="datos/config.json"
RUTA_LOG="logs/panel.log"

#Conseguir valor de la contraseña
with open(RUTA_JSON, "r", encoding="utf-8") as f:
    config=json.load(f)
password=config["password"]
nombre_pizzeria=config["nombre_pizzeria"]

#Logging inicio de sesión
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def accesoPanel():
    contador=0
    while contador < 3:
        intento=input("Introduzca la contraseña de acceso: ")
        if intento == password:
            print("Acceso concedido.")
            logging.info("Inicio de sesión correcto.")
            print(f"---------- {nombre_pizzeria} ----------")
            return True

        contador+=1
        print(f"ERROR: Contraseña incorrecta intentos restantes: {3-contador}")

    logging.error("Inicio de sesión fallido después de 3 intentos.")

