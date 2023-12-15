import requests
import csv

medicos = []

def cargar_medico_desde_API(cantidad=1):
    url = f'https://randomuser.me/api/?results={cantidad}&inc=id,dni,name,phone,email,location,login&password=number,6-6'
    response = requests.get(url)
    data = response.json()

    for result in data.get('results', []):
        password = result["login"]["password"]
        hashdni = sum(ord(char) for char in password)
        hashdni = hashdni % (10 ** 8)

    for result in data.get('results', []):
        medico = {
            "id": len(medicos) + 1,
            "dni": hashdni,
            "nombre": result["name"]["first"],
            "apellido": result["name"]["last"],
            "matricula": result["login"]["password"],
            "telefono": result["phone"],
            "email": result["email"],
            "habilitado": True,
        }
        medicos.append(medico)

    with open('modelos/medicos.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["id", "dni", "nombre", "apellido", "matricula", "telefono", "email", "habilitado"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        if csv_file.tell() == 0:
            writer.writeheader()

        for medico in medicos:
            writer.writerow(medico)

cargar_medico_desde_API(1)


