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
