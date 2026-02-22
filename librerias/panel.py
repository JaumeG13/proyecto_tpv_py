import json
import logging
import pandas as pd
import glob

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
            print(f"------ Panel {nombre_pizzeria} ------")
            return True

        contador+=1
        print(f"ERROR: Contraseña incorrecta intentos restantes: {3-contador}")

    logging.error("Inicio de sesión fallido después de 3 intentos.")


#2.3 Analisis de datos con pandas
def estadisticas():
    archivos = glob.glob("datos/ticket_*.json")

    df_estadisticas = pd.DataFrame([
        pd.read_json(archivo)["total"][0]
        for archivo in archivos
    ], columns=["total"])

    print("Estadísticas de ventas:")
    print(f"Nº de ventas: {len(df_estadisticas)}")
    print(f"Total ingresos: {df_estadisticas['total'].sum()} EUR")
    print(f"Media ticket: {df_estadisticas['total'].mean():.2f} EUR")
