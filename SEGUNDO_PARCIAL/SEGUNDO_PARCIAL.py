import csv
import os

NOMBRE_ARCHIVO = "ejemplares.csv"

def obtener_ejemplares():
    ejemplares = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["TITULO","cantidad"])
            escritor.writeheader()

        return ejemplares

    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            ejemplares.append({"TITULO":fila["TITULO"], "cantidad": int(fila["cantidad"])})
    return ejemplares        

def existe_ejemplar(titulo):
    ejemplares = obtener_ejemplares()

    for ejemplar in ejemplares:
        if ejemplar["TITULO"].lower() == titulo.strip().lower():
            return True
    return False
def validar_numero(texto):
    if texto.isdigit():
        numero = int(texto)
        if numero > 0:
            return True
        else:
            print("Error: La cantidad debe ser mayor a 0")
            return False
    else:
        print("Error: Debe ingresar un número válido")
        return False
    
def mostrar_ejemplares():
    print("====CATALOGO DISPONIBLE====")
    ejemplares = obtener_ejemplares()
    
    print ("Titulo                     cantidad")
    for ejemplar in ejemplares:
        print(f"{ejemplar["TITULO"]} {ejemplar["cantidad"]}")

def agregar_ejemplares():
    print("====INGRESAR EJEMPLARES====")
    titulo = input("Ingrese el título del ejemplar: ").strip()

    if existe_ejemplar(titulo):
        print("El título ya está en existencia")
        return
    
    cantidad = input("Ingrese la cantidad ")
    if validar_numero (cantidad):
        cantidad = int(cantidad)

def guardar_ejemplares(ejemplares):
    
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "cantidad"])
        escritor.writeheader()
        escritor.writerows(ejemplares)

def ingresar_titulos():
    print("==== INGRESAR TÍTULOS ====")
    print("Ingrese los títulos con su cantidad (escriba 'fin' para terminar)\n")
    
    ejemplares = obtener_ejemplares()
    titulos_agregados = 0
    
    while True:
        titulo = input("Ingrese el título del libro (o 'fin' para terminar): ").strip()
        
        if titulo.lower() == 'fin':
            break
        
        if titulo == "":
            print(" El título no puede estar vacío")
            continue
        
        if existe_ejemplar(titulo):
            print(f" El título '{titulo}' ya existe en el catálogo")
            continue
        
        cantidad = input(f"Ingrese la cantidad de ejemplares para '{titulo}': ").strip()
        
        if validar_numero(cantidad):
            cantidad = int(cantidad)
            ejemplares.append({"TITULO": titulo, "cantidad": cantidad})
            titulos_agregados += 1
            print(f"Título agregado correctamente\n")
        else:
            print("No se agregó el título por cantidad inválida\n")
    
    if titulos_agregados > 0:
        guardar_ejemplares(ejemplares)
        print(f"\n{'='*50}")
        print(f"Se agregaron {titulos_agregados} título(s) al catálogo")
        print(f"{'='*40}\n")
    else:
        print("\nNo se agregaron títulos al catálogo\n")

def consultar_disponibilidad():
    print("==== CONSULTAR DISPONIBILIDAD ====")
    
    ejemplares = obtener_ejemplares()
    
    if not ejemplares:
        print("No hay ejemplares registrados en el catálogo.\n")
        return
    
    titulo_buscar = input("Ingrese el título a consultar: ").strip()
    
    if titulo_buscar == "":
        print("El título no puede estar vacío\n")
        return
    
    encontrado = False
    
    for ejemplar in ejemplares:
        if ejemplar["TITULO"].lower() == titulo_buscar.lower():
            encontrado = True
            print(f"Título: {ejemplar['TITULO']}")
            print(f"Disponibles: {ejemplar['cantidad']}")
            
            if ejemplar['cantidad'] == 0:
                print("Estado:  AGOTADO")
            else:
                print("Estado:  DISPONIBLE")
            break
    
    if not encontrado:
        print(f"\n El título '{titulo_buscar}' no se encuentra en el catálogo\n")

