import tkinter as tk
from tkinter import messagebox, ttk

import tkinter

from com.moduloB import mascotas


def guardar():
    nombre_dueño = entry_nombre_dueño.get()
    dni_dueño = entry_dni_dueño.get()
    tipo = entry_tipo_Animal.get()
    nombre = entry_nombre.get()
    raza = entry_raza.get()
    edad = entry_edad.get()

    if not dni_dueño or not nombre_dueño or not raza:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    animal = mascotas.Animal(nombre_dueño, dni_dueño, nombre, raza, edad, tipo)
    mascotas.guardar_datos(animal)

    messagebox.showinfo("Éxito", "Los datos del animal se han guardado con éxito")

def mostrar_Ficha_Animal():
    """
    Muestra la ficha de un animal en una nueva ventana
    :param nombre: Nombre del animal
    :param dni: DNI del dueño
    :param buscar_por: 'nombre' o 'dni'
    :param nombre_dueño: Nombre del dueño
    :param dni_dueño: DNI del dueño
    :param tipo: Tipo de animal
    :param raza: Raza del animal
    :param edad: Edad del animal
    :param historial_medico: Historial médico del animal

    :return:
    """
    dni = entry_dni_dueño.get()
    nombre_animal = entry_nombre.get()
    if not dni:
        dates = mascotas.cargar_datos(nombre_animal)
    else:
        dates = mascotas.cargar_datos(dni, buscar_por='dni')
    # Crear una nueva ventana
    window = tk.Toplevel(root)

    # Crear y empaquetar las etiquetas para los dates del animal
    tk.Label(window, text=f'Nombre: {dates["nombre"]}').pack()
    tk.Label(window, text=f'Raza: {dates["raza"]}').pack()
    tk.Label(window, text=f'Edad: {dates["edad"]}').pack()

    # Crear y empaquetar una etiqueta para el historial médico
    tk.Label(window, text='Historial Médico:').pack()

    historial_medico = dates.get('historial_medico', [])
    if historial_medico:
        for i, registro in enumerate(historial_medico, 1):
            tk.Label(window, text=f'Registro {i}:').pack()
            tk.Label(window, text=f'Fecha: {registro["fecha"]}').pack()
            tk.Label(window, text=f'Motivo: {registro["motivo"]}').pack()
            tk.Label(window, text=f'Descripción: {registro["descripcion"]}').pack()
    else:
        tk.Label(window, text='No hay registros en el historial médico').pack()

root = tk.Tk()

# Nombre dueño
label_nombre_dueño = ttk.Label(root, text="Nombre_dueño")
label_nombre_dueño.grid(row=0, column=0, padx=10, pady=10)

entry_nombre_dueño = ttk.Entry(root)
entry_nombre_dueño.grid(row=0, column=1, padx=10, pady=10)

# DNI dueño
label_dni_dueño = ttk.Label(root, text="DNI_dueño")
label_dni_dueño.grid(row=1, column=0, padx=10, pady=10)

entry_dni_dueño = ttk.Entry(root)
entry_dni_dueño.grid(row=1, column=1, padx=10, pady=10)

# Nombre animal
label_nombre = ttk.Label(root, text="Nombre")
label_nombre.grid(row=2, column=0, padx=10, pady=10)

entry_nombre = ttk.Entry(root)
entry_nombre.grid(row=2, column=1, padx=10, pady=10)

# Tipo Animal
label_tipo_Animal = ttk.Label(root, text="Tipo_Animal")
label_tipo_Animal.grid(row=3, column=0, padx=10, pady=10)

entry_tipo_Animal = ttk.Entry(root)
entry_tipo_Animal.grid(row=3, column=1, padx=10, pady=10)

# Raza
label_raza = ttk.Label(root, text="Raza")
label_raza.grid(row=4, column=0, padx=10, pady=10)

entry_raza = ttk.Entry(root)
entry_raza.grid(row=4, column=1, padx=10, pady=10)

# Edad
label_edad = ttk.Label(root, text="Edad")
label_edad.grid(row=5, column=0, padx=10, pady=10)

entry_edad = ttk.Entry(root)
entry_edad.grid(row=5, column=1, padx=10, pady=10)

# Botones
button_guardar = ttk.Button(root, text="Guardar", command=guardar)
button_guardar.grid(row=6, column=0, padx=10, pady=10)

button_mostrar = ttk.Button(root, text="Mostrar", command=mostrar_Ficha_Animal)
button_mostrar.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
