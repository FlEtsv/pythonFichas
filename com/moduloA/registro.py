import tkinter as tk
from tkinter import messagebox
from com.moduloB import mascotas
from com.moduloB.mascotas import Animal

def Registro(entry_nombre_dueño, entry_dni_dueño, entry_nombre, entry_tipo_Animal, entry_raza, entry_edad):
    nombre_dueño = entry_nombre_dueño.get()
    dni_dueño = entry_dni_dueño.get()
    nombre = entry_nombre.get()
    tipo = entry_tipo_Animal.get()
    raza = entry_raza.get()
    edad = entry_edad.get()

    if not dni_dueño or not nombre_dueño or not raza:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    if mascotas.Animal.cargar_datos(dni_dueño, 'dni'):
        messagebox.showerror("Error", "Ya existe un animal registrado con ese DNI")
        return

    animal = Animal(nombre_dueño, dni_dueño, nombre, tipo, raza, edad)
    try:
        mascotas.guardar_datos(animal)
        mascotas.cargar_fichas_a_clase()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar los datos: {e}")
        return

    messagebox.showinfo("Éxito", "Los datos del animal se han guardado con éxito")
