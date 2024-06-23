import tkinter as tk
from tkinter import ttk
from com.moduloA.auxiliarViews.añadir_historia import Añadir_historial_medico
from com.moduloA.citas_Medicas import citas_medicas
from com.moduloB import mascotas

def mostrar_Ficha_Animal(entry_dni_dueño, entry_nombre):
    dni = entry_dni_dueño.get()
    nombre_animal = entry_nombre.get()
    if not dni:
        dates = mascotas.Animal.cargar_datos(nombre_animal, buscar_por='nombre')
    else:
        dates = mascotas.Animal.cargar_datos(dni, buscar_por='dni')

    window = tk.Toplevel()
    window.geometry("800x400")
    window.title('Ficha mascota completa')

    if dates is not None:
        # Primera columna
        tk.Label(window, text=f'Nombre: {dates.nombre}').grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(window, text=f'Raza: {dates.raza}').grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(window, text=f'Edad: {dates.edad}').grid(row=2, column=0, padx=10, pady=10, sticky="w")

        tk.Label(window, text='Historial Médico:').grid(row=3, column=0, padx=10, pady=10, sticky="w")
        listbox = tk.Listbox(window)
        listbox.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Segunda columna
        motivo_label = tk.Label(window, text='')
        motivo_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        descripcion_label = tk.Label(window, text='')
        descripcion_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        #Botones

        button_añadir_historial = ttk.Button(window, text="Añadir historial",
                                             command=lambda: Añadir_historial_medico(dates, listbox))
        button_añadir_historial.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        button_eliminar_historial = ttk.Button(window, text="Eliminar historial",
                                               command=lambda: eliminar_historial(dates, listbox))
        button_eliminar_historial.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        button_citas_medicas = ttk.Button(window, text="Citas",
                                          command=lambda: citas_medicas(dates))

        button_citas_medicas.grid(row=5, column=2, padx=10, pady=10, sticky="w")

        if hasattr(dates, 'historial_medico') and dates.historial_medico:
            for i, registro in enumerate(dates.historial_medico, 1):
                listbox.insert(i, f'Fecha: {registro["fecha"]}')
        else:
            listbox.insert(0, 'No hay historial médico')

        def on_select(event):
            index = listbox.curselection()
            if index:
                index = index[0]
                registro = dates.historial_medico[index]
                # Actualizar el contenido de los labels
                motivo_label.config(text=f'Motivo: {registro["motivo"]}')
                descripcion_label.config(text=f'Descripción: {registro["descripcion"]}')

        listbox.bind('<<ListboxSelect>>', on_select)

        def eliminar_historial(dates, listbox):
            index = listbox.curselection()
            if index:
                index = index[0]
                del dates.historial_medico[index]
                mascotas.guardar_datos(dates)
                listbox.delete(index)
                motivo_label.config(text='')
                descripcion_label.config(text='')

    else:
        tk.Label(window, text='No se encontró un animal con ese nombre').grid(row=0, column=0, padx=10, pady=10, sticky="w")