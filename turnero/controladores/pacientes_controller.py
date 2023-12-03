import requests #biblioteca para hacer peticiones http
import csv

def cargar_datos_con_API(cantidad=1):

    url = f'https://randomuser.me/api/?results={cantidad}'
    
    try:
        # Realizar una solicitud GET a la API utilizando la biblioteca 'requests'
        respuesta = requests.get(url)

        # Verificar si hubo errores en la solicitud
        respuesta.raise_for_status()

        # Obtener la respuesta en formato JSON
        DatosEnJson = respuesta.json()

        # Extraer la información de los pacientes de la clave 'results' en el JSON
        pacientes = datos_json.get('results', [])

        # Devolver la lista de pacientes
        return pacientes

    #se guarda el error en la variable e para imprimirlo luego
    except requests.exceptions.RequestException as e:

        print(f"Error en la solicitud: {e}")

        # Devolver None para indicar que la solicitud falló
        return None
