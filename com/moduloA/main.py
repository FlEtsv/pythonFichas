import tkinter as tk
from tkinter import ttk

from com.moduloB.mascotas import cargar_fichas_a_clase
from registro import Registro
from mostrar_ficha import mostrar_Ficha_Animal

root = tk.Tk()
root.title('Control de mascotas')
cargar_fichas_a_clase()

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
button_guardar = ttk.Button(root, text="Guardar", command=lambda: Registro(entry_nombre_dueño, entry_dni_dueño, entry_nombre, entry_tipo_Animal, entry_raza, entry_edad))
button_guardar.grid(row=6, column=0, padx=10, pady=10)

button_mostrar = ttk.Button(root, text="Mostrar", command=lambda: mostrar_Ficha_Animal(entry_dni_dueño, entry_nombre))
button_mostrar.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
