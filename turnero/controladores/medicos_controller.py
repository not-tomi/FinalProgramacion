from flask import Blueprint, jsonify, request
from modelos.medicos import *
import csv
# Crea un Blueprint para los médicos
medicos_blueprint = Blueprint('medicos', __name__)

@medicos_blueprint.route('/medicos', methods=['GET'])
def obtener_datos():
    return jsonify(obtener_datos_desde_api())

@medicos_blueprint.route('/medicos/<int:medico_id>', methods=['GET'])
def obtener_detalle_medico(medico_id):
    medico = next((m for m in medicos if m['id'] == medico_id), None)
    if medico:
        return jsonify(medico)
    else:
        return jsonify({'mensaje': 'Médico no encontrado'}), 404

@medicos_blueprint.route('/medicos', methods=['POST'])
def agregar_medico():
    nuevo_medico = request.get_json()
    medicos.append(nuevo_medico)
    
    with open('modelos/medicos.csv', mode='a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["id", "dni", "nombre", "apellido", "matricula", "telefono", "email", "habilitado"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if csv_file.tell() == 0:
            writer.writeheader()

        writer.writerow(nuevo_medico)

    return jsonify({'mensaje': 'Médico agregado correctamente'})


@medicos_blueprint.route('/medicos/<int:medico_id>', methods=['PUT'])
def actualizar_medico(medico_id):
    medico = next((m for m in medicos if m['id'] == medico_id), None)
    if medico:
        datos_actualizados = request.get_json()
        medico.update(datos_actualizados)

        with open('modelos/medicos.csv', mode='r', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["id", "dni", "nombre", "apellido", "matricula", "telefono", "email", "habilitado"]
            reader = csv.DictReader(csv_file)
            filas = list(reader)

        with open('modelos/medicos.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for fila in filas:
                if int(fila["id"]) == medico_id:
                    fila.update(medico)
                writer.writerow(fila)

        return jsonify({'mensaje': 'Médico actualizado correctamente'})
    else:
        return jsonify({'mensaje': 'Médico no encontrado'}), 404


@medicos_blueprint.route('/medicos/deshabilitar/<int:medico_id>', methods=['PUT'])
def deshabilitar_medico(medico_id):
    medico = next((m for m in medicos if m['id'] == medico_id), None)
    if medico:
        medico['habilitado'] = False

        with open('modelos/medicos.csv', mode='r', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["id", "dni", "nombre", "apellido", "matricula", "telefono", "email", "habilitado"]
            reader = csv.DictReader(csv_file)
            filas = list(reader)

        with open('modelos/medicos.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for fila in filas:
                if int(fila["id"]) == medico_id:
                    fila.update(medico)
                writer.writerow(fila)

        return jsonify({'mensaje': 'Médico deshabilitado correctamente'})
    else:
        return jsonify({'mensaje': 'Médico no encontrado'}), 404
        

