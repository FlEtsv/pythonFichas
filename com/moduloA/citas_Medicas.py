import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from com.moduloA.auxiliarViews.añadir_cita import anadir_cita_medica
from com.moduloB import mascotas
from datetime import datetime

def citas_medicas(dates):
    window = tk.Toplevel()
    window.geometry("800x600")  # Ajusta el tamaño de la ventana aquí
    window.title('Citas médicas')

    # Crear el calendario
    calendario = Calendar(window, selectmode='day', date_pattern="yyyy-mm-dd", showweeknumbers=False)
    calendario.grid(row=0, column=0, rowspan=2,padx=10, pady=10, sticky="nsew")

    # Crear el Listbox
    listbox = tk.Listbox(window)
    listbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # Crear el botón de añadir cita
    button_anadir_cita = ttk.Button(window, text="Añadir cita", command=lambda: anadir_cita_medica(dates, calendario.selection_get()))
    button_anadir_cita.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    # Crear el botón de eliminar cita
    button_eliminar_cita = ttk.Button(window, text="Eliminar cita", command=lambda: eliminar_cita(dates, listbox, calendario))
    button_eliminar_cita.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    # Ajustar el tamaño de las columnas
    window.grid_columnconfigure(0, weight=1)  # Ajusta el tamaño de la columna

    # Función para actualizar el Listbox según la fecha seleccionada
    def on_select(event):
        listbox.delete(0, tk.END)
        fecha_seleccionada = calendario.selection_get().strftime("%Y-%m-%d")
        citas_del_dia = [cita for cita in dates.citas if cita['fecha'] == fecha_seleccionada]
        for cita in citas_del_dia:
            listbox.insert(tk.END, f"Motivo: {cita['motivo']}\nDescripción: {cita['descripcion']}")

    # Vincular la selección del calendario con la actualización del Listbox
    calendario.bind('<<CalendarSelected>>', on_select)

    # Función para actualizar el calendario con las citas
    def actualizar_calendario(dates, calendario):
        for cita in dates.citas:
            fecha_evento = datetime.strptime(cita['fecha'], "%Y-%m-%d").date()
            calendario.calevent_create(date=fecha_evento, text='Cita', tags='cita')
        calendario.tag_config('cita', background='lightblue', foreground='black')

    # Función para eliminar una cita seleccionada del Listbox
    def eliminar_cita(dates, listbox, calendario):
        seleccion = listbox.curselection()
        if seleccion:
            index = seleccion[0]
            fecha_seleccionada = calendario.selection_get().strftime("%Y-%m-%d")
            citas_del_dia = [cita for cita in dates.citas if cita['fecha'] == fecha_seleccionada]
            cita_a_eliminar = citas_del_dia[index]
            dates.citas.remove(cita_a_eliminar)
            mascotas.guardar_datos(dates)
            actualizar_calendario(dates, calendario)
            on_select(None)

    actualizar_calendario(dates, calendario)

    window.mainloop()