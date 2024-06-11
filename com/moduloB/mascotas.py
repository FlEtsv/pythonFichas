import json
import os

"""
Crear un módulo llamado mascotas.py que contenga una clase llamada Animal. La clase debe tener los atributos nombre, raza y edad.
Crear una función llamada guardar_datos que reciba un objeto de tipo Animal y guarde sus atributos en un archivo json.
Crear una función llamada cargar_datos que reciba el nombre de un archivo json y retorne un objeto de tipo Animal con los atributos correspondientes.
Crear una función llamada mostrar_ficha que reciba el nombre de un archivo json y muestre en pantalla los atributos de un objeto de tipo Animal."""


class Animal:
    instances = []

    def __init__(self, nombre_dueño, dni_dueño, nombre, TipoAnimal, raza, edad):
        self.nombre_dueño = nombre_dueño
        self.dni_dueño = dni_dueño
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.TipoAnimal = TipoAnimal
        self.historial_medico = []

    @classmethod
    def cargar_datos(cls, identificador, buscar_por='nombre'):
        if buscar_por == 'nombre':
            for instance in cls.instances:
                if instance.nombre == identificador:
                    return instance
        elif buscar_por == 'dni':
            for instance in cls.instances:
                if instance.dni_dueño == identificador:
                    return instance
        else:
            raise ValueError("El argumento buscar_por debe ser 'nombre' o 'dni'")


"""
Crear un método llamado cargar_datos que reciba un identificador y un argumento opcional llamado buscar_por que por defecto debe ser 'nombre'. 
El método debe buscar un objeto de tipo Animal en la lista instances y retornarlo si el atributo correspondiente coincide con el identificador. 
Si el argumento buscar_por es 'dni', el método debe buscar el objeto por el atributo dni_dueño. Si no se encuentra un objeto con el 
identificador dado, el método debe retornar None."""


def todas_las_fichas():
    print('Fichas de animales:')
    for instance in Animal.instances:
        print(f'Nombre: {instance.nombre}')
        print(f'Dueño: {instance.nombre_dueño}')
        print(f'DNI: {instance.dni_dueño}')
        print(f'Tipo: {instance.TipoAnimal}')
        print(f'Raza: {instance.raza}')
        print(f'Edad: {instance.edad}')
        print()
        # historial Medico
        print('Historial médico:')

        for registro in instance.historial_medico:
            print(f'Fecha: {registro["fecha"]}')
            print(f'Motivo: {registro["motivo"]}')
            print(f'Descripción: {registro["descripcion"]}')
            print()


"""
creamos un metodo que cargue todos las fichas a la clase animal
"""


def cargar_fichas_a_clase():
    for filename in os.listdir('fichas_animal'):
        with open(f'fichas_animal/{filename}', 'r') as f:
            datos = json.load(f)
            animal = Animal(datos['nombre_dueño'], datos['dni_dueño'], datos['nombre'], datos['tipo'], datos['raza'],
                            datos['edad'])
            animal.historial_medico = datos.get('historial_medico', [])
            Animal.instances.append(animal)


# historial Medico
"""
Crear un método llamado añadir_historial que reciba una fecha, un motivo y una descripción y añada un registro al historial médico del animal.
"""


def añadir_historial(animal, fecha, motivo, descripcion):
    animal.historial_medico.append({
        'fecha': fecha,
        'motivo': motivo,
        'descripcion': descripcion
    })


def mostrar_historial_medico(nombre):
    animal = Animal.cargar_datos(nombre)
    if animal is not None:
        historial_medico = animal.historial_medico
        if historial_medico:
            for i, registro in enumerate(historial_medico, 1):
                print(f'Registro {i}')
                print(f'Fecha: {registro["fecha"]}')
                print(f'Motivo: {registro["motivo"]}')
                print(f'Descripción: {registro["descripcion"]}')
                print()
        else:
            print('No hay registros en el historial médico')
    else:
        print('No se encontró un animal con ese nombre')

    # guardar datos animal


def guardar_datos(animal):
    datos = {
        "nombre_dueño": animal.nombre_dueño,
        "dni_dueño": animal.dni_dueño,
        "nombre": animal.nombre,
        'tipo': animal.TipoAnimal,
        "raza": animal.raza,
        "edad": animal.edad
    }

    if not os.path.exists('fichas_animal'):
        os.makedirs('fichas_animal')

    ficha_animal = os.path.join('fichas_animal', f'{animal.nombre}.json')

    with open(ficha_animal, 'w') as f:
        json.dump(datos, f)
