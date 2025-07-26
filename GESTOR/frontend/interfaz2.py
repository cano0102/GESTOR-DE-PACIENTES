import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
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
enfermeros: List[Enfermero] = [
    {"Nombre": "Ana", "Edad": 30, "Cedula": 123, "Estado": True},
    {"Nombre": "Luis", "Edad": 28, "Cedula": 456, "Estado": True},
]
medicos: List[Medico] = [
    {"Nombre": "Dr. Juan", "Edad": 45, "Cedula": 789, "Consultorio": 1, "Estado": True},
    {"Nombre": "Dra. Marta", "Edad": 50, "Cedula": 101, "Consultorio": 2, "Estado": True},
]

# ----- FUNCIONES DE LÓGICA -----
def limpiar_campos():
    nombre_var.set("")
    edad_var.set("")
    enfermedad_var.set("")
    medicamentos_var.set("")

def registro_de_pacientes():
    nombre = nombre_var.get().capitalize()
    if not nombre:
        messagebox.showerror("Error", "El nombre es obligatorio.")
        return
    try:
        edad = int(edad_var.get())
    except ValueError:
        messagebox.showerror("Error", "Edad inválida.")
        return
    enfermedad = enfermedad_var.get().capitalize()
    medicamentos = [m.strip() for m in medicamentos_var.get().split(",") if m.strip()]
    paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Enfermedad": enfermedad,
        "Medicamentos": medicamentos,
        "Médico_asignado": "Ninguno",
        "Enfermero_asignado": "Ninguno"
    }
    pacientes.append(paciente)
    actualizar_lista_pacientes()
    messagebox.showinfo("Registro", "✅ Paciente registrado correctamente.")
    limpiar_campos()

def consultar_paciente():
    seleccionado = lista_pacientes.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un paciente de la lista.")
        return
    idx = seleccionado[0]
    p = pacientes[idx]
    info = f"""
Nombre: {p['Nombre']}
Edad: {p['Edad']}
Enfermedad: {p['Enfermedad']}
Medicamentos: {', '.join(p['Medicamentos'])}
Médico asignado: {p['Médico_asignado']}
Enfermero asignado: {p['Enfermero_asignado']}
"""
    messagebox.showinfo("Consulta", info)

def eliminar_paciente():
    seleccionado = lista_pacientes.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un paciente de la lista.")
        return
    idx = seleccionado[0]
    nombre = pacientes[idx]["Nombre"]
    if messagebox.askyesno("Confirmar", f"¿Eliminar a {nombre}?"):
        pacientes.pop(idx)
        actualizar_lista_pacientes()
        messagebox.showinfo("Eliminado", "✅ Paciente eliminado.")

def editar_paciente():
    seleccionado = lista_pacientes.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un paciente de la lista.")
        return
    idx = seleccionado[0]
    p = pacientes[idx]
    campo = simpledialog.askstring("Editar", "Campo a editar (Nombre, Edad, Enfermedad, Medicamentos):")
    if not campo:
        return
    campo = campo.capitalize()
    if campo == "Nombre":
        nuevo = simpledialog.askstring("Nuevo nombre", "Ingrese nuevo nombre:")
        if nuevo:
            p["Nombre"] = nuevo.capitalize()
    elif campo == "Edad":
        try:
            nuevo = int(simpledialog.askstring("Nueva edad", "Ingrese nueva edad:"))
            p["Edad"] = nuevo
        except:
            messagebox.showerror("Error", "Edad inválida.")
    elif campo == "Enfermedad":
        nuevo = simpledialog.askstring("Nueva enfermedad", "Ingrese nueva enfermedad:")
        if nuevo:
            p["Enfermedad"] = nuevo.capitalize()
    elif campo == "Medicamentos":
        nuevo = simpledialog.askstring("Nuevos medicamentos", "Ingrese medicamentos separados por coma:")
        if nuevo:
            p["Medicamentos"] = [m.strip() for m in nuevo.split(",") if m.strip()]
    actualizar_lista_pacientes()
    messagebox.showinfo("Editado", "✅ Paciente editado.")

def asignar_medico_enfermero():
    seleccionado = lista_pacientes.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Seleccione un paciente de la lista.")
        return
    idx = seleccionado[0]
    p = pacientes[idx]
    # Selección de médico
    medicos_disponibles = [m["Nombre"] for m in medicos if m["Estado"]]
    enfermeros_disponibles = [e["Nombre"] for e in enfermeros if e["Estado"]]
    if not medicos_disponibles or not enfermeros_disponibles:
        messagebox.showerror("Error", "No hay médicos o enfermeros disponibles.")
        return
    medico = simpledialog.askstring("Médico", f"Médicos disponibles: {', '.join(medicos_disponibles)}\nNombre del médico a asignar:")
    enfermero = simpledialog.askstring("Enfermero", f"Enfermeros disponibles: {', '.join(enfermeros_disponibles)}\nNombre del enfermero a asignar:")
    if medico and medico.capitalize() in medicos_disponibles and enfermero and enfermero.capitalize() in enfermeros_disponibles:
        p["Médico_asignado"] = medico.capitalize()
        p["Enfermero_asignado"] = enfermero.capitalize()
        actualizar_lista_pacientes()
        messagebox.showinfo("Asignación", "✅ Asignación completada.")
    else:
        messagebox.showerror("Error", "Médico o enfermero no disponibles.")

def actualizar_lista_pacientes():
    lista_pacientes.delete(0, tk.END)
    for p in pacientes:
        lista_pacientes.insert(tk.END, f"{p['Nombre']} ({p['Edad']} años)")

# ----- INTERFAZ -----
root = tk.Tk()
root.title("Gestión Médica Moderna")
root.geometry("700x500")
root.config(bg="#f5f6fa")

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Segoe UI', 11), padding=6, background='#00b894', foreground='white')
style.configure('TLabel', font=('Segoe UI', 11), background='#f5f6fa')

# Título
tk.Label(root, text="Sistema de Gestión Médica", font=("Segoe UI", 22, "bold"), bg="#f5f6fa", fg="#0984e3").pack(pady=15)

main_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

# --- Formulario de registro ---
form_frame = tk.Frame(main_frame, bg="#ffffff")
form_frame.pack(side="left", fill="y", padx=20, pady=20)

nombre_var = tk.StringVar()
edad_var = tk.StringVar()
enfermedad_var = tk.StringVar()
medicamentos_var = tk.StringVar()

fields = [
    ("Nombre", nombre_var),
    ("Edad", edad_var),
    ("Enfermedad", enfermedad_var),
    ("Medicamentos (coma)", medicamentos_var)
]
for i, (label, var) in enumerate(fields):
    ttk.Label(form_frame, text=label).grid(row=i, column=0, sticky="w", pady=6)
    ttk.Entry(form_frame, textvariable=var, width=22).grid(row=i, column=1, pady=6)

# Botón registrar
reg_btn = ttk.Button(form_frame, text="Registrar Paciente", command=registro_de_pacientes)
reg_btn.grid(row=len(fields), column=0, columnspan=2, pady=12)

# --- Lista de pacientes ---
list_frame = tk.Frame(main_frame, bg="#ffffff")
list_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

lista_pacientes = tk.Listbox(list_frame, font=("Segoe UI", 11), width=35, height=15, bd=2, relief="groove")
lista_pacientes.pack(pady=8, padx=8, fill="both", expand=True)

# --- Botones de acciones ---
btns_frame = tk.Frame(list_frame, bg="#ffffff")
btns_frame.pack(pady=8)

acciones = [
    ("Consultar", consultar_paciente, '#0984e3'),
    ("Editar", editar_paciente, '#fdcb6e'),
    ("Eliminar", eliminar_paciente, '#d63031'),
    ("Asignar Médico/Enfermero", asignar_medico_enfermero, '#6c5ce7')
]
for i, (txt, cmd, color) in enumerate(acciones):
    b = tk.Button(btns_frame, text=txt, command=cmd, bg=color, fg='white', font=('Segoe UI', 10, 'bold'), width=20)
    b.grid(row=0, column=i, padx=5)

# --- Botón salir ---
tk.Button(root, text="Salir", command=root.quit, bg="#636e72", fg="white", font=("Segoe UI", 11), width=12).pack(pady=10)

actualizar_lista_pacientes()
root.mainloop()