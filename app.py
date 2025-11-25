#we import funcions because we need to use them
from funciones import mostrar,agregar,calcular,buscar,eliminar,agregar1
#i make the list ventas 
ventas = [
    {"cliente" : "jaime","producto" : "100 años","cantidad": 2,"fecha": "sabado","precio": 10000},
    {"cliente" : "sara","producto" : "crepusculo","cantidad": 20,"fecha": "lunes","precio": 2000},
    {"cliente" : "jose","producto" : "100 habitos atomicos","cantidad": 50,"fecha": "sabado","precio": 20000},
    {"cliente" : "juan","producto" : "los 3 cerditos","cantidad": 45,"fecha": "sabado","precio": 15000}
          ]
#i make the list inventario
inventario = [
     {"title" : "100 años","author" : "gabriel garcia marquez", "category" : "fiction", "price" : 10000, "amount": 20},
     {"title" : "habitos atomicos","author" : "stranger", "category" : "personal growth", "price" : 20000, "amount": 5},
     {"title" : "el club de las 5 ","author" : "stranger", "category" : "personal growth", "price" : 50000, "amount": 34},
     {"title" : "crepusculo","author" : "stranger", "category" : "romantic", "price" : 2000, "amount": 100},
     {"title" : "los 3 cerditos","author" : "stranger", "category" : "children", "price" : 15000, "amount": 7}
     ]
inicio = True
#this is the begin of loop
while inicio == True:
    #this is the menu that the user will see
    print("1.add product")
    print("2. show inventory")
    print("3. update")
    print("4. remove")
    print("5. sales")
    print("6. reportes")
    print("7. guardar csv")
    print("8. cargar cvs")
    print("9. show sales")
    print("10. exit")
    #i make opcion for save the user anwser
    opcion = int(input("ingrese una opcion"))
    # in this opcion we add a data from a book i use try for mistakes and while for the loop 
    if opcion == 1:
        try:
            while True:
                #this is the necesary data for the inventory
                titulo = input("write the title of the book")
                if not titulo.strip():
                    print("entrada vacia ")
                    continue
                autor = input("write the author of the book")
                if not autor.strip():
                    print("entrada vacia ")
                    continue
                categoría = input("write category")
                if not categoría.strip():
                    print("entrada vacia ")
                    continue
                precio = int(input("write price"))
                cantidad = int(input("write how much"))
                #i create nuevo_usuario for save the result of agregar funcion
                nuevo_usuario = agregar(titulo, autor, categoría, precio, cantidad)
                #this is for save the result in inventario
                inventario.append(nuevo_usuario)
                #i print inventario for ensurance 
                print(inventario)
                #i ask to user if he want to add another book,if the anwser is yes we start a new register,if not we go out the loop 
                salir_registro = input("do you want to register other title?")
                if salir_registro == "yes":
                    print("the title is added")
                    continue
                else:
                    break
        except IOError:
            print(f"❌ should to be a correct value")
    elif opcion == 2:
         mostrar(inventario)
    elif opcion == 3:
        nombre_buscado = input("write the title that you want to find: ").lower()
        buscar(inventario,nombre_buscado)
    elif opcion == 4:
        eliminar(inventario)
    elif opcion == 5:
        #this is similar to opcion 1 because we need to register a sales
        chose = input("do you want to register a sell?")
        while True:
            if chose == "yes":
                #we ask to customers the necesary data
                print("beging the sell")
                print("estos son los productos disponibles")
                #cliente, producto vendido,cantidad, fecha y descuento (si aplica).
                cliente = input("ingrese el nombre del cliente")
                if not cliente.strip():
                    print("entrada vacia ")
                    continue
                titulo = input("ingrese el producto vendido")
                if not titulo.strip():
                    print("entrada vacia ")
                    continue
                cantidad = input("ingrese la cantidad de productos vendidos")
                if not cantidad.strip():
                    print("entrada vacia ")
                    continue
                fecha = input("ingrese el dia actual")
                precio = int(input("write price"))
                #i create nuevo_usuario for save the result of agregar funcion
                nuevo_usuario = agregar1(cliente, titulo,cantidad,fecha,precio)
                #this is for save the result in ventas
                ventas.append(nuevo_usuario)
                print(ventas)
                mostrar(inventario)
                #i ask to user if he want to add another book,if the anwser is yes we start a new register,if not we go out the loop 
                salir_registro = input("do you want to register other sell?")
                if salir_registro == "yes":
                    print("the title is added")
                    continue
                else:
                    break   

    elif opcion == 6:
        calcular(ventas)
    elif opcion == 7:
        print
    elif opcion == 8:
        print
    elif opcion == 9:
        print(ventas)
    elif opcion == 10:
        print("exit the sistem")
        break
    else:
         print("write a correct data")

#this code work with a funcions for more efective inicialization you have a menu and in this you can to chose between
#the opcions, and in 1 opcion you can register a new book in the list inventory you only need to provide the necesary data
#with the 2 opcion you can show the inventory
#with the 3 opcion you can search any book that you want to find
#with the 4 opcion you can remove any book to the library you only need provide the necesary data
# with the 5 opcion you can add a new sell
#with the 6 opcion you can know what is the most seller book in the company and you can know what is the sales amount
#with hte 10 opcion you can finish the sistem 