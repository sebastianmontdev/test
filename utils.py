def format_data_for_display(data_list):
    """
    Recibe una lista de diccionarios y la convierte en una lista de tuplas 
    para su visualización (Tupla: colección inmutable).
    """
    if not data_list:
        return []
        
    # El encabezado es la clave del primer diccionario
    header = list(data_list[0].keys())
    
    # Crea una lista de tuplas. La primera tupla es el encabezado.
    display_list = [tuple(header)]
    for item in data_list:
        # Cada fila es una tupla con los valores
        display_list.append(tuple(item.values()))
        
    return display_list

def display_statistics(stats_dict, *args):
    """
    Muestra estadísticas con un título principal y subtítulos opcionales.
    Uso de *args para subtítulos dinámicos.
    """
    print("\n📊 --- REPORTE ESTADÍSTICO --- 📊")
    
    # Imprime los subtítulos usando *args
    if args:
        for subtitle in args:
            print(f"| {subtitle.upper()} |")
            
    # Imprime las estadísticas del diccionario
    for key, value in stats_dict.items():
        print(f"  - {key.replace('_', ' ').title()}: **{value}**")
        
    print("---------------------------------")

def classify_by_rarity(data_list, **kwargs):
    """
    Clasifica los artefactos por nivel de rareza y aplica filtros adicionales 
    usando **kwargs.
    Retorna un diccionario: {'rareza': [lista_de_artefactos]}
    """
    classified = {}
    
    for item in data_list:
        # Filtra por **kwargs (ej: estatus='Almacenado')
        is_filtered = True
        for key, value in kwargs.items():
            if item.get(key) != value:
                is_filtered = False
                break
        
        if is_filtered and 'rareza' in item:
            rarity = item['rareza']
            if rarity not in classified:
                classified[rarity] = []
            classified[rarity].append(item)
            
    return classified