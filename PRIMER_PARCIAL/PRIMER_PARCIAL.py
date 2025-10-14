print ("BIENVENIDO A LA BIBLIOTECA ESCOLAR")

# Enunciado
# La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
# copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
# utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
# vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
# Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
# elija salir.


print ("BIENVENIDO A LA BIBLIOTECA ESCOLAR")  #armar el menu
opciones_menu = ["1. Ingresar Titulos (sin ejemplares)",
                 "2. Ingresar ejemplares",
                 "3. Mostrar catalogo",
                 "4. Consultar disponibilidad",
                 "5. Listar agotados",
                 "6. Agregar título",
                 "7. Actualizar ejemplares (prestamos/devoluciones)",
                 "8. Salir"
                 ]
titulos = ['Harry Potter', 'Matar a un ruiseñor', 'Orgullo y prejuicio'] #cargamos los primeros libros para que al ejecutar no haya que crea las listas cada vez
ejemplares = [5, 3, 7] #listamos la cantidad de ejemplares


#se muestra el manu
while True:
    print ("---MENU BIBLIOTECA---")
    for opcion in opciones_menu:
        print (opcion)
    seleccion = input("Elija una opcion " )

    print ("=========================================================================") # separador
    #opcion '1' se solicita el ingreso  del titulo de un libro
    #se valida que no este repetido o que no este en blanco
    #se ingresa con append y se lo vincula (index , insert) con la posicion en la lista de cantidad de ejemplares

    if seleccion == "1":
        titulo = input("Ingrese el Título " )
       
        while titulo in titulos or titulo == "":
            print("****************")
            print("Título repetido o inválido. Intente nuevamente")
            titulo = input("Ingrese nuevamente el Título " )
            print("****************")
        print(f"Título ingresado: {titulo}")
        titulos.append(titulo)
        posicion = titulos.index(titulo)
        ejemplares.insert(posicion, 0)
    
    elif seleccion == "2":
        #se valida que haya al menos un titulo existente
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        # se numera el titulo para saber a cual se va a incorporar la cantidad de ejemplares
        for i , titulo in enumerate (titulos):
            print(f"{i + 1} . {titulo}")
        posicion = int(input("Seleccione el número de título que va a ingresar ejemplares: " ) ) - 1

        #validacion de posicion existente
        while posicion < 0 or posicion >= len(titulos):
            print ("Posición inválida. Intente nuevamente")
            posicion = int(input("Seleccione el número de título que va a ingresar ejemplares: " ) ) - 1
        
        #se ingresa la cantidad de ejemplares (lista ejemplares)y se imprime
        # los titulos por orden de posicion (lista titulos) vinculada con la cantidad de ejemplares
        cantidad = int(input("Ingrese la cantidad de ejemlpares  "  ) )
        ejemplares[posicion]+= cantidad
        print (f"Ejemplares disponibles actualmente para {titulos[posicion]} : {ejemplares[posicion]}")

    elif seleccion == "3":
        # validar que haya titulos 
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        #se imprimen las listas vinculadas de titulos y cantidad de ejemplares
        print("----Catálogo de libros----")
        for i , titulo in enumerate (titulos):
            print(f"{i + 1} . {titulo} hay {ejemplares[i]} disponibles")

    elif seleccion == "4":
        #validar que haya titulos
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        
        titulo_consulta = input("Ingresar el Título a consultar:  " )

        #se verifica si el titulo ingresado esta en el catalogo
        #si esta se imprime titulo y cantidadde ejemplares,
        #si no esta se imprime que no se encuentra con la opcion de salir del menu o
        #volver a cargar el titulo
        while True:
            if titulo_consulta in titulos:
                posicion = titulos.index(titulo_consulta)
                print (f"Ejemplares disponibles para'  {titulo_consulta}  ': {ejemplares[posicion]}")
                break
            else:
                print (f"El título ' {titulo_consulta}  ' no se encuentra en el catálogo actual ")
                print ("Desea volverlo a ingresar? (s: vuelve a ingresar / n: volver al menú principal)")
                if input().lower() == "s":
                    titulo_consulta = input("Ingresar el Título a consultar")
                else:
                    break

    elif seleccion == "5":
        #validar que haya titulos
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        #buscamos si hay algun titulo agotado, usando una bandera, iniciada false
        #Busco en la lista ejemplares los que tenga contidad 0. 
        # Si hay al menos uno (o la cantidad que haya), los imprimo. 
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

    elif seleccion == "6": # carga un nuevo libro(titulo) ,en lista titulos, y su cantidad 
        #(en lista ejemplares) en una sola opcion de menu
        
        #validar si el titulo es nuevo o ya existe
        #se lo carga en lista titulos y vincula con lista ejemplares
        #se imprime
        nuevo_titulo = input("Ingresar el nuevo Título " )
        if nuevo_titulo in titulos:
            print(f"El título {nuevo_titulo} , ya existe en el catálogo")
        else:
            titulos.append(nuevo_titulo)
            cantidad = int(input(f"Ingresar la cantidad para {nuevo_titulo}  "))
            posicion = titulos.index(nuevo_titulo)
            ejemplares.insert(posicion, cantidad)
            print(f"El libro {nuevo_titulo}, ha sido ingresado al catálogo con {cantidad} ejemplares ")    

    elif seleccion == "7":
    #validar que haya titulos
        if not titulos:
            print("No hay títulos ingresados. Para ingresar cantidades, primero debe haber títulos")
            continue

        #se imprime y numera los titulos existentes y se solicita la eleccion del titulo y la accion a seguir
        for i, titulo in enumerate(titulos):
            print (f" {i+1 } . {titulo } ")
        posicion = int(input("Ingresar el número del libros: " )) -1
        accion = input("Ingrese 'p' para préstamo o 'd' para devolución:  " ).lower() #.lower para validar si se ingresa una 's' o 'p' mayuscula

        # se verifica que el titulo ni este agotado (lista de elementos de ese titulo en '0')
        #si la accion es prestamo 'p', se actualiza en -1 la lista ejemplares
        #si la accion es devolucion 'd' se actualiza en +1 la lista de ejemplares
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
            print("La acción es inválida. Use 'p' o 'd' ") #se invalida si no es una opcion

    elif seleccion == "8": 
        print ("Fin del programa!")
        break
                   