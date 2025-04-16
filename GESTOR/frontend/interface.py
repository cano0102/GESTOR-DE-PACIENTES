import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.index import registrar_medicos
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame  

root = tk.Tk()
root.title("SISTEMA DE GESTOR DE PACIENTES")
root.geometry("400x300")
root.config(bg="pink")

titulo = tk.Label(root, text="Gestor de pacientes", font=("Arial", 16), bg="purple", fg="white")
titulo.pack(pady=20)


cuadro = Frame(root, width=500, height=600, bg="blak", bd=2, relief="solid")
cuadro.place(relx=0.5, rely=0.5, anchor="center")
cuadro.config(bg="blue")  



root.mainloop()
