import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.index import registrar_medicos
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("SISTEMA DE GESTOR DE PACIENTES")
root.geometry("400x300")
titulo = tk.Label(root, text="Gestor de pacientes", font=("Arial", 16))
titulo.pack(pady=20)
root.mainloop()