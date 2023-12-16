from flask import Blueprint, jsonify, request
from modelos.turnos import *

turnos_bp = Blueprint('turnos', __name__)

@turnos_bp.route('/turnos/', methods=["GET"])
def obtener_turnos_json():
    return jsonify(obtener_turnos()),200

@turnos_bp.route('/turnos/<int:id>', methods=["GET"])
def obtener_turno_id_json(id):
    if(id >= 1 and id <= obtener_maximo_id_medico()):
        return jsonify(obtener_turno_id(id)),200
    else:
        return jsonify({"error":"id fuera de rango"}),404
    
@turnos_bp.route('/turnos/', methods=["POST"])
def registrar_turno_json():
    if request.is_json:
        if "id_medico" in request.json and "id_paciente" in request.json and "hora_turno" in request.json and "fecha_turno" in request.json:
            turno = request.get_json()
            if validar_id_medico(turno["id_medico"]) and validar_id_paciente(turno["id_paciente"]):
                if validar_hora(turno["hora_turno"]):
                    turno_creado = registrar_turno(turno["id_medico"],turno["id_paciente"],turno["hora_turno"], turno["fecha_turno"])
                    return jsonify({"turno creado" : turno_creado}),200
                else:
                    return jsonify({"error":"hora invalida"}),411
            else:
                return jsonify({"error":"id fuera de rango"}),404
        else:
            return jsonify({"error":"Faltan datos"}),413
    else:
        return jsonify({"error":"el formato de la solicitud no es JSON"}),414

@turnos_bp.route('/turnos/<int:id>', methods=["DELETE"])
def eliminar_turno_id_json(id):
    if(id >= 1 and id <= obtener_maximo_id_medico()):
        eliminar_turno_id(id)
        return jsonify({"TURNO/S" : "ELIMINADO/S"}),200
    else:
        return jsonify({"error":"Indice fuera de rango"}),404
                

        



    