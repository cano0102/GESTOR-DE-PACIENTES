from typing import TypedDict, List #AGREGANDO TIPADO DE VARIABLES

class Paciente(TypedDict):
    #CREANDO LISTA QUE TENDRA EL TIPADO DE LAS CLAVES
    nombre: str
    edad: int
    enfermedad: str
    medicamentos: List[str]


pacientes: List[Paciente] = []
def registro_de_pacientes(nombre: str, edad: int, enfermedad: str, medicamentos: List[str]) -> None:
    paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Enfermedad": enfermedad,
        "Medicamentos": medicamentos
    }
    pacientes.append(paciente)
    print("✅ Paciente registrado correctamente.")
    print(paciente)

class enfermero(TypedDict):
    #CREANDO LISTA QUE TENDRA EL TIPADO DE LAS CLAVES
    nombre: str
    edad: int
    cedula: int
    


enfermeros: List[enfermero] = []

def registrar_enfermeras(nombre: str, edad: int, cedula: int):
        enfermero = {
        "Nombre": nombre,
        "Edad": edad,
        "cadula" : cedula
    }
        enfermeros.append(enfermero)
        print("✅ Enfermeros registrado correctamente.")
        print(enfermero)

def registrar_medicos():
    pass

def consultar_paciente():
    pass
def eliminar_paciente():
    pass
def editar_paciente():
    pass

def asignación_de_médicos_y_enfermeras():
    pass

def menu():
    print("---OPCIONES A ELEGIR---")
    print("-"*30)
    print("1. Para registrar paciente")
    print("2. Para registrar enfermeras")
    print("3. Para registrar medicos")
    print("4. Para consultar un paciente")
    print("5 Para eliminar un paciente")
    print("6 Para editar la informacion de un paciente")
    print("7 Para asignar enfermeros y medicos a pacientes")
    print("8 Para salir")

while True:
    menu()
    opcion = int(input("INGRESA UNA OPCION: "))
    if opcion == 1:
        nombre: str = input("INGRESA EL NOMBRE DEL PACIENTE: ").capitalize()
        edad: int = int(input("INGRESA LA EDAD DEL PACIENTE: "))
        enfermedad: str = input("INGRESA LA CONDICION DEL PACIENTE: ").capitalize()
        medicamentos = input("INGRESA LOS MEDICAMENTOS DEL PACIENTE (SEPARADOS POR COMA): ").split(",") #SE CONVIERTE EN UNA LISTA PARA AGREGAR A LA FUNCION
        registro_de_pacientes(nombre,edad,enfermedad,medicamentos)
    elif opcion == 2:
        nombre: str = input("INGRESA EL NOMBRE DEL ENFERMER@: ").capitalize()
        edad: int = int(input("INGRESA LA EDAD  DEL ENFERMER@: "))
        cedula: int = int(input("INGRESA LA CEDULA  DEL ENFERMER@: "))
        registrar_enfermeras(nombre,edad,cedula)
    elif opcion == 3:
        registrar_medicos()
    elif opcion == 4:
        consultar_paciente()
    elif opcion == 5:
        eliminar_paciente()
    elif opcion == 6:
        editar_paciente()
    elif opcion == 7:
        asignación_de_médicos_y_enfermeras()
    elif opcion == 8:
        print("gracias por utilizar este programa.")
        break
    else:
        print("esta opcion es invalida.")
