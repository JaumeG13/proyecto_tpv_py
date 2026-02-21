#Jaume Genaro van der Heide
import examen
import random

alumno=[]

while True:
    print("----------Examen U4----------")
    print("1) Introducir alumno")
    print("2) Nota media de un alumno")
    print("3) Trimestres aprobados")
    print("4) Beca")
    print("5) Media grupo")
    print("6) Salir")
    opcion=int(input("Introduzca una opción (1-6): "))
    
    match opcion:
        case 1:
            nombre=(input("Introduzca un nombre: "))
            apellido=(input("Introduzca un apellido: "))
            nota1=round(random.uniform(0,10),1)
            nota2=round(random.uniform(0,10),1)
            nota3=round(random.uniform(0,10),1)
            print(examen.crear_alumno(alumno, nombre, apellido, nota1, nota2, nota3))

        case 2:
            lista=["Jaume", "van der Heide", 10, 8.7, 7.8]
            print(f"Media del alumno: {round(examen.calcular_media(lista),1)}")

        case 3:
            lista=["Jaume", "van der Heide", 10, 8.7, 4.9]
            print(f"Ha aprobado {examen.trimestres_aprobados(lista)} trimestres.")

        case 4:
            lista=["Roberto", "Guerrero", 10, 8.7, 9]
            print(examen.tiene_beca(lista))

        case 5:
            alumno1=["Jaume", "van der Heide", 1, 8.7, 4.9]
            alumno2=["Roberto", "Guerrero", 4.9, 8.7, 9]
            ficheros=("a.txt", "b.txt", "c.txt")
            print(examen.media_grupo_fichero(alumno1, alumno2, ficheros))

        case 6:
            print("Saliendo ...")
            break

        case _:
            print("Error: Introduzca una opción correcta.")
            