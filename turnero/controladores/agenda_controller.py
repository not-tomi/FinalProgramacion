from flask import Blueprint, jsonify, request
from modelos.agenda_medicos import *

agenda_bp = Blueprint('agenda_medicos', __name__)

@agenda_bp.route('/agenda/', methods=["GET"])
def obtener_agenda_json():
    return jsonify(obtener_horarios()),200

@agenda_bp.route('/agenda/<int:id>/', methods=["GET"])
def obtener_agenda_id_json(id):
    if(id >= 1 and id <= obtener_cantidad_horarios()):
        return jsonify(obtener_horarios_id(id)),200
    else:
        return jsonify({"error":"id inexistente"}),404


