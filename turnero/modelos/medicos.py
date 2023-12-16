import requests
import csv

medicos = []
url = f'https://randomuser.me/api/?results=10&inc=id,dni,name,phone,email,location,login&password=number,6-6'
ruta_archivo_medicos = "modelos/medicos.csv"

def obtener_datos_desde_api():
    response = requests.get(url)
    datos = response.json()
    
    for result in datos.get('results', []):
        password = result["login"]["password"]
        hashdni = sum(ord(char) for char in password)

    for result in datos.get('results', []):
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
    
    with open(ruta_archivo_medicos, 'w', newline='', encoding='utf-8') as archivo_csv:
        fieldnames = ["id", "dni", "nombre", "apellido", "matricula", "telefono", "email", "habilitado"]
        writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
        
        if archivo_csv.tell() == 0:
            writer.writeheader()

        for medico in medicos:
            writer.writerow(medico)
    
    return medicos

