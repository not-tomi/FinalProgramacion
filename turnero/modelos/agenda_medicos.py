import csv
import os

agenda_medicos = []
id_horario_medico = 1
ruta_archivo_agenda = "modelos/agenda_medicos.csv"

def importar_datos_desde_csv():
    global agenda_medicos
    global id_horario_medico
    agenda_medicos = []  
    with open(ruta_archivo_agenda, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id_medico'] = int(row['id_medico'])
            agenda_medicos.append(row) 
    if len(agenda_medicos)>0:
        id_horario_medico= agenda_medicos[-1]["id_medico"]+1
    else:
        id_horario_medico = 1

def exportar_a_csv():
    with open(ruta_archivo_agenda, 'w', newline='', encoding="utf8") as csvfile:
        campos = ['id_medico', 'dia_numero', 'hora_inicio','hora_fin','fecha_actualizacion']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for horario in agenda_medicos:
            writer.writerow(horario)

def inicializar_agenda():
    global id_horario_medico
    if os.path.exists(ruta_archivo_agenda):
        importar_datos_desde_csv()

def obtener_cantidad_horarios():
    global id_horario_medico
    return id_horario_medico

def obtener_horarios():
    return agenda_medicos

def obtener_horarios_id(id_medico):
    horarios_desorganizados = []
    if(id_medico >= 1 and id_medico <= obtener_cantidad_horarios()):
        for horario in agenda_medicos:
            if horario["id_medico"] == id_medico:
                horarios_desorganizados.append(horario)
        horarios_organizados = sorted(horarios_desorganizados, key=lambda x: x['dia_numero'])
        return horarios_organizados
    else:
        return None
    
