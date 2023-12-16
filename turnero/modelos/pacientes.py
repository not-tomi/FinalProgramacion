import requests
import csv


pacientes = []

def cargar_pacientes_desde_api_y_guardar_en_csv(cantidad=1):
    url = f'https://randomuser.me/api/?results={cantidad}&inc=id,dni,name,phone,email,location,login&password=number,6-6'
    response = requests.get(url)
    data = response.json()

    for result in data.get('results', []):
        password = result["login"]["password"]
        hashdni = sum(ord(char) for char in password)
        hashdni = hashdni % (10 ** 8)

    for result in data.get('results', []):
        paciente = {
            "id": len(pacientes) + 1,
            "dni": hashdni,
            "nombre": result["name"]["first"],
            "apellido": result["name"]["last"],
            "telefono": result["phone"],
            "email": result["email"],
            "direccion_calle": result["location"]["street"]["name"],
            "direccion_numero": result["location"]["street"]["number"]
        }
        pacientes.append(paciente)

    with open('modelos/pacientes.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["id", "dni", "nombre", "apellido", "telefono", "email", "direccion_calle", "direccion_numero"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if csv_file.tell() == 0:
            writer.writeheader()

        for paciente in pacientes:
            writer.writerow(paciente)
cargar_pacientes_desde_api_y_guardar_en_csv(1)
