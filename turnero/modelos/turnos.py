import csv
import datetime
def cargar_datos_turnos():
    datos = []
    try:
        with open('modelos/turnos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        pass
    return datos

def guardar_datos_turnos(datos):
    with open('modelos/turnos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id_medico', 'id_paciente', 'hora_turno', 'fecha_solicitud']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for turno in datos:
            writer.writerow(turno)