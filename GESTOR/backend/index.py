from typing import TypedDict, List #AGREGANDO TIPADO DE VARIABLES

class Paciente(TypedDict):
    #CREANDO LISTA QUE TENDRA EL TIPADO DE LAS CLAVES
    nombre: str
    edad: int
    enfermedad: str
    medicamentos: List[str]

class Enfermero(TypedDict):
    #CREANDO LISTA QUE TENDRA EL TIPADO DE LAS CLAVES
    nombre: str
    edad: int
    cedula: int

class Medico(TypedDict):
    #CREANDO LISTA QUE TENDRA EL TIPADO DE LAS CLAVES
    nombre: str
    especialidad: str
    cedula: int
    consultorio: int

pacientes: List[Paciente] = []
enfermeros: List[Enfermero] = []
medicos: List[Medico] = []

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

def registrar_enfermeras(nombre: str, edad: int, cedula: int):
        enfermero = {
        "Nombre": nombre,
        "Edad": edad,
        "cedula" : cedula
    }
        enfermeros.append(enfermero)
        print("✅ Enfermeros registrado correctamente.")
        print(enfermero)

def registrar_medicos(nombre: str,edad: int,cedula: int,consultorio: int):
    medico = {
        "Nombre": nombre,
        "Edad": edad,
        "Cedula": cedula,
        "Consultorio": consultorio
    }
    medicos.append(medico)
    print("✅ Medico registrado correctamente.")
    print(medico)

def consultar_paciente():
    nombre_paciente = str(input("DAME EL NOMBRE DEL PACIENTE A CONSULTAR:")).capitalize()
    for paciente in pacientes:
        if paciente["Nombre"] == nombre_paciente:
            print("Busqueda exitosa👌")
            print("Nombre: ",nombre_paciente)
            print("Edad: ",paciente["Edad"])
            print("Enfermedad:",paciente["Enfermedad"])
            print("Medicamentos:",paciente["Medicamentos"])
            return #SALE SI YA ENCONTRO EL PACIENTE
        else:
            print("!NO ESTA REGISTRADO¡")

def eliminar_paciente():
    nombre_paciente = str(input("DAME EL NOMBRE DEL PACIENTE A ELIMINAR:")).capitalize()
    for paciente in pacientes:
        if paciente["Nombre"] == nombre_paciente:
            pacientes.remove(paciente)
            print("✅ Paciente eliminado correctamente.")
            return
    print("❌ Paciente no encontrado.")

def editar_paciente():
    nombre_paciente = str(input("Dame el nombre del paciente a editar: ")).capitalize()

    for paciente in pacientes:

        if paciente["Nombre"] == nombre_paciente:

            opcion_a_editar = str(input("Dame una opcion para editar escribe alguna de estas:nombre , edad ,enfermedad , medicamentos")).capitalize()

            if "Nombre" == opcion_a_editar :

                del paciente["Nombre"]
                nombre_nuevo = str(input("Dame el nombre nuevo: ")).capitalize()
                paciente["Nombre"] = nombre_nuevo
                print(paciente)

            elif opcion_a_editar == "Edad":

                del paciente["Edad"]
                edad_nueva = int(input("Dame la edad nueva:"))
                paciente["Edad"] = edad_nueva
                print(paciente)

            elif opcion_a_editar == "Enfermedad":

                del paciente["Enfermedad"]
                enfermedad_nuevo = str(input("Dame la enfermedad nueva: ")).capitalize()
                paciente["Enfermedad"] = enfermedad_nuevo
                print(paciente)

            elif opcion_a_editar == "Medicamentos":

                del paciente["Medicamentos"]
                medicamentos_nuevo = str(input("Dame los medicamentos nuevos (SEPARADOS POR COMA) : ")).split(",") 
                paciente["Medicamentos"] = medicamentos_nuevo
                print(paciente)
            else:
                print("la opcion es invalidad")
        else:
            print("no esta el paciente")



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

def app():
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

if __name__ == "__main__":
    app() #CORRE LA APP PRINCIPAL