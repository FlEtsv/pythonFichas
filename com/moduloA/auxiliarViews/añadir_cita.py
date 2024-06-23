from tkinter import ttk
import tkinter as tk
from com.moduloB import mascotas

def anadir_cita_medica(dates, fecha_seleccionada):
    def añadir_cita():
        fecha = fecha_seleccionada.strftime("%Y-%m-%d")
        motivo = entry_motivo.get()
        descripcion = entry_descripcion.get()
        if not motivo or not descripcion:
            print('Todos los campos deben estar llenos.')
            return

        if not hasattr(dates, 'citas'):
            dates.citas = []
        dates.citas.append({
            'fecha': fecha,
            'motivo': motivo,
            'descripcion': descripcion
        })
        mascotas.guardar_datos(dates)
        print('Cita añadida con éxito')
        window.destroy()

    window = tk.Toplevel()
    window.geometry("400x300")
    window.title('Añadir cita médica')

    tk.Label(window, text=f'Fecha: {fecha_seleccionada.strftime("%Y-%m-%d")}').pack(pady=10)
    tk.Label(window, text='Motivo:').pack()
    entry_motivo = tk.Entry(window)
    entry_motivo.pack(pady=5)

    tk.Label(window, text='Descripción:').pack()
    entry_descripcion = tk.Entry(window)
    entry_descripcion.pack(pady=5)

    button_guardar_cita = ttk.Button(window, text="Guardar", command=añadir_cita)
    button_guardar_cita.pack(pady=20)

    window.mainloop()
