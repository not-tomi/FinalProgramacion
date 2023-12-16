import csv
import os
from datetime import *

hoy = datetime.now()
agenda_medicos = []
ruta_archivo_agenda = "modelos/agenda_medicos.csv"

def importar_datos_desde_csv():
    global agenda_medicos
    agenda_medicos = []  
    with open(ruta_archivo_agenda, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id_medico'] = int(row['id_medico'])
            agenda_medicos.append(row)

def exportar_a_csv():
    with open(ruta_archivo_agenda, 'w', newline='', encoding="utf8") as csvfile:
        campos = ['id_medico', 'dia_numero', 'hora_inicio','hora_fin','fecha_actualizacion']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for horario in agenda_medicos:
            writer.writerow(horario)

def inicializar_agenda():
    if os.path.exists(ruta_archivo_agenda):
        importar_datos_desde_csv()

def obtener_maximo_id():
    mayor = None 
    with open(ruta_archivo_agenda, newline='', encoding="utf8") as csvfile:
        lector = csv.reader(csvfile)  
        next(lector)  
        for fila in lector:
            valor = int(fila[0])
            if mayor is None or valor > mayor:
                mayor = valor
    return mayor

def obtener_horarios():
    return agenda_medicos

def obtener_horarios_id(id_medico):
    horarios_desorganizados = []
    for horario in agenda_medicos:
            if horario["id_medico"] == id_medico:
                horarios_desorganizados.append(horario)
    horarios_organizados = sorted(horarios_desorganizados, key=lambda x: x['dia_numero'])
    return horarios_organizados

def crear_horario(id_medico,dia_numero, hora_inicio, hora_fin):
    agenda_medicos.append({
            "id_medico" : id_medico,
            "dia_numero" : dia_numero,
            "hora_inicio" : hora_inicio,
            "hora_fin" : hora_fin,
            "fecha_actualizacion" : hoy,
        })
    exportar_a_csv
    return agenda_medicos[-1]

def modificar_horario_id(id_medico, dia_numero, hora_inicio, hora_fin):
    for horario in agenda_medicos:
            if horario["id_medico"] == id_medico:
                horario["dia_numero"] = dia_numero
                horario["hora_inicio"] = hora_inicio
                horario["hora_fin"] = hora_fin
                horario["fecha_actualizacion"] = hoy
                exportar_a_csv
                return horario

def validar_hora(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
    except ValueError:
        return False
    
    return 0 <= hora.hour < 24 and 0 <= hora.minute < 60

def validar_dia(dia_str):
    try:
        dia = int(dia_str)
    except ValueError:
        return False
    
    return 1 <= dia <= 6
    
def eliminar_horario_id(id_medico):
    global agenda_medicos
    agenda_medicos = [horario for horario in agenda_medicos if horario["id_medico"] != id_medico]
    exportar_a_csv()