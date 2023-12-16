import os
import csv
from datetime import *

turnos = []
medicos = []
agenda = []
ruta_archivo_turnos = "modelos/turnos.csv"
ruta_archivo_medicos = "modelos/medicos.csv"
ruta_archivo_agenda = "modelos/agenda_medicos.csv"

def obtener_maximo_id_medico():
    mayor = None 
    with open(ruta_archivo_turnos, newline='', encoding="utf8") as csvfile:
        lector = csv.reader(csvfile)  
        next(lector)  
        for fila in lector:
            valor = int(fila[0])
            if mayor is None or valor > mayor:
                mayor = valor
    return mayor

def obtener_maximo_id_paciente():
    mayor = None 
    with open(ruta_archivo_turnos, newline='', encoding="utf8") as csvfile:
        lector = csv.reader(csvfile)  
        next(lector)  
        for fila in lector:
            valor = int(fila[1])
            if mayor is None or valor > mayor:
                mayor = valor
    return mayor

def importar_datos_desde_csv():
    global turnos
    turnos = []  
    with open(ruta_archivo_turnos, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id_medico'] = int(row['id_medico'])
            row['id_paciente'] = int(row['id_paciente'])
            turnos.append(row)

def exportar_a_csv():
    global turnos
    with open(ruta_archivo_turnos, 'w', newline='', encoding="utf8") as csvfile:
        campos = ['id_medico', 'id_paciente', 'hora_turno', 'fecha_turno','fecha_solicitud']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for turno in turnos:
            writer.writerow(turno)

def incializar_turnos():
    if os.path.exists(ruta_archivo_turnos):
        importar_datos_desde_csv()

def obtener_turnos():
    return turnos

def obtener_turno_id(id_medico):
    turnos_filtro = []
    for turno in turnos:
        if turno["id_medico"] == id_medico:
            turnos_filtro.append(turno)
    return turnos_filtro

def registrar_turno(id_medico, id_paciente, hora_turno, fecha_turno):
    global turnos
    fecha_actual = datetime.today()
    fecha_solicitada = datetime.strptime(fecha_turno, "%Y/%m/%d")
    dia_solicitado = fecha_solicitada.weekday()
    hora_solicitada = datetime.strptime(hora_turno, "%H:%M")

    for turno in turnos:
        if turno["fecha_turno"] == fecha_turno and turno["hora_turno"] == hora_turno:
            return "Ese turno ya esta dado"
        else:
            if  fecha_actual <= fecha_solicitada <= fecha_actual + timedelta(days=30):
                if obtener_habilitacion(id_medico) == "true":
                    if len(obtener_rango_horario(id_medico, dia_solicitado)) > 0:
                        inicioHorario_medico = datetime.strptime(obtener_rango_horario(id_medico, dia_solicitado)[0], "%H:%M")
                        finHorario_medico = datetime.strptime(obtener_rango_horario(id_medico, dia_solicitado)[1], "%H:%M")
                        if(inicioHorario_medico.hour < hora_solicitada.hour <= finHorario_medico.hour):
                            turnos.append({
                                "id_medico" : id_medico,
                                "id_paciente" : id_paciente,
                                "hora_turno" : hora_turno,
                                "fecha_turno" : fecha_turno,
                                "fecha_solicitud" : fecha_actual,
                                        })
                            exportar_a_csv()
                            return turnos[-1]
                        else:
                            return "Hora no valida"
                    else:
                        return "El medico no trabaja ese dia"
                else:
                    return "No hay habilitacion"
            else:
                return "Fecha no valida para registrar un turno"  
                                        
def validar_hora(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
    except ValueError:
        return False
    
    return 0 <= hora.hour < 24 and 0 <= hora.minute < 60

def validar_hora(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
    except ValueError:
        return False
    
    return 0 <= hora.hour < 24 and 0 <= hora.minute < 60

def validar_id_medico(id_str):
    try:
        id = int(id_str)
    except ValueError:
        return False
    
    return 1 <= id <= obtener_maximo_id_medico()

def validar_id_paciente(id_str):
    try:
        id = int(id_str)
    except ValueError:
        return False
    
    return 1 <= id <= obtener_maximo_id_paciente()

def eliminar_turno_id(id_medico):
    global turnos
    turnos = [turno for turno in turnos if turno["id_medico"] != id_medico]
    exportar_a_csv()

def obtener_dias_medico(id_medico):
    dias = []
    with open(ruta_archivo_agenda, newline='', encoding="utf8") as csvfile:
        lector = csv.reader(csvfile)  
        next(lector)  
        for fila in lector:
            if (fila[0]) == id_medico:
                dia = fila[1]
                dias.append(dia)
    return dias

def obtener_habilitacion(id_medico):
    with open(ruta_archivo_medicos, newline='', encoding="utf8") as csvfile:
        lector = csv.reader(csvfile)  
        next(lector)
        for fila in lector:
            if int(fila[0]) == id_medico:
                habilitado = fila[7]
    return habilitado

def obtener_rango_horario(id_medico, dia_numero):
    rango = []
    with open(ruta_archivo_agenda, newline='', encoding="utf8") as csvfile:
        lector = csv.reader(csvfile)  
        next(lector)  
        for fila in lector:
            if int(fila[0]) == id_medico and int(fila[1]) == dia_numero:
                rango.append(fila[2])
                rango.append(fila[3])
    return rango
    
