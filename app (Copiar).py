import csv
from funciones import mostrar,agregar,calcular,buscar,guardar,cargar,eliminar
inventario = [
     {"titulo" : "100 años","autor" : "gabriel garcia marquez", "categoria" : "ficcion", "precio" : 10000, "cantidad": 20},
     {"titulo" : "habitos atomicos","autor" : "desconocido", "categoria" : "crecimiento personal", "precio" : 20000, "cantidad": 5},
     {"titulo" : "el club de las 5 ","autor" : "desconocido", "categoria" : "crecimiento personal", "precio" : 50000, "cantidad": 34},
     {"titulo" : "crepusculo","autor" : "desconocido", "categoria" : "romantico", "precio" : 2000, "cantidad": 100},
     {"titulo" : "loa 3 cerditos","autor" : "desconocido", "categoria" : "infantil", "precio" : 15000, "cantidad": 7}
     ]
#declaramos la fucion calcular


inicio = True
while inicio == True:
    print("1.Agregar producto")
    print("2. Mostrar inventario")
    print("3. buscar")
    print("4. actualizar")
    print("5. eliminar")
    print("6. estadisticas")
    print("7. guardar csv")
    print("8. cargar cvs")
    print("9. salir")
    opcion = int(input("ingrese una opcion"))
    if opcion == 1:
        while True:
            #título, autor, categoría, precio, cantidad en stock.
            título = input("ingrese el titulo del libro")
            autor = input("ingrese el nombre del autor")
            categoría = input("ingrese la categoria")
            precio = int(input("ingrese el precio"))
            cantidad = int(input("ingrese la cantidad"))

            nuevo_usuario = agregar(título, autor, categoría, precio, cantidad)
            print(inventario)
            salir_registro = input("desea registrar otro producto?")
            if salir_registro == "si":
                 print("inicia proceso de registro")
                 continue
            else:
                break
    elif opcion == 2:
         mostrar(inventario)
    elif opcion == 3:
        nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ").lower()
        buscar(inventario,nombre_buscado)
    elif opcion == 4:
        print()
    elif opcion == 5:
        nombre_a_eliminar = input("inserte el nombre del producto que desea eliminar")
        elemento_encontrado = None
        for producto in inventario:
            if producto["nombre"] == nombre_a_eliminar:
                elemento_encontrado = producto
                break
            if elemento_encontrado:
                inventario.remove(elemento_encontrado)
                print(f"✅ Diccionario con nombre '{nombre_a_eliminar}' eliminado.")
            else:
                print(f"❌ Diccionario con nombre '{nombre_a_eliminar}' no encontrado.")    
    elif opcion == 6:
        calcular(inventario)
    elif opcion == 7:
        guardar(inventario)
    elif opcion == 8:
        cargar(inventario)
    elif opcion == 9:
        print("saliendo del sistema")
        break
    else:
         print("ingrese un dato correcto")