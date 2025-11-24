import storage
import utils

VISITORS_HEADER = storage.VISITORS_HEADER

def get_visitor_ids(visitors_list):
    """Usa un SET para obtener todos los IDs de visitantes únicos."""
    return {v['id'] for v in visitors_list}

def load_visitors():
    """Carga los visitantes del CSV."""
    return storage.load_data(storage.VISITORS_FILE, VISITORS_HEADER)

def save_visitors(visitors_list):
    """Guarda la lista de visitantes en el CSV."""
    return storage.save_data(storage.VISITORS_FILE, visitors_list, VISITORS_HEADER)

def register_visitor():
    """Registra un nuevo visitante."""
    visitors = load_visitors()
    current_ids = get_visitor_ids(visitors)

    print("\n--- REGISTRAR NUEVO VISITANTE ---")
    
    while True:
        v_id = input("ID Único del Visitante: ").strip()
        if not v_id:
            print("⚠️ El ID no puede estar vacío.")
            continue
        if v_id in current_ids:
            print("❌ ID ya existe. Intente con otro.")
        else:
            break

    nombre = input("Nombre: ").strip()
    especie = input("Especie (Humano/Androide/Otros): ").strip().title()
    estado = 'Activo' # Estado inicial

    # Representación del visitante como un DICCIONARIO
    new_visitor = {
        'id': v_id,
        'nombre': nombre,
        'especie': especie,
        'estado': estado
    }

    visitors.append(new_visitor)
    if save_visitors(visitors):
        print(f"\n✅ Visitante **{nombre}** registrado exitosamente con ID: **{v_id}**.")
    else:
        print("\n❌ Error al guardar el visitante.")

def list_visitors():
    """Lista todos los visitantes cargados, mostrando datos como TUPLAS."""
    visitors = load_visitors()
    if not visitors:
        print("\nℹ️ No hay visitantes registrados.")
        return
        
    # Usamos la función auxiliar para convertir a TUPLAS
    display_data = utils.format_data_for_display(visitors)
    
    print("\n📜 --- LISTA DE VISITANTES INTERGALÁCTICOS ---")
    # Imprime el encabezado
    print(display_data[0]) 
    print("-" * 50)
    # Imprime las filas (tuplas)
    for row_tuple in display_data[1:]:
        print(row_tuple)
    print("---------------------------------------------")

def search_visitor():
    """Busca un visitante por ID."""
    v_id = input("Ingrese el ID del visitante a buscar: ").strip()
    visitors = load_visitors()
    
    found_visitor = next((v for v in visitors if v['id'] == v_id), None)
    
    if found_visitor:
        print("\n🔍 VISITANTE ENCONTRADO:")
        # Muestra el diccionario encontrado
        for key, value in found_visitor.items():
            print(f"  {key.title()}: **{value}**")
        return found_visitor
    else:
        print(f"\n❌ Visitante con ID **{v_id}** no encontrado.")
        return None

def update_visitor_status():
    """Actualiza el estado de un visitante (Activo/Retirado)."""
    v_id = input("Ingrese el ID del visitante para actualizar estado: ").strip()
    visitors = load_visitors()
    
    for i, v in enumerate(visitors):
        if v['id'] == v_id:
            current_status = v['estado']
            new_status = 'Retirado' if current_status == 'Activo' else 'Activo'
            
            # Actualiza el diccionario
            visitors[i]['estado'] = new_status
            
            if save_visitors(visitors):
                print(f"\n✅ Estado de **{v['nombre']}** actualizado: **{current_status}** -> **{new_status}**.")
            else:
                print("\n❌ Error al guardar la actualización.")
            return
            
    print(f"\n❌ Visitante con ID **{v_id}** no encontrado.")

def delete_visitor():
    """Elimina un visitante. (Opción B: Marcar 'Eliminado')."""
    # Justificación de Opción B en README.md: Marcar como 'Eliminado' mantiene
    # la integridad histórica y es más seguro que borrar permanentemente.
    v_id = input("Ingrese el ID del visitante a ELIMINAR (marcar): ").strip()
    visitors = load_visitors()
    
    for i, v in enumerate(visitors):
        if v['id'] == v_id:
            
            # Marcar "Eliminado" en el campo 'estado'
            visitors[i]['estado'] = 'Eliminado' 
            
            if save_visitors(visitors):
                print(f"\n✅ Visitante **{v['nombre']}** con ID **{v_id}** marcado como **Eliminado**.")
            else:
                print("\n❌ Error al guardar la eliminación.")
            return

    print(f"\n❌ Visitante con ID **{v_id}** no encontrado.")

def get_visitor_stats():
    """Calcula y muestra estadísticas de visitantes."""
    visitors = load_visitors()
    
    stats = {}
    
    # Total de visitantes
    stats['total_visitantes'] = len(visitors)
    
    if not visitors:
        utils.display_statistics(stats, "Visitantes", "Información General")
        return
        
    # Visitantes por especie (usando un diccionario)
    species_count = {}
    for v in visitors:
        species = v['especie']
        species_count[species] = species_count.get(species, 0) + 1
    
    stats['visitantes_por_especie'] = species_count
    
    # Visitantes activos vs retirados (usando un diccionario)
    status_count = {}
    for v in visitors:
        status = v['estado']
        status_count[status] = status_count.get(status, 0) + 1
        
    stats['estado_visitantes'] = status_count

    # Usa la función auxiliar con *args para títulos
    utils.display_statistics(
        stats, 
        "General", 
        "Por Especie", 
        "Por Estado"
    )