from flask import Blueprint, jsonify, request
import csv
import datetime

turnos_bp = Blueprint('turnos_bp', __name__)

def cargar_datos_turnos():
    datos = []
    try:
        with open('modelos/turnos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        pass
    return datos

def guardar_datos_turnos(datos):
    with open('modelos/turnos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_medico', 'id_paciente', 'hora_turno', 'fecha_solicitud']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for turno in datos:
            writer.writerow(turno)

@turnos_bp.route('/', methods=['GET'])
def obtener_turnos():
    datos_turnos = cargar_datos_turnos()
    return jsonify({"turnos": datos_turnos})

@turnos_bp.route('/pendientes/<int:id_medico>', methods=['GET'])
def obtener_turnos_pendientes(id_medico):
    datos_turnos = cargar_datos_turnos()
    turnos_pendientes = [turno for turno in datos_turnos if turno['id_medico'] == str(id_medico)]
    return jsonify({"turnos_pendientes": turnos_pendientes})

@turnos_bp.route('/', methods=['POST'])
def registrar_turno():
    datos_turnos = cargar_datos_turnos()

    nuevo_turno = request.get_json()

    fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
    nuevo_turno['fecha_solicitud'] = fecha_actual

    datos_turnos.append(nuevo_turno)

    guardar_datos_turnos(datos_turnos)

    return jsonify({"mensaje": "Turno registrado exitosamente"})
