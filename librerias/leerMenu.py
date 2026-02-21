import pandas as pd

RUTA_CSV="datos/productos.csv"
SEPARADOR=";"

def leerMenu():
    df=pd.read_csv(RUTA_CSV, sep=SEPARADOR)
    return df