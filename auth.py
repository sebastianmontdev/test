import storage
import hashlib

# Usa el header definido en storage.py
ADMIN_HEADER = storage.ADMIN_HEADER

def load_admin_credentials():
    """Carga las credenciales del único administrador del CSV."""
    # Los datos son cargados como lista de diccionarios
    admin_data_list = storage.load_data(storage.ADMIN_FILE, ADMIN_HEADER)
    if admin_data_list:
        # Retorna el primer y único registro como diccionario
        return admin_data_list[0]
    return None

def login(attempts=3):
    """
    Función recursiva para manejar el inicio de sesión del administrador.
    """
    if attempts == 0:
        print("\n🚫 Has agotado los intentos. Acceso denegado. Cerrando sistema.")
        return False

    admin_creds = load_admin_credentials()
    if not admin_creds:
        print("\n❌ Error: No se encontraron credenciales de administrador.")
        return False

    print(f"\n🔑 INTENTO DE LOGIN - Quedan {attempts} intentos")
    username = input("   ID de administrador: ").strip()
    password = input("   Contraseña: ").strip()

    # Validación
    if username == admin_creds['username'] and password == admin_creds['password']:
        print("\n✅ Acceso concedido. Bienvenido, SUPERADMIN.")
        return True
    else:
        print("\n⚠️ Credenciales incorrectas.")
        # Llamada recursiva con un intento menos
        return login(attempts - 1)