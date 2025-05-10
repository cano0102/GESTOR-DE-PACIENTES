








import tkinter as tk
from tkinter import messagebox, simpledialog
from typing import TypedDict, List

class Paciente(TypedDict):
    nombre: str
    edad: int
    enfermedad: str
    medicamentos: List[str]

class Enfermero(TypedDict):
    nombre: str
    edad: int
    cedula: int
    estado: bool

class Medico(TypedDict):
    nombre: str
    edad: int
    cedula: int
    consultorio: int
    estado: bool

pacientes: List[Paciente] = []
enfermeros: List[Enfermero] = []
medicos: List[Medico] = []

def registrar_paciente():
    nombre = nombre_entry.get().capitalize()
    edad = int(edad_entry.get())
    enfermedad = enfermedad_entry.get().capitalize()
    medicamentos = medicamentos_entry.get().split(",")

    paciente = {
        "nombre": nombre,
        "edad": edad,
        "enfermedad": enfermedad,
        "medicamentos": medicamentos
    }
    pacientes.append(paciente)
    messagebox.showinfo("Registro", "✅ Paciente registrado correctamente.")
    limpiar_campos()

def consultar_paciente():
    nombre = simpledialog.askstring("Consulta", "Ingrese el nombre del paciente:").capitalize()
    for paciente in pacientes:
        if paciente["nombre"] == nombre:
            resultado = f"Nombre: {paciente['nombre']}\nEdad: {paciente['edad']}\nEnfermedad: {paciente['enfermedad']}\nMedicamentos: {', '.join(paciente['medicamentos'])}"
            messagebox.showinfo("Consulta exitosa", resultado)
            return
    messagebox.showerror("Error", "❌ Paciente no encontrado.")

def limpiar_campos():
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    enfermedad_entry.delete(0, tk.END)
    medicamentos_entry.delete(0, tk.END)

# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Gestión Médica")
root.geometry("500x400")
root.configure(bg="#f0f8ff")

# Título
titulo = tk.Label(root, text="Registro de Pacientes", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#333")
titulo.pack(pady=10)

# Nombre
tk.Label(root, text="Nombre:", bg="#f0f8ff").pack()
nombre_entry = tk.Entry(root, width=40)
nombre_entry.pack()

# Edad
tk.Label(root, text="Edad:", bg="#f0f8ff").pack()
edad_entry = tk.Entry(root, width=40)
edad_entry.pack()

# Enfermedad
tk.Label(root, text="Enfermedad:", bg="#f0f8ff").pack()
enfermedad_entry = tk.Entry(root, width=40)
enfermedad_entry.pack()

# Medicamentos
tk.Label(root, text="Medicamentos (separados por coma):", bg="#f0f8ff").pack()
medicamentos_entry = tk.Entry(root, width=40)
medicamentos_entry.pack()

# Botones
tk.Button(root, text="Registrar Paciente", command=registrar_paciente, bg="#4caf50", fg="white").pack(pady=10)
tk.Button(root, text="Consultar Paciente", command=consultar_paciente, bg="#2196f3", fg="white").pack(pady=5)
tk.Button(root, text="Salir", command=root.quit, bg="#f44336", fg="white").pack(pady=10)

# Ejecutar app
root.mainloop()