def listar_agotados():
    print("==== LISTAR AGOTADOS ====")
    
    ejemplares = obtener_ejemplares()
    
    if not ejemplares:
        print("No hay ejemplares registrados en el catálogo.\n")
        return
    
    agotados = []
    
    for ejemplar in ejemplares:
        if ejemplar["cantidad"] == 0:
            agotados.append(ejemplar)
    
    if not agotados:
        print(" No hay títulos agotados en el catálogo.")
        return
    
    
    
    for ejemplar in agotados:
        print(f"{ejemplar['TITULO']}")

def incorporar_titulo():
    print("==== INCORPORAR TÍTULO ====")
    
    titulo = input("Ingrese el título del libro: ").strip()
    
    if titulo == "":
        print("El título no puede estar vacío\n")
        return
    
    if existe_ejemplar(titulo):
        print(f"El título '{titulo}' ya existe en el catálogo\n")
        return
    
    cantidad = input(f"Ingrese la cantidad inicial de ejemplares: ").strip()
    
    if validar_numero(cantidad):
        cantidad = int(cantidad)
        
        ejemplares = obtener_ejemplares()
        ejemplares.append({"TITULO": titulo, "cantidad": cantidad})
        guardar_ejemplares(ejemplares)
        
        print(f"El título '{titulo}' ha sido incorporado al catalogo")
        
        
    else:
        print("No se pudo incorporar el título por cantidad inválida\n")
    
def prestamos_devoluciones():
    print("==== PRÉSTAMOS Y DEVOLUCIONES ====")
    
    ejemplares = obtener_ejemplares()
    
    if not ejemplares:
        print("No hay ejemplares registrados en el catálogo.\n")
        return
    
    titulo = input("Ingrese el título del libro: ").strip()
    
    if titulo == "":
        print("El título no puede estar vacío\n")
        return
    
    encontrado = False
    posicion = -1
    
    for i in range(len(ejemplares)):
        if ejemplares[i]["TITULO"].lower() == titulo.lower():
            encontrado = True
            posicion = i
            break
    
    if not encontrado:
        print(f"El título '{titulo}' no se encuentra en el catálogo\n")
        return
    
    print(f"\nTítulo: {ejemplares[posicion]['TITULO']}")
    print(f"Cantidad actual: {ejemplares[posicion]['cantidad']}")
    print("\n1. Préstamo (restar)")
    print("2. Devolución (sumar)")
    
    operacion = input("\nSeleccione operación: ").strip()
    
    if operacion == "1":
        if ejemplares[posicion]['cantidad'] > 0:
            ejemplares[posicion]['cantidad'] = ejemplares[posicion]['cantidad'] - 1
            guardar_ejemplares(ejemplares)
            print(f"\n✓ Préstamo registrado exitosamente")
            print(f"  Nueva cantidad: {ejemplares[posicion]['cantidad']} ejemplares\n")
        else:
            print(f"\n No se puede realizar el préstamo. No hay ejemplares disponibles.\n")
    
    elif operacion == "2":
        ejemplares[posicion]['cantidad'] = ejemplares[posicion]['cantidad'] + 1
        guardar_ejemplares(ejemplares)
        print(f"\n Devolución registrada exitosamente")
        print(f"  Nueva cantidad: {ejemplares[posicion]['cantidad']} ejemplares\n")
    
    else:
        print("\n Operación inválida. No se realizó ningún cambio.\n")
    

def mostrar_menu ():
    while True:
        print("*"*40)
        print("1. Mostrar catálogo")
        print("2. Ingresar ejemplares")
        print("3. Ingresar títulos")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título")
        print("7. Actualizar ejemplares (prestamos/devoluciones)")
        print("8. Salir")
        print("*"*40)
        opcion = input("Ingrese opción: ").strip()

        match opcion:
            case "1":
                mostrar_ejemplares()
            case "2":
                agregar_ejemplares()
            case "3":
                ingresar_titulos()
            case "4":
                consultar_disponibilidad()
            case "5":
                listar_agotados()
            case"6":
                incorporar_titulo()
            case "7":
                prestamos_devoluciones()
            case "8":
                print("Gracias por utilizar nuestra aplicación :) ")
                break
            case _:
                print("La opción ingresada es inválida ")
mostrar_menu()



