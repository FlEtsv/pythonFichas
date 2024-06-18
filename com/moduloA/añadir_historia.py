import tkinter as tk
from tkinter import ttk
from com.moduloB import mascotas

def Añadir_historial_medico(animal):
    def añadir_registro():
        fecha = entry_fecha.get()
        motivo = entry_motivo.get()
        descripcion = entry_descripcion.get()
        if not fecha or not motivo or not descripcion:
            print('All fields must be filled.')
            return

        animal.historial_medico = animal.historial_medico if hasattr(animal, 'historial_medico') else []
        mascotas.añadir_historial(animal, fecha, motivo, descripcion)
        print('Registro añadido con éxito')
        mascotas.cargar_fichas_a_clase()
        window.destroy()

    window = tk.Toplevel()
    window.geometry("400x400")
    window.title('Añadir historial médico')

    tk.Label(window, text='Fecha:').pack()
    entry_fecha = tk.Entry(window)
    entry_fecha.pack()
    tk.Label(window, text='Motivo:').pack()
    entry_motivo = tk.Entry(window)
    entry_motivo.pack()
    tk.Label(window, text='Descripción:').pack()
    entry_descripcion = tk.Entry(window)
    entry_descripcion.pack()

    button_guardar_historial_medico = ttk.Button(window, text="Guardar", command=añadir_registro)
    button_guardar_historial_medico.pack()
