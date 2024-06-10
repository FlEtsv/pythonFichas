import json
import os

"""
Crear un módulo llamado mascotas.py que contenga una clase llamada Animal. La clase debe tener los atributos nombre, raza y edad.
Crear una función llamada guardar_datos que reciba un objeto de tipo Animal y guarde sus atributos en un archivo json.
Crear una función llamada cargar_datos que reciba el nombre de un archivo json y retorne un objeto de tipo Animal con los atributos correspondientes.
Crear una función llamada mostrar_ficha que reciba el nombre de un archivo json y muestre en pantalla los atributos de un objeto de tipo Animal."""
class Animal:
    def __init__(self, nombre_dueño, dni_dueño,nombre , TipoAnimal, raza, edad ):
        self.nombre_dueño = nombre_dueño
        self.dni_dueño = dni_dueño
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.TipoAnimal = TipoAnimal
        self.historial_medico = []



#historial Medico
def añadir_historial(self, fecha, motivo, descripcion):
    self.historial_medico.append({
        'fecha' : fecha,
        'motivo' : motivo,
        'descripcion' : descripcion
    }

    )

def mostrar_historial_medico(nombre):
    datos = cargar_datos(nombre)
    historial_medico = datos.get('historial_medico', [])
    if historial_medico:
        for i, registro in enumerate(historial_medico, 1):
            print(f'Registro {i}')
            print(f'Fecha: {registro["fecha"]}')
            print(f'Motivo: {registro["motivo"]}')
            print(f'Descripción: {registro["descripcion"]}')
            print()
    else:
        print('No hay registros en el historial médico')








    #guardar datos animal


def guardar_datos(animal):
    datos = {
        "nombre_dueño": animal.nombre_dueño,
        "dni_dueño": animal.dni_dueño,
        "nombre": animal.nombre,
        'tipo': animal.TipoAnimal,
        "raza": animal.raza,
        "edad": animal.edad
    }

    # Crear la carpeta si no existe
    if not os.path.exists('fichas_animal'):
        os.makedirs('fichas_animal')

    # Construir la ruta del archivo
    ficha_animal = os.path.join('fichas_animal', f'{animal.nombre}.json')

    with open(ficha_animal, 'w') as f:
        json.dump(datos, f)
def cargar_datos(identificador, buscar_por='nombre'):
    if buscar_por == 'nombre':
        with open(f'fichas_animal/{identificador}.json', 'r') as f:
            datos = json.load(f)
            return datos
    elif buscar_por == 'dni':
        for filename in os.listdir('fichas_animal'):
            with open(f'fichas_animal/{filename}', 'r') as f:
                datos = json.load(f)
                if datos['dni_dueño'] == identificador:
                    return datos
    else:
        raise ValueError("El argumento buscar_por debe ser 'nombre' o 'dni'")
def mostrar_ficha_dni(dni_dueño):
    datos = cargar_datos(dni_dueño, buscar_por='dni')
    print(f'Nombre dueño: {datos["nombre_dueño"]}')
    print(f'DNI dueño: {datos["dni_dueño"]}')
    print(f'Nombre: {datos["nombre"]}')
    print(f'Tipo: {datos["tipo"]}')
    print(f'Raza: {datos["raza"]}')
    print(f'Edad: {datos["edad"]}')
