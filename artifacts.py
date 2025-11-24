import storage
import utils

ARTIFACTS_HEADER = storage.ARTIFACTS_HEADER

def load_artifacts():
    """Carga los artefactos del CSV."""
    return storage.load_data(storage.ARTIFACTS_FILE, ARTIFACTS_HEADER)

def save_artifacts(artifacts_list):
    """Guarda la lista de artefactos en el CSV."""
    return storage.save_data(storage.ARTIFACTS_FILE, artifacts_list, ARTIFACTS_HEADER)

def get_artifact_codes(artifacts_list):
    """Usa un SET para obtener todos los códigos de artefactos únicos."""
    return {a['codigo'] for a in artifacts_list}

def register_artifact():
    """Registra un nuevo artefacto."""
    artifacts = load_artifacts()
    current_codes = get_artifact_codes(artifacts)

    print("\n--- REGISTRAR NUEVO ARTEFACTO ---")
    
    while True:
        code = input("Código Único del Artefacto: ").strip()
        if not code:
            print("⚠️ El Código no puede estar vacío.")
            continue
        if code in current_codes:
            print("❌ Código ya existe. Intente con otro.")
        else:
            break

    descripcion = input("Descripción: ").strip()
    
    valid_rarity = ['Bajo', 'Medio', 'Alto', 'Prohibido']
    while True:
        rareza = input(f"Nivel de rareza {valid_rarity}: ").strip().title()
        if rareza in valid_rarity:
            break
        print("⚠️ Nivel de rareza no válido.")
        
    estatus = 'Almacenado' # Estado inicial

    # Representación del artefacto como un DICCIONARIO
    new_artifact = {
        'codigo': code,
        'descripcion': descripcion,
        'rareza': rareza,
        'estatus': estatus
    }

    artifacts.append(new_artifact)
    if save_artifacts(artifacts):
        print(f"\n✅ Artefacto **{descripcion}** (Código: {code}) registrado exitosamente.")
    else:
        print("\n❌ Error al guardar el artefacto.")

def list_artifacts():
    """Lista todos los artefactos cargados, mostrando datos como TUPLAS."""
    artifacts = load_artifacts()
    if not artifacts:
        print("\nℹ️ No hay artefactos registrados.")
        return
        
    display_data = utils.format_data_for_display(artifacts)
    
    print("\n📜 --- LISTA DE ARTEFACTOS RECUPERADOS ---")
    print(display_data[0])
    print("-" * 50)
    for row_tuple in display_data[1:]:
        print(row_tuple)
    print("-----------------------------------------")

def search_artifact():
    """Busca un artefacto por código."""
    code = input("Ingrese el Código del artefacto a buscar: ").strip()
    artifacts = load_artifacts()
    
    found_artifact = next((a for a in artifacts if a['codigo'] == code), None)
    
    if found_artifact:
        print("\n🔍 ARTEFACTO ENCONTRADO:")
        for key, value in found_artifact.items():
            print(f"  {key.title()}: **{value}**")
        return found_artifact
    else:
        print(f"\n❌ Artefacto con Código **{code}** no encontrado.")
        return None

def classify_artifacts_menu():
    """
    Menú para clasificar artefactos usando **kwargs.
    El filtro por defecto es 'rareza', pero se puede añadir un filtro por 'estatus'.
    """
    artifacts = load_artifacts()
    if not artifacts:
        print("\nℹ️ No hay artefactos para clasificar.")
        return
        
    print("\n--- CLASIFICACIÓN DE ARTEFACTOS ---")
    filter_status = input("Filtrar por estatus (dejar vacío para clasificar todos): ").strip().title()
    
    filter_params = {}
    if filter_status in ['Almacenado', 'En Estudio', 'Destruido']:
        # Se pasa el filtro adicional como **kwargs
        filter_params['estatus'] = filter_status
        
    # Llamada a la función con **kwargs
    classified_data = utils.classify_by_rarity(artifacts, **filter_params)
    
    print("\n📦 ARTEFACTOS CLASIFICADOS:")
    for rarity, items in classified_data.items():
        print(f"  ## {rarity.upper()} ({len(items)}) ##")
        for item in items:
            print(f"    - [{item['codigo']}] {item['descripcion']} | Estatus: {item['estatus']}")
            
def get_artifact_stats():
    """Calcula y muestra estadísticas de artefactos."""
    artifacts = load_artifacts()
    
    stats = {}
    
    # Total de artefactos
    stats['total_artefactos'] = len(artifacts)
    
    if not artifacts:
        utils.display_statistics(stats, "Artefactos", "Información General")
        return
        
    # Artefactos por rareza (usando un diccionario)
    rarity_count = {}
    for a in artifacts:
        rarity = a['rareza']
        rarity_count[rarity] = rarity_count.get(rarity, 0) + 1
    
    stats['artefactos_por_rareza'] = rarity_count
    
    # Artefactos por estatus (usando un diccionario)
    status_count = {}
    for a in artifacts:
        status = a['estatus']
        status_count[status] = status_count.get(status, 0) + 1
        
    stats['estado_artefactos'] = status_count

    # Usa la función auxiliar con *args para títulos
    utils.display_statistics(
        stats, 
        "General", 
        "Por Nivel de Rareza", 
        "Por Estatus"
    )

def delete_artifact():
    """Elimina un artefacto. (Opción B: Marcar 'Destruido')."""
    code = input("Ingrese el Código del artefacto a ELIMINAR (marcar): ").strip()
    artifacts = load_artifacts()
    
    for i, a in enumerate(artifacts):
        if a['codigo'] == code:
            
            # Marcar "Destruido" en el campo 'estatus'
            artifacts[i]['estatus'] = 'Destruido' 
            
            if save_artifacts(artifacts):
                print(f"\n✅ Artefacto **{a['descripcion']}** marcado como **Destruido**.")
            else:
                print("\n❌ Error al guardar la eliminación.")
            return

    print(f"\n❌ Artefacto con Código **{code}** no encontrado.")