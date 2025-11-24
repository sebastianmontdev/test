import csv
import os

# Define los nombres de los archivos
ADMIN_FILE = 'admin_access.csv'
VISITORS_FILE = 'visitantes.csv'
ARTIFACTS_FILE = 'artefactos.csv'

def load_data(filename, default_header):
    """
    Carga los datos de un archivo CSV. Si no existe, crea el archivo con el encabezado.
    Retorna una lista de diccionarios con los datos.
    """
    data = []
    if not os.path.exists(filename):
        print(f"Creando archivo: {filename}")
        save_data(filename, [], default_header)
        return []

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except Exception as e:
        print(f"Error al leer {filename}: {e}")
    
    return data

def save_data(filename, data_list, header):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(data_list)
        return True
    except Exception as e:
        print(f"Error al guardar en {filename}: {e}")
        return False

# --- Inicialización de Archivos ---

# 1. admin_access.csv
ADMIN_HEADER = ['username', 'password', 'role']
ADMIN_DATA = [
    {'username': 'GLK_Admin', 'password': 'superpassword2487', 'role': 'SUPERADMIN'}
]

if not os.path.exists(ADMIN_FILE):
    save_data(ADMIN_FILE, ADMIN_DATA, ADMIN_HEADER)

# 2. visitantes.csv
VISITORS_HEADER = ['id', 'nombre', 'especie', 'estado']
if not os.path.exists(VISITORS_FILE):
    save_data(VISITORS_FILE, [], VISITORS_HEADER)

# 3. artefactos.csv
ARTIFACTS_HEADER = ['codigo', 'descripcion', 'rareza', 'estatus']
if not os.path.exists(ARTIFACTS_FILE):
    save_data(ARTIFACTS_FILE, [], ARTIFACTS_HEADER)