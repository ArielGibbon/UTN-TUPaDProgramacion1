print ("BIENVENIDO A LA BIBLIOTECA ESCOLAR")
opciones_menu = ["1. Ingresar Titulos (sin ejemplares)",
                 "2. Ingresar ejemplares",
                 "3. Mostrar catalogo",
                 "4. Consultar disponibilidad",
                 "5. Listar agotados",
                 "6. Agregar título",
                 "7. Actualizar ejemplares (prestamos/devoluciones)",
                 "8. Salir"
                 ]
titulos = []
ejemplares = []

while True:
    print ("---MENU BIBLIOTECA---")
    for opcion in opciones_menu:
        print (opcion)
    seleccion = input("Elija una opcion " )

    print ("=========================================================================")

    if seleccion == "1":
        titulo = input("Ingrese el Título " )
       
        while titulo in titulos or titulo == "":
            print("****************")
            print("Título repetido o inválido. Intente nuevamente")
            titulo = input("Ingrese nuevamente el Título")
            print("****************")
            print(f"Título ingresado {titulo}")
            titulos.append(titulo)
            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, 0)
    
    elif seleccion == "2":
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        for i , titulo in enumerate (titulos):
            print(f"{i + 1} . {titulo}")
        posicion = int(input("Seleccione el número de título que va a ingresar ejemplares: ")) - 1

        while posicion < 0 or posicion >= len(titulos):
            print ("Posición inválida. Intente nuevamente")
            posicion = int(input("Seleccione el número de título que va a ingresar ejemplares: ")) - 1
        
        cantidad = int(input("Ingrese la cantidad de ejemlpares"  ))
        ejemplares[posicion]+= cantidad
        print (f"Ejemplares dispoibles actualmente para {titulos[posicion]} : {ejemplares[posicion]}")
    
    elif seleccion == "3":
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        print("----Catálogo de libros----")
        for i , titulo in enumerate (titulos):
            print(f"{i + 1} . {titulo}")

    elif seleccion == "4":
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        titulo_consulta = input("Ingresar el Título a consultar")

        while True:
            if titulo_consulta in titulos:
                posicion = titulos.index(titulo_consulta)
                print (f"Ejemplares disponibles para {titulo_consulta} : {ejemplares[posicion]}")
                break
            else:
                print (f"El título {titulo_consulta} no se encuentra en el catálogo actual ")
                print ("Desea volverlo a ingresar? (s: vuelve a ingresar / n: volver al menú principal)")
                if input().lower() == "s":
                    titulo_consulta = input("Ingresar el Título a consultar ")
                else:
                    break

    elif seleccion == "5":
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        agotados = False

        for i in ejemplares:
            if i == 0:
                agotados = True
                break
        if agotados:
            print("---Libros agotados---")
            for titulo in titulos:
                posicion = titulos.index(titulo)
                if ejemplares[posicion] == 0:
                    print (titulo)

    elif seleccion == "6":
        nuevo_titulo = input("Ingresar el nuevo Título " )
        if nuevo_titulo in titulos:
            print(f"El título {nuevo_titulo} , ya existe en el catálogo")
        else:
            titulos.append(nuevo_titulo)
            cantidad = int(input(f"Ingresar la cantidad para {nuevo_titulo}"))
            posicion = titulos.index(nuevo_titulo)
            ejemplares.insert(posicion, cantidad)
            print(f"El libro {nuevo_titulo}, ha sido ingresado al catálogo con {cantidad} ejemplares ")

    elif seleccion == "7":
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        for i, titulo in enumerate(titulos):
            print (f" {i+1 } . {titulo } ")
        posicion = int(input("Ingresar el número de libros: " )) -1
        accion = input("Ingrese 'p' para préstamo o 'd' para devolución:  " ).lower()

        if accion == "p":
            if ejemplares[posicion] > 0:
                ejemplares[posicion] -= 1
                print(f"Préstamo realizado. Ejemplares disponibles para {titulos[posicion ] } : {ejemplares[posicion]}")
            else:
                print(f"No hay ejemplares disponibles para {titulos[posicion]}")
        elif accion == "d":
            ejemplares[posicion]+= 1
            print("Devolución realizada")
        else:
            print("La acción es inválida. Use 'p' o 'd' ")



    elif seleccion == "8":
        print ("Fin del programa")
        break
       

    
       