import requests
import csv
import os

def guardar_datos_en_csv(datos, archivo_csv):
    # Verificar si el archivo CSV ya existe
    existe_archivo = os.path.exists(archivo_csv)

    # Modo de apertura del archivo dependiendo de si ya existe o no
    modo = 'a' if existe_archivo else 'w'

    # Abrir el archivo CSV en modo de escritura
    with open(archivo_csv, mode=modo, newline='') as csvfile:
        # Definir los nombres de las columnas del CSV
        fieldnames = ['id', 'dni', 'nombre', 'apellido', 'telefono', 'email', 'direccion_calle', 'direccion_numero']

        # Crear un objeto DictWriter pero no se si se puede usar objetos
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir la cabecera solo si es un archivo nuevo
        if not existe_archivo:
            writer.writeheader()

        # Escribir los datos en el archivo CSV
        writer.writerows(datos)

def cargar_datos_con_API(cantidad=1):
    url = f'https://randomuser.me/api/?results={cantidad}'

    try:
        # Realiza una solicitud GET a la API utilizando la biblioteca request
        respuesta = requests.get(url)

        # Verificar si hubo errores en la solicitud
        respuesta.raise_for_status()

        # Obtener la respuesta en formato JSON
        datos_en_json = respuesta.json()

        # Extraer la información de los pacientes de la clave 'results' en el JSON
        pacientes = datos_en_json.get('results', [])

        # Guardar los datos en el archivo CSV pacientes.csv en la carpeta modelos
        guardar_datos_en_csv(pacientes, 'modelos/pacientes.csv')

        # Devuelve la lista de pacientes
        return pacientes
    
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        # Devolver None para indicar que la solicitud falló
        return None

cargar_datos_con_API()
