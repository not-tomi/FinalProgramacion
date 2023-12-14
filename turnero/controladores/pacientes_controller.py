from flask import Blueprint, jsonify, request
from modelos.pacientes import pacientes, cargar_pacientes_desde_api

pacientes_blueprint = Blueprint("pacientes", __name__)

# Ruta para cargar pacientes desde la API randomuser
@pacientes_blueprint.route("/pacientes/cargar-desde-api", methods=["GET"])
def cargar_pacientes_api():
    cantidad = int(request.args.get("cantidad", 10))
    cargar_pacientes_desde_api(cantidad)
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

@pacientes_blueprint.route("/pacientes/<int:paciente_id>", methods=["DELETE"])
def eliminar_paciente(paciente_id):
    global pacientes
    pacientes = [p for p in pacientes if p["id"] != paciente_id]
    return jsonify({"message": f"Paciente {paciente_id} eliminado correctamente"})
