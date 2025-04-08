# Estoy buscando un programa de gestión de pacientes para una enfermería. El programa debe ser fácil de usar y permitirme gestionar la información de los pacientes de manera eficiente.

# Requisitos:
# 1. Registro de pacientes: Debe permitirme registrar nuevos pacientes con su nombre, edad, enfermedad y otros detalles relevantes.
# 2. Gestión de pacientes: Debe permitirme buscar, editar y eliminar pacientes existentes.
# 3. Asignación de médicos y enfermeras: Debe permitirme asignar médicos y enfermeras a cada paciente.
# 4. Interfaz de usuario: Debe tener una interfaz de usuario fácil de usar y intuitiva.
# 5. Almacenamiento de datos: Debe almacenar los datos de los pacientes de manera segura y eficiente.

# Características adicionales:
# 1. Validación de datos: Debe validar los datos ingresados para asegurarse de que sean correctos y consistentes.
# 2. Mensajes de error: Debe mostrar mensajes de error claros y concisos en caso de que ocurran errores.
# 3. Ayuda y documentación: Debe incluir ayuda y documentación para que pueda aprender a usar el programa de manera efectiva.

# Plataforma y lenguaje:
# El programa debe ser desarrollado en Python y debe ser compatible con sistemas operativos Windows, macOS y Linux.

# Entrega:
# El programa debe ser entregado con un manual de usuario y una guía de instalación. También debe incluir cualquier dependencia o biblioteca requerida para su funcionamiento.
enfermos = []

def registro_de_pacientes():
    pacientes = {}
    nombre = str(input("Dame el nombre del paciente: "))
    pacientes["nombre_paciente"] = nombre
    edad = str(input("Dame la edad del paciente: "))
    pacientes["edad_paciente"] = edad
    emfermedad = str(input("Describe la emfermedad del pacientes: "))
    pacientes["enfermedad"] = emfermedad
    medicamnetos = str(input("Dame los medicamentos del paciente"))
    enfermos["medicamentos"] = medicamnetos
    enfermos.append(pacientes)

def registrar_medicos():
    pass

def registrar_enfermaras():
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
    print("1. Para registrar paciente")
    print("2. Para registrar medicos")
    print("3. Para registrar enfermeras")
    print("4. Para consultar un paciente")
    print("5 Para eliminar un paciente")
    print("6 Para editar la informacion de un paciente")
    print("7 Para asignar enfermeros y medicos a pacientes")
    print("8 Para salir")

while True:
    menu()
    opcion = int(input("Dame la opcion que deseas realizar"))

    if opcion == 1:
        registro_de_pacientes()
    elif opcion == 2:
        registrar_medicos()
    elif opcion == 3:
        registrar_enfermaras()
    elif opcion == 4:
        consultar_paciente()
    elif opcion == 5:
        eliminar_paciente()
    elif opcion == 6:
        editar_paciente()
    elif opcion == 7:
        asignación_de_médicos_y_enfermeras()
    elif opcion == 8:
        print("gracias por utilizar este programa")
        break
    else:
        print("esta opcion es invalidad")

    