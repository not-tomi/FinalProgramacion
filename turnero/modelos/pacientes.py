import requests

# Lista de pacientes en memoria (diccionarios)
pacientes = []


# Función para cargar pacientes desde la API randomuser
def cargar_pacientes_desde_api(cantidad=10):

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

# Cargar algunos pacientes iniciales desde la API al inicio de la aplicación
cargar_pacientes_desde_api(5)
