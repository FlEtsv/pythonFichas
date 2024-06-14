import tkinter as tk
from tkinter import messagebox, ttk

import tkinter

from com.moduloB import mascotas
from com.moduloB.mascotas import Animal

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
    nombre = entry_nombre.get()
    tipo = entry_tipo_Animal.get()
    raza = entry_raza.get()
    edad = entry_edad.get()

    if not dni_dueño or not nombre_dueño or not raza:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    #verificamos que el dni del dueño no este registrado en las fichas
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

def mostrar_Ficha_Animal():
    dni = entry_dni_dueño.get()
    nombre_animal = entry_nombre.get()
    if not dni:
        dates = mascotas.Animal.cargar_datos(nombre_animal, buscar_por='nombre')
    else:
        dates = mascotas.Animal.cargar_datos(dni, buscar_por='dni')

    window = tk.Toplevel(root)
    window.geometry("400x400")
    window.title('Ficha mascota completa')

    canvas = tk.Canvas(window)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    if dates is not None:
        tk.Label(scrollable_frame, text=f'Nombre: {dates.nombre}').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(scrollable_frame, text=f'Raza: {dates.raza}').grid(row=2, column=0, padx=10, pady=10)
        tk.Label(scrollable_frame, text=f'Edad: {dates.edad}').grid(row=3, column=0, padx=10, pady=10)

        tk.Label(scrollable_frame, text='Historial Médico:').grid(row=4, column=0, padx=10, pady=10)

        historial_medico = dates.historial_medico if hasattr(dates, 'historial_medico') else []
        if historial_medico:
            for i, registro in enumerate(historial_medico, 1):
                tk.Label(scrollable_frame, text=f'Registro {i}:').grid(row=5+i*4, column=0, padx=10, pady=10)
                tk.Label(scrollable_frame, text=f'Fecha: {registro["fecha"]}').grid(row=6+i*4, column=0, padx=10, pady=10)
                tk.Label(scrollable_frame, text=f'Motivo: {registro["motivo"]}').grid(row=7+i*4, column=0, padx=10, pady=10)
                tk.Label(scrollable_frame, text=f'Descripción: {registro["descripcion"]}').grid(row=8+i*4, column=0, padx=10, pady=10)
        else:
            tk.Label(scrollable_frame, text='No hay registros en el historial médico').grid(row=9, column=0, padx=10, pady=10)
    else:
        tk.Label(scrollable_frame, text='No animal found with the given identifier.').grid(row=1, column=0, padx=10, pady=10)

    button_añadir_historial = ttk.Button(scrollable_frame, text="Añadir historial", command=lambda: Añadir_historial_medico(dates))
    button_añadir_historial.grid(row=10, column=0, padx=10, pady=10)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def Añadir_historial_medico(animal):
    """
    Añade un registro al historial médico de un animal
    :param animal: INSTANCIA DE LA CLASE ANIMAL
    :return:
    """
    def añadir_registro():

        fecha = entry_fecha.get()
        motivo = entry_motivo.get()
        descripcion = entry_descripcion.get()
        if not fecha or not motivo or not descripcion:
            print('All fields must be filled.')
            return

        # Añadir el registro al historial médico
        animal.historial_medico = animal.historial_medico if hasattr(animal, 'historial_medico') else []
        #añadimos el historial medico
        mascotas.añadir_historial(animal, fecha, motivo, descripcion)
        print('Registro añadido con éxito')
        mascotas.cargar_fichas_a_clase()
        window.destroy()

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
    # Crear y empaquetar el botón de guardar
    button_guardar_historial_medico = ttk.Button(window, text="Guardar", command=lambda: añadir_registro())
    button_guardar_historial_medico.pack()









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
