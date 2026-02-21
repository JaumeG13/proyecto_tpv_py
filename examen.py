#Jaume Genaro van der Heide
import random
import math

def crear_alumno(alumno, nombre, apellido, nota1, nota2, nota3):
    alumno.append(nombre)
    alumno.append(apellido)
    alumno.append(nota1)
    alumno.append(nota2)
    alumno.append(nota3)
    return alumno

def calcular_media(lista): #statistics.mean(total) solo me da problemas
    total=0
    for i in range(3):
        total+=lista[i+2]

    media=total/3
    
    return media

def trimestres_aprobados(lista):
    aprobados=0
    for i in range(3):
        if lista[i+2] >= 5:
            aprobados+=1
    return aprobados

def tiene_beca(lista):
    nombre=lista[0] #sacar nombre de la lista, sé que esta en la posición 0

    if calcular_media(lista) >= 8 and trimestres_aprobados(lista) == 3:
        beca=f"Estimado alumno {nombre}, sí tienes beca"
        return beca
    else:
        beca=f"Estimado alumno {nombre}, no tienes beca"
        return beca

def media_grupo_fichero(alumno1, alumno2, ficheros):
    fichero=random.choice(ficheros) #elegir un fichero aleatorio

    media_trimestre1=(alumno1[2]+alumno2[2])/2 #calcular media
    
    with open(fichero, "w") as f:   #escribir la media (como cadena) al fichero elegido
        f.write(str(media_trimestre1))

    with open(fichero, "r") as f:   #leer contenido del fichero, guardar como variable "linea"
        linea=f.readline()

    if media_trimestre1 >= 5:   #si la media es mayor que 5, devolver el fichero, su contenido y la raizq
        raiz=math.sqrt(media_trimestre1)
        return fichero, linea, raiz
    else:                       #si no lo es, devolver solo el fichero y su contenido
        return fichero, linea