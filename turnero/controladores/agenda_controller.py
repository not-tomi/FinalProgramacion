from flask import Blueprint, jsonify, request
import csv

agenda_medicos_bp = Blueprint('agenda_medicos_bp', __name__)

def cargar_datos_agenda_medicos():
    datos = []
    try:
        with open('modelos/agenda_medicos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        pass
    return datos

def guardar_datos_agenda_medicos(datos):
    with open('modelos/agenda_medicos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_medico', 'dia_numero', 'hora_inicio', 'hora_fin', 'fecha_actualizacion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for horario in datos:
            writer.writerow(horario)

@agenda_medicos_bp.route('/', methods=['GET'])
def obtener_horarios_habilitados():
    datos_agenda_medicos = cargar_datos_agenda_medicos()
    return jsonify({"agenda_medicos": datos_agenda_medicos})

@agenda_medicos_bp.route('/', methods=['POST'])
def agregar_horario_atencion():
    datos_agenda_medicos = cargar_datos_agenda_medicos()

    nuevo_horario = request.get_json()

    datos_agenda_medicos.append(nuevo_horario)

    guardar_datos_agenda_medicos(datos_agenda_medicos)

    return jsonify({"mensaje": "Horario de atención agregado exitosamente"})

@agenda_medicos_bp.route('/', methods=['PUT'])
def modificar_horarios_atencion():
    datos_agenda_medicos = cargar_datos_agenda_medicos()

    horarios_modificados = request.get_json()

    # Lógica para validar y modificar los horarios

    guardar_datos_agenda_medicos(datos_agenda_medicos)

    return jsonify({"mensaje": "Horarios de atención modificados exitosamente"})

@agenda_medicos_bp.route('/<int:id_medico>', methods=['DELETE'])
def eliminar_horarios_atencion(id_medico):
    datos_agenda_medicos = cargar_datos_agenda_medicos()

    # Lógica para eliminar los horarios de un médico específico
    datos_agenda_medicos = [horario for horario in datos_agenda_medicos if horario['id_medico'] != str(id_medico)]

    guardar_datos_agenda_medicos(datos_agenda_medicos)

    return jsonify({"mensaje": "Horarios de atención eliminados exitosamente"})
