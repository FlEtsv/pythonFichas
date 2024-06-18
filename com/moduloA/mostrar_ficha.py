import tkinter as tk
from tkinter import ttk
from com.moduloA.añadir_historia import Añadir_historial_medico
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
        tk.Label(window, text=f'Nombre: {dates.nombre}').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(window, text=f'Raza: {dates.raza}').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(window, text=f'Edad: {dates.edad}').grid(row=2, column=0, padx=10, pady=10)

        tk.Label(window, text='Historial Médico:').grid(row=3, column=0, padx=10, pady=10)
        listbox = tk.Listbox(window)
        listbox.grid(row=4, column=0, padx=10, pady=10)

        # Segunda columna
        registro_label = tk.Label(window, text='')
        registro_label.grid(row=0, column=1, padx=10, pady=10)

        button_añadir_historial = ttk.Button(window, text="Añadir historial", command=lambda: Añadir_historial_medico(dates))
        button_añadir_historial.grid(row=3, column=1, padx=10, pady=10)

        button_eliminar_historial = ttk.Button(window, text="Eliminar historial", command=lambda: eliminar_historial(dates, listbox))
        button_eliminar_historial.grid(row=4, column=1, padx=10, pady=10)

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
                registro_label['text'] = f'\nMotivo: {registro["motivo"]}\nDescripción: {registro["descripcion"]}'

        listbox.bind('<<ListboxSelect>>', on_select)

        def eliminar_historial(dates, listbox):
            index = listbox.curselection()
            if index:
                index = index[0]
                del dates.historial_medico[index]
                mascotas.guardar_datos(dates)
                listbox.delete(index)
                registro_label['text'] = ''
    else:
        tk.Label(window, text='No se encontró un animal con ese nombre').grid(row=0, column=0, padx=10, pady=10)

