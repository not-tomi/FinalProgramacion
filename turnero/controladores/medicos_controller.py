from flask import Blueprint, jsonify
import csv

medicos_bp = Blueprint('medicos_bp', __name__)

def cargar_datos_medicos():
    datos = []
    try:
        with open('modelos/medicos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        pass
    return datos

def guardar_datos_medicos(datos):
    with open('modelos/medicos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'dni', 'nombre', 'apellido', 'matricula', 'telefono', 'email', 'habilitado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for medico in datos:
            writer.writerow(medico)

@medicos_bp.route('/', methods=['GET'])
def obtener_medicos():
    datos_medicos = cargar_datos_medicos()
    return jsonify({"medicos": datos_medicos})

@medicos_bp.route('/<int:id>', methods=['GET'])
def obtener_medico_por_id(id):
    datos_medicos = cargar_datos_medicos()
    medico = next((med for med in datos_medicos if med['id'] == str(id)), None)
    if medico:
        return jsonify({"medico": medico})
    else:
        return jsonify({"mensaje": "Médico no encontrado"}), 404

@medicos_bp.route('/nombre/<string:nombre>', methods=['GET'])
def obtener_medicos_por_nombre(nombre):
    datos_medicos = cargar_datos_medicos()
    medicos_por_nombre = [med for med in datos_medicos if med['nombre'].lower() == nombre.lower()]
    return jsonify({"medicos": medicos_por_nombre})

@medicos_bp.route('/dni/<string:dni>', methods=['GET'])
def obtener_medicos_por_dni(dni):
    datos_medicos = cargar_datos_medicos()
    medico_por_dni = next((med for med in datos_medicos if med['dni'] == dni), None)
    if medico_por_dni:
        return jsonify({"medico": medico_por_dni})
    else:
        return jsonify({"mensaje": "Médico no encontrado"}), 404

@medicos_bp.route('/matricula/<string:matricula>', methods=['GET'])
def obtener_medicos_por_matricula(matricula):
    datos_medicos = cargar_datos_medicos()
    medicos_por_matricula = [med for med in datos_medicos if med['matricula'].lower() == matricula.lower()]
    return jsonify({"medicos": medicos_por_matricula})
