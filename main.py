import auth
import visitors
import artifacts
import os
import sys

def clear_screen():
    """Limpia la consola para una mejor experiencia."""
    os.system('cls' if os.name == 'nt' else 'clear')

def visitors_menu():
    """Menú de gestión de Visitantes Intergalácticos."""
    while True:
        print("\n\n--- 🚀 MÓDULO DE VISITANTES INTERGALÁCTICOS ---")
        print("1. Registrar visitante")
        print("2. Listar visitantes")
        print("3. Buscar visitante por ID")
        print("4. Actualizar estado")
        print("5. Eliminar visitante (Marcar 'Eliminado')")
        print("6. Estadísticas de visitantes")
        print("0. Volver al Menú Principal")
        
        choice = input("Seleccione una opción: ")
        clear_screen()
        
        if choice == '1':
            visitors.register_visitor()
        elif choice == '2':
            visitors.list_visitors()
        elif choice == '3':
            visitors.search_visitor()
        elif choice == '4':
            visitors.update_visitor_status()
        elif choice == '5':
            visitors.delete_visitor()
        elif choice == '6':
            visitors.get_visitor_stats()
        elif choice == '0':
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

def artifacts_menu():
    """Menú de gestión de Artefactos Recuperados."""
    while True:
        print("\n\n--- 💎 MÓDULO DE ARTEFACTOS RECUPERADOS ---")
        print("1. Registrar artefacto")
        print("2. Listar artefactos")
        print("3. Buscar artefacto por Código")
        print("4. Clasificar artefactos por rareza (**kwargs)")
        print("5. Estadísticas de artefactos")
        print("6. Eliminar artefacto (Marcar 'Destruido')")
        print("0. Volver al Menú Principal")
        
        choice = input("Seleccione una opción: ")
        clear_screen()
        
        if choice == '1':
            artifacts.register_artifact()
        elif choice == '2':
            artifacts.list_artifacts()
        elif choice == '3':
            artifacts.search_artifact()
        elif choice == '4':
            artifacts.classify_artifacts_menu()
        elif choice == '5':
            artifacts.get_artifact_stats()
        elif choice == '6':
            artifacts.delete_artifact()
        elif choice == '0':
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")


def main_menu():
    """Menú principal del sistema Galactic Library Keeper."""
    while True:
        print("\n\n=== 🌌 GALACTIC LIBRARY KEEPER v1.0 ===")
        print("1. Gestionar Visitantes Intergalácticos")
        print("2. Gestionar Artefactos Recuperados")
        print("0. Salir del Sistema")
        
        choice = input("Seleccione un módulo: ")
        clear_screen()
        
        if choice == '1':
            visitors_menu()
        elif choice == '2':
            artifacts_menu()
        elif choice == '0':
            print("\n👋 Gracias por usar Galactic Library Keeper. ¡Apagado seguro!")
            sys.exit(0)
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    clear_screen()
    print("-----------------------------------------------------")
    print("--- INICIANDO GALACTIC LIBRARY KEEPER (2487) ---")
    print("-----------------------------------------------------")

    # 1. Inicio de sesión del administrador (recursivo)
    if auth.login():
        clear_screen()
        main_menu()
    else:
        # El login ya maneja el mensaje de denegado y salida si se agotan los intentos
        sys.exit(1)