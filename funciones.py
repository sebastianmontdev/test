#in this funtion we'll try to calculate how is the most important sell and what is the total amount of the all sales
def calcular(inventario):
    try:
        total_inventario = 0
        unidades_totales = 0
        for i in inventario:
            unidades_totales = unidades_totales + i['cantidad']
            precio_total = i['precio'] * i['cantidad']
            total_inventario = total_inventario + precio_total
            cantidad = len(inventario)
            producto_mas_caro = max(inventario, key=lambda producto: producto['precio'])
            mayor_stock = max(inventario, key=lambda producto: producto['cantidad'])
        print(f"the total of products in cash is:", total_inventario)
        print(f"the most sell product is",mayor_stock)
    except IOError:
        print(f"❌ you should to write a correct value")
def mostrar(inventario):
    try:    
        for item in inventario:
           #titulo, autor,categoria,precio,cantidad
           print(f"title: {item['title']} | author: {item['author']} | category: {item['category']}  | price: {item['price']}  | amount: {item['amount']}")
    except IOError:
        print(f"❌ you should to write a correct value")

def agregar(titulo, autor,categoria,precio,cantidad):
    try:
        usuario = {}
        usuario['title'] = titulo
        usuario['author'] = autor
        usuario['category'] = categoria
        usuario['price'] = precio
        usuario['amount'] = cantidad
        
        return usuario
    except IOError:
        print(f"❌ you should to write a correct value")
#cliente, producto vendido,cantidad, fecha y descuento (si aplica)
def agregar1(cliente, producto,cantidad,fecha):
    try:
        usuario = {}
        usuario['custumer'] = cliente
        usuario['titlr'] = producto
        usuario['amount'] = cantidad
        usuario['date'] = fecha
        
        return usuario
    except IOError:
        print(f"❌ you should to write a correct value")

def buscar(inventario,nombre_buscado):
    try:
        for producto in inventario:
            if producto["nombre"].lower() == nombre_buscado:
                print("\n✅ Product founded:")
                print(f"   Nombre: {producto['nombre']}")
                return producto
            else:
                print("product non-existent")
    except IOError:
        print(f"❌ you should to write a correct value")


def eliminar(inventario):
    try:
        nombre_a_eliminar = input("write the title that you want to remove")
        elemento_encontrado = None
        for producto in inventario:
            if producto["title"] == nombre_a_eliminar:
                elemento_encontrado = producto
                break
        if elemento_encontrado:
            inventario.remove(elemento_encontrado)
            print(f"✅ Dicionary wiht name '{nombre_a_eliminar}' removed.")
        else:
            print(f"❌ Dicionary wiht name '{nombre_a_eliminar}' did not find.")
    except IOError:
        print(f"❌ you should to write a correct value")