import requests
import csv

# Lista de pacientes en memoria (diccionarios)
pacientes = []

# Función para cargar pacientes desde la API randomuser y escribir en CSV
def cargar_pacientes_desde_api_y_guardar_en_csv(cantidad=10):
    url = f'https://randomuser.me/api/?results={cantidad}&inc=id,dni,name,phone,email,location'
    response = requests.get(url)
    data = response.json()

    for result in data.get('results', []):
        paciente = {
            "id": len(pacientes) + 1,
            "dni": result["id"]["value"],
            "nombre": result["name"]["first"],
            "apellido": result["name"]["last"],
            "telefono": result["phone"],
            "email": result["email"],
            "direccion_calle": result["location"]["street"]["name"],
            "direccion_numero": result["location"]["street"]["number"]
        }
        pacientes.append(paciente)

    # Escribir los datos en pacientes.csv
    with open('modelos/pacientes.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["id", "dni", "nombre", "apellido", "telefono", "email", "direccion_calle", "direccion_numero"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Escribir el encabezado solo si el archivo está vacío
        if csv_file.tell() == 0:
            writer.writeheader()

        # Escribir cada paciente en una nueva fila
        for paciente in pacientes:
            writer.writerow(paciente)

# Cargar algunos pacientes iniciales desde la API al inicio de la aplicación
cargar_pacientes_desde_api_y_guardar_en_csv(5)
