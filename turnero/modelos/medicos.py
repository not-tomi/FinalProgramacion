import csv

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