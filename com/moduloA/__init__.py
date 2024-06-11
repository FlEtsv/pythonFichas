import tkinter as tk
from tkinter import messagebox, ttk

import tkinter

from com.moduloB import mascotas

# Cargamos las fichas a la clase
mascotas.cargar_fichas_a_clase()
#imprimimos las instancias de la clase animal
mascotas.todas_las_fichas()

def Registro():
    """
    Guarda los datos de un animal en un archivo json
    :param nombre_dueño: Nombre del dueño
    :param dni_dueño: DNI del dueño
    :param tipo: Tipo de animal
    :param nombre: Nombre del animal
    :param raza: Raza del animal
    :param edad: Edad del animal
    no se almacena el hsitorial medico en el registro.
    :return:
    """
    nombre_dueño = entry_nombre_dueño.get()
    dni_dueño = entry_dni_dueño.get()
    tipo = entry_tipo_Animal.get()
    nombre = entry_nombre.get()
    raza = entry_raza.get()
    edad = entry_edad.get()

    if not dni_dueño or not nombre_dueño or not raza:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    #verificamos que el dni del dueño no este registrado en las fichas
    if mascotas.cargar_datos(dni_dueño, buscar_por='dni'):
        messagebox.showerror("Error", "Ya existe un animal registrado con ese DNI")
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
        dates = mascotas.Animal.cargar_datos(nombre_animal, buscar_por='nombre')

    else:
        dates = mascotas.Animal.cargar_datos(dni, buscar_por='dni')

    # Crear una nueva ventana para mostrar la ficha
    window = tk.Toplevel(root)
    # damos un tamaño a la ventana
    window.geometry("400x400")
    window.title('Ficha mascota completa')
    # Crear y empaquetar las etiquetas para los dates del animal
    if dates is not None:
        tk.Label(window, text=f'Nombre: {dates.nombre}').pack()
        tk.Label(window, text=f'Raza: {dates.raza}').pack()
        tk.Label(window, text=f'Edad: {dates.edad}').pack()

        # Crear y empaquetar una etiqueta para el historial médico
        tk.Label(window, text='Historial Médico:').pack()

        historial_medico = dates.historial_medico if hasattr(dates, 'historial_medico') else []
        if historial_medico:
            for i, registro in enumerate(historial_medico, 1):
                tk.Label(window, text=f'Registro {i}:').pack()
                tk.Label(window, text=f'Fecha: {registro["fecha"]}').pack()
                tk.Label(window, text=f'Motivo: {registro["motivo"]}').pack()
                tk.Label(window, text=f'Descripción: {registro["descripcion"]}').pack()
        else:
            tk.Label(window, text='No hay registros en el historial médico').pack()
    else:
        tk.Label(window, text='No animal found with the given identifier.').pack()

    #añadimos boton para añadir historial medico

    button_añadir_historial = ttk.Button(window, text="Añadir historial", command=lambda: Añadir_historial_medico(dates))
    button_añadir_historial.pack()

def Añadir_historial_medico(nombre):
    """
    Añade un registro al historial médico de un animal
    :param nombre: INSTANCIA DE LA CLASE ANIMAL
    :param fecha: Fecha del registro
    :param motivo: Motivo de la consulta
    :param descripcion: Descripción de la consulta
    :return:
    """
    animal = nombre

    # Crear una nueva ventana para añadir el historial médico
    window = tk.Toplevel(root)

    # damos un tamaño a la ventana
    window.geometry("400x400")
    window.title('Añadir historial médico')
    # Crear y empaquetar las etiquetas y los campos de texto
    tk.Label(window, text='Fecha:').pack()
    entry_fecha = tk.Entry(window)
    entry_fecha.pack()
    tk.Label(window, text='Motivo:').pack()
    entry_motivo = tk.Entry(window)
    entry_motivo.pack()
    tk.Label(window, text='Descripción:').pack()
    entry_descripcion = tk.Entry(window)
    entry_descripcion.pack()

    # instanciamos la clase animal con los datos del diccionario
    if animal is not None:
        animal = mascotas.Animal(animal.nombre_dueño, animal.dni_dueño, animal.nombre, animal.raza, animal.edad, animal.TipoAnimal)
    else:
        print('No animal found with the given identifier.')
        return
    # Añadir el registro al historial médico
    animal.historial_medico = animal.historial_medico if hasattr(animal, 'historial_medico') else []
    #añadimos el historial medico
    mascotas.añadir_historial(animal, entry_fecha.get(), entry_motivo.get(), entry_descripcion.get())
    print('Registro añadido con éxito')
    """
    Crear una interfaz gráfica con tkinter que permita registrar un animal y mostrar su ficha."""
root = tk.Tk()
root.title('Control de mascotas')

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
button_guardar = ttk.Button(root, text="Guardar", command=Registro)
button_guardar.grid(row=6, column=0, padx=10, pady=10)

button_mostrar = ttk.Button(root, text="Mostrar", command=mostrar_Ficha_Animal)
button_mostrar.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
