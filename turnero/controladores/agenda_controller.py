from flask import Blueprint, jsonify, request
from modelos.agenda_medicos import *

agenda_bp = Blueprint('agenda_medicos', __name__)

@agenda_bp.route('/agenda/', methods=["GET"])
def obtener_agenda_json():
    return jsonify(obtener_horarios()),200

@agenda_bp.route('/agenda/<int:id>/', methods=["GET"])
def obtener_agenda_id_json(id):
    if(id >= 1 and id <= obtener_maximo_id()):
        return jsonify(obtener_horarios_id(id)),200
    else:
        return jsonify({"error":"id fuera de rango"}),404

@agenda_bp.route('/agenda/', methods=["POST"])
def crear_horario_json():
    if request.is_json:
        if "id_medico" in request.json and "dia_numero" in request.json and "hora_inicio" in request.json and "hora_fin" in request.json:
            horario = request.get_json()
            if horario["id_medico"] >= 1 and horario["id_medico"] <= obtener_maximo_id():
                if validar_dia(horario["dia_numero"]):
                    if int(horario["dia_numero"]) >= 1 and int(horario["dia_numero"]) <= 6:
                        if validar_hora(horario["hora_inicio"]) and validar_hora(horario["hora_fin"]):
                            horario_creado = crear_horario(horario["id_medico"],horario["dia_numero"],horario["hora_inicio"],horario["hora_fin"])
                            return jsonify({"horario creado" : horario_creado})
                        else:
                            return jsonify({"error":"hora no valida"}),411
                    else:
                        return jsonify({"error":"dia fuera de rango"}),412
                else:
                    return jsonify({"error":"dia no valido"}),410
            else:
                return jsonify({"error":"id fuera de rango"}),404
        else:
            return jsonify({"error":"Faltan datos"}),413
    else:
        return jsonify({"error":"el formato de la solicitud no es JSON"}),414
        
@agenda_bp.route('/agenda/<int:id>', methods=["PUT"])
def modificar_horario_json(id):
    if(id >= 1 and id <= obtener_maximo_id()):
        if request.is_json:
            if "dia_numero" in request.json and "hora_inicio" in request.json and "hora_fin" in request.json:
                horario_nuevo = request.get_json()
                if validar_dia(horario_nuevo["dia_numero"]):
                    if int(horario_nuevo["dia_numero"]) >= 1 and int(horario_nuevo["dia_numero"]) <= 6:
                        if validar_hora(horario_nuevo["hora_inicio"]) and validar_hora(horario_nuevo["hora_fin"]):
                            horario = modificar_horario_id(id, horario_nuevo["dia_numero"], horario_nuevo["hora_inicio"], horario_nuevo["hora_fin"])
                            return jsonify({"horario modificado" : horario})
                        else:
                            return jsonify({"error":"hora no valida"}),411
                    else:
                        return jsonify({"error":"dia fuera de rango"}),412
                else:
                    return jsonify({"error":"dia no valido"}),410
            else:
                return jsonify({"error":"Faltan datos"}),413
        else:
            return jsonify({"error":"El formato de la solicitud no es JSON"}),414
    else:
        return jsonify({"error":"Indice fuera de rango"}),404
        
@agenda_bp.route('/agenda/<int:id>', methods=["DELETE"])
def eliminar_horarios_json(id):
    if(id >= 1 and id <= obtener_maximo_id()):
        eliminar_horario_id(id)
        return jsonify({"HORARIO/S" : "ELIMINADO/S"}),200
    else:
        return jsonify({"error":"Indice fuera de rango"}),404

        

        



        
