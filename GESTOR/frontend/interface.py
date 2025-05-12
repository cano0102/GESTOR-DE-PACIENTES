import tkinter as tk
from tkinter import messagebox, simpledialog
from typing import List, TypedDict

# ----- TIPADO -----
class Paciente(TypedDict):
    Nombre: str
    Edad: int
    Enfermedad: str
    Medicamentos: List[str]
    Médico_asignado: str
    Enfermero_asignado: str

class Enfermero(TypedDict):
    Nombre: str
    Edad: int
    Cedula: int
    Estado: bool

class Medico(TypedDict):
    Nombre: str
    Edad: int
    Cedula: int
    Consultorio: int
    Estado: bool

# ----- DATOS -----
pacientes: List[Paciente] = []
enfermeros: List[Enfermero] = []
medicos: List[Medico] = []

# ----- FUNCIONES -----
def registro_de_pacientes():
    nombre = nombre_entry.get().capitalize()
    edad = int(edad_entry.get())
    enfermedad = enfermedad_entry.get().capitalize()
    medicamentos = medicamentos_entry.get().split(",")
    paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Enfermedad": enfermedad,
        "Medicamentos": medicamentos,
        "Médico_asignado": "Ninguno",
        "Enfermero_asignado": "Ninguno"
    }
    pacientes.append(paciente)
    messagebox.showinfo("Registro", "✅ Paciente registrado correctamente.")
    limpiar_campos()

def consultar_paciente():
    nombre = simpledialog.askstring("Consulta", "Nombre del paciente:").capitalize()
    for p in pacientes:
        if p["Nombre"] == nombre:
            info = f"""
            Nombre: {p["Nombre"]}
            Edad: {p["Edad"]}
            Enfermedad: {p["Enfermedad"]}
            Medicamentos: {', '.join(p["Medicamentos"])}
            Médico asignado: {p["Médico_asignado"]}
            Enfermero asignado: {p["Enfermero_asignado"]}
            """
            messagebox.showinfo("Consulta", info)
            return
    messagebox.showerror("Error", "❌ Paciente no encontrado.")

def eliminar_paciente():
    nombre = simpledialog.askstring("Eliminar", "Nombre del paciente:").capitalize()
    for p in pacientes:
        if p["Nombre"] == nombre:
            pacientes.remove(p)
            messagebox.showinfo("Eliminado", "✅ Paciente eliminado.")
            return
    messagebox.showerror("Error", "❌ Paciente no encontrado.")

def editar_paciente():
    nombre = simpledialog.askstring("Editar", "Nombre del paciente:").capitalize()
    for p in pacientes:
        if p["Nombre"] == nombre:
            campo = simpledialog.askstring("Editar", "Campo a editar (Nombre, Edad, Enfermedad, Medicamentos):").capitalize()
            if campo == "Nombre":
                nuevo = simpledialog.askstring("Nuevo nombre", "Ingrese nuevo nombre:").capitalize()
                p["Nombre"] = nuevo
            elif campo == "Edad":
                nuevo = int(simpledialog.askstring("Nueva edad", "Ingrese nueva edad:"))
                p["Edad"] = nuevo
            elif campo == "Enfermedad":
                nuevo = simpledialog.askstring("Nueva enfermedad", "Ingrese nueva enfermedad:").capitalize()
                p["Enfermedad"] = nuevo
            elif campo == "Medicamentos":
                nuevo = simpledialog.askstring("Nuevos medicamentos", "Ingrese medicamentos separados por coma:")
                p["Medicamentos"] = nuevo.split(",")
            messagebox.showinfo("Editado", "✅ Paciente editado.")
            return
    messagebox.showerror("Error", "❌ Paciente no encontrado.")

def asignar_medico_enfermero():
    nombre = simpledialog.askstring("Asignar", "Nombre del paciente:").capitalize()
    for p in pacientes:
        if p["Nombre"] == nombre:
            medico = simpledialog.askstring("Médico", "Nombre del médico a asignar:").capitalize()
            enfermero = simpledialog.askstring("Enfermero", "Nombre del enfermero a asignar:").capitalize()
            for m in medicos:
                if m["Nombre"] == medico and m["Estado"]:
                    for e in enfermeros:
                        if e["Nombre"] == enfermero and e["Estado"]:
                            p["Médico_asignado"] = medico
                            p["Enfermero_asignado"] = enfermero
                            messagebox.showinfo("Asignación", "✅ Asignación completada.")
                            return
            messagebox.showerror("Error", "Médico o enfermero no disponibles.")
            return
    messagebox.showerror("Error", "❌ Paciente no encontrado.")

def limpiar_campos():
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    enfermedad_entry.delete(0, tk.END)
    medicamentos_entry.delete(0, tk.END)

# ----- INTERFAZ -----
root = tk.Tk()
root.title("Gestión Médica")
root.geometry("550x500")
root.config(bg="#e0f7fa")

tk.Label(root, text="Sistema de Gestión Médica", font=("Arial", 18, "bold"), bg="#e0f7fa").pack(pady=10)

# Entrada de datos
frame = tk.Frame(root, bg="#ffffff", bd=3, relief="groove")
frame.pack(pady=20)

tk.Label(frame, text="Nombre", bg="white").grid(row=0, column=0, padx=10, pady=5)
nombre_entry = tk.Entry(frame, width=30)
nombre_entry.grid(row=0, column=1)

tk.Label(frame, text="Edad", bg="white").grid(row=1, column=0, padx=10, pady=5)
edad_entry = tk.Entry(frame, width=30)
edad_entry.grid(row=1, column=1)

tk.Label(frame, text="Enfermedad", bg="white").grid(row=2, column=0, padx=10, pady=5)
enfermedad_entry = tk.Entry(frame, width=30)
enfermedad_entry.grid(row=2, column=1)

tk.Label(frame, text="Medicamentos (coma)", bg="white").grid(row=3, column=0, padx=10, pady=5)
medicamentos_entry = tk.Entry(frame, width=30)
medicamentos_entry.grid(row=3, column=1)

# Botones
tk.Button(root, text="Registrar Paciente", bg="#4caf50", fg="white", width=20, command=registro_de_pacientes).pack(pady=5)
tk.Button(root, text="Consultar Paciente", bg="#2196f3", fg="white", width=20, command=consultar_paciente).pack(pady=5)
tk.Button(root, text="Editar Paciente", bg="#ff9800", fg="white", width=20, command=editar_paciente).pack(pady=5)
tk.Button(root, text="Eliminar Paciente", bg="#f44336", fg="white", width=20, command=eliminar_paciente).pack(pady=5)
tk.Button(root, text="Asignar Médico y Enfermero", bg="#9c27b0", fg="white", width=25, command=asignar_medico_enfermero).pack(pady=10)

tk.Button(root, text="Salir", command=root.quit, bg="#607d8b", fg="white", width=15).pack(pady=10)

root.mainloop()



