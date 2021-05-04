# El reto consta de lo siguiente :
# - Tomando como base la solucion del reto anterior (Nivel 3), vamos a crear 2 modulos : 
#  1) Alumnos
#  2) Profesores (Docentes)

# En cada modulo vamos a tener las siguientes opciones Listar y Crear
# Para la creacion del Alumno se necesita : Nombre, notas, nota mayor, nota menor y promedio
# Para la crecion del Docente se necesita: Nombre, Edad y DNI (Identificación)
# Esto se guardara en un txt o en un json (a elección)

from time import sleep
from json import load, decoder, dump


data = {
    'alumnos':[],
    'docentes':[]
    }

class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

class Docente:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def interfaz(self):
        while True:
            print("\n------ Elija una opción ------")
            print("1- Agregar Datos de Alumno. ")
            print("2- Agregar Datos de Docente. ")
            print("3- Mostrar Datos. ")
            print("4- Salir del Programa!")
            
            print("------------------------------")
            opcion = input(":: ")
            print("------------------------------")

            if opcion == "1":
                self.agregar_alumno()
            elif opcion == "2":
                self.agregar_docente()
            elif opcion == "3":
                self.mostrar_datos()
            elif opcion == "4":
                print("Adiós!")
                break
            else:
                print("La opción ingresada es incorrecta!")
                print("===================================\n")

    def agregar_alumno(self):
        lista_notas = []
        nombre = input("Ingrese nombre del alumno: ")
        cant = int(input("Ingrese la cantidad de notas: "))

        for i in range(cant):
            nota = int(input(f"Ingrese la nota {i+1}: "))
            lista_notas.append(nota)

        crear_alumno = Alumno(nombre, lista_notas)

        datos = {
            "Nombre": crear_alumno.nombre,
            "Notas": crear_alumno.notas,
            "Nota Maxima": max(crear_alumno.notas),
            "Nota Minima": min(crear_alumno.notas),
            "Nota Promedio": sum(crear_alumno.notas)/cant
        }

        self.guardar_persona(datos, "alumnos")

    def agregar_docente(self):
        nombre = input("Ingresar nombre del Docente: ")
        edad = input("Ingresar la edad del Docente: ")
        dni = input("Ingresar el DNI del Docente: ")

        crear_docente = Docente(nombre, edad, dni)

        datos = {
            "nombre": crear_docente.nombre,
            "edad": crear_docente.edad,
            "dni": crear_docente.dni
        }

        self.guardar_persona(datos, "docentes")

    def guardar_persona(self, dato, tipo):
        if tipo=="alumnos":
            data["alumnos"].append(dato)
            doc = open("datos_alumnos.json", "w")
            dump(data[tipo], doc, indent=4)
            doc.close()
            
        elif tipo=="docentes":
            data["docentes"].append(dato)
            doc = open("datos_docentes.json", "w")
            dump(data[tipo], doc, indent=4)
            doc.close()

        else:
            pass

    def refresh_datos(self):
        try:
            doc = open("datos_alumnos.json", "r")
            data["alumnos"] = load(doc)
            doc.close()

            doc = open("datos_docentes.json", "r")
            data["docentes"] = load(doc)
            doc.close()

        except FileNotFoundError:
            doc = open("datos_alumnos.json", "w")
            doc.close()
            
            doc = open("datos_docentes.json", "w")
            doc.close()

        # except decoder.JSONDecodeError:
        #     print("\nNo hay datos aun")

    def mostrar_datos(self):
        try:
            print(" --- Mostrar --- ")
            print("1- Alummnos")
            print("2- Docentes")
            dopt = int(input(":: "))

            if dopt == 1:
                for alumno in data["alumnos"]:
                    print(" ")
                    for key in alumno:
                        print(key,":",alumno[key]) 
                sleep(2)      
            if dopt == 2 :
                for docente in data["docentes"]:
                    print(" ")
                    for key in docente:
                        print(key,":",docente[key])
                sleep(2)    
            else:
                print("El valor no es correcto!")        
        except Exception:
            print("El valor ingresado es errado!")

class Start(Alumno, Docente):
    def __init__(self):
        try:
            self.refresh_datos()
            self.interfaz()

        except KeyboardInterrupt:
            print('Error de programa!\n')

Start()






































