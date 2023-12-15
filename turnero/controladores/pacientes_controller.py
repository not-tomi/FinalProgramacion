from flask import Blueprint, jsonify, request
from modelos.pacientes import pacientes, cargar_pacientes_desde_api_y_guardar_en_csv

pacientes_blueprint = Blueprint("pacientes", __name__)

@pacientes_blueprint.route("/pacientes/cargar-desde-api", methods=["GET"])
def cargar_pacientes_api():
    cantidad = int(request.args.get("cantidad", 1))
    cargar_pacientes_desde_api_y_guardar_en_csv(cantidad)
    return jsonify({"message": f"Se cargaron {cantidad} pacientes desde la API randomuser"})

@pacientes_blueprint.route("/pacientes", methods=["GET"])
def obtener_pacientes():
    return jsonify({"pacientes": pacientes})

@pacientes_blueprint.route("/pacientes/<int:paciente_id>", methods=["GET"])
def obtener_detalle_paciente(paciente_id):
    paciente = next((p for p in pacientes if p["id"] == paciente_id), None)
    if paciente:
        return jsonify({"paciente": paciente})
    else:
        return jsonify({"message": "Paciente no encontrado"}), 404

@pacientes_blueprint.route("/pacientes", methods=["POST"])
def agregar_paciente():
    nuevo_paciente = request.json
    nuevo_paciente["id"] = len(pacientes) + 1
    pacientes.append(nuevo_paciente)
    return jsonify({"message": "Paciente agregado correctamente"})

@pacientes_blueprint.route("/pacientes/<int:paciente_id>", methods=["PUT"])
def actualizar_paciente(paciente_id):
    paciente = next((p for p in pacientes if p["id"] == paciente_id), None)
    if paciente:
        datos_actualizados = request.json
        paciente.update(datos_actualizados)
        return jsonify({"message": f"Paciente {paciente_id} actualizado correctamente"})
    else:
        return jsonify({"message": "Paciente no encontrado"}), 404

import csv

@pacientes_blueprint.route("/pacientes/<int:paciente_id>", methods=["DELETE"])
def eliminar_paciente(paciente_id):
    global pacientes
    paciente = next((p for p in pacientes if p["id"] == paciente_id), None)
    if paciente:
        pacientes = [p for p in pacientes if p["id"] != paciente_id]

        with open('modelos/pacientes.csv', mode='r', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["id", "nombre", "apellido", "telefono", "email"]
            reader = csv.DictReader(csv_file)
            filas = list(reader)

        with open('modelos/pacientes.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for fila in filas:
                if int(fila["id"]) != paciente_id:
                    writer.writerow(fila)

        return jsonify({"message": f"Paciente {paciente_id} eliminado correctamente"})
    else:
        return jsonify({"error": "Paciente no encontrado"}), 404

