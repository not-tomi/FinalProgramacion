import csv

def cargar_datos_medicos():
    datos = []
    try:
        with open('medicos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        #  excepción si el archivo no existe, es una palabra reservada 
        pass
    return datos

def guardar_datos_medicos(datos):
    with open('medicos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'dni', 'nombre', 'apellido', 'matricula', 'telefono', 'email', 'habilitado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for medico in datos:
            writer.writerow(medico)