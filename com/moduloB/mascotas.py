import json
import os

class Animal:
    instances = []

    def __init__(self, nombre_dueño, dni_dueño, nombre, tipo_animal, raza, edad):
        self.nombre_dueño = nombre_dueño
        self.dni_dueño = dni_dueño
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tipo_animal = tipo_animal
        self.historial_medico = []
        self.citas = []

    def añadir_cita(self, fecha, motivo, descripcion):
        self.citas.append({
            'fecha': fecha,
            'motivo': motivo,
            'descripcion': descripcion
        })

    def eliminar_cita(self, index):
        if index < len(self.citas):
            del self.citas[index]

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
        return None

def todas_las_fichas():
    print('Fichas de animales:')
    for instance in Animal.instances:
        print(f'Nombre: {instance.nombre}')
        print(f'Dueño: {instance.nombre_dueño}')
        print(f'DNI: {instance.dni_dueño}')
        print(f'Tipo: {instance.tipo_animal}')
        print(f'Raza: {instance.raza}')
        print(f'Edad: {instance.edad}')
        print('Historial médico:')
        for registro in instance.historial_medico:
            print(f'Fecha: {registro["fecha"]}')
            print(f'Motivo: {registro["motivo"]}')
            print(f'Descripción: {registro["descripcion"]}')
        print('Citas:')
        for cita in instance.citas:
            print(f'Fecha: {cita["fecha"]}')
            print(f'Motivo: {cita["motivo"]}')
            print(f'Descripción: {cita["descripcion"]}')
        print()

def cargar_fichas_a_clase():
    if not os.path.exists('fichas_animal'):
        return
    for filename in os.listdir('fichas_animal'):
        with open(f'fichas_animal/{filename}', 'r') as f:
            datos = json.load(f)
            animal = Animal(
                datos['nombre_dueño'], datos['dni_dueño'], datos['nombre'],
                datos['tipo'], datos['raza'], datos['edad']
            )
            animal.historial_medico = datos.get('historial_medico', [])
            animal.citas = datos.get('citas', [])
            Animal.instances.append(animal)

def guardar_datos(animal):
    datos = {
        "nombre_dueño": animal.nombre_dueño,
        "dni_dueño": animal.dni_dueño,
        "nombre": animal.nombre,
        'tipo': animal.tipo_animal,
        "raza": animal.raza,
        "edad": animal.edad,
        "historial_medico": animal.historial_medico,
        "citas": animal.citas
    }

    if not os.path.exists('fichas_animal'):
        os.makedirs('fichas_animal')

    ficha_animal = os.path.join('fichas_animal', f'{animal.nombre}.json')

    with open(ficha_animal, 'w') as f:
        json.dump(datos, f)

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

def añadir_historial(animal, fecha, motivo, descripcion):
    if not hasattr(animal, 'historial_medico'):
        animal.historial_medico = []
    animal.historial_medico.append({
        'fecha': fecha,
        'motivo': motivo,
        'descripcion': descripcion
    })
    guardar_datos(animal)
