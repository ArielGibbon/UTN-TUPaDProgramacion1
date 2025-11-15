import csv
import os


def cargar_paises_desde_csv(nombre_archivo):
    """
    Carga la lista de países desde un archivo CSV.
    Si el archivo no existe, retorna una lista vacía.
    
    Parámetros:
    - nombre_archivo: nombre del archivo CSV a cargar
    
    Retorna:
    - lista de diccionarios con los datos de países
    """
    paises = []
    
    # Intentar abrir el archivo
    archivo = abrir_archivo(nombre_archivo)
    
    if archivo == None:
        print(f"Aviso: No se encontró el archivo '{nombre_archivo}'. Se iniciará con lista vacía.")
        return paises
    
    # Leer todas las líneas
    lineas = archivo.readlines()
    archivo.close()
    
    # Verificar que el archivo no esté vacío
    if len(lineas) == 0:
        print("Aviso: El archivo está vacío. Se iniciará con lista vacía.")
        return paises
    
    # Validar encabezado
    encabezado = lineas[0].strip()
    if not validar_encabezado(encabezado):
        print("Error: El encabezado del CSV no tiene el formato correcto.")
        print("Formato esperado: PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE")
        return paises
    
    # Procesar cada línea de datos
    contador_exitosos = 0
    contador_errores = 0
    
    i = 1
    while i < len(lineas):
        linea = lineas[i].strip()
        
        # Ignorar líneas vacías
        if linea != "":
            pais = procesar_linea(linea, i + 1)
            
            if pais != None:
                paises.append(pais)
                contador_exitosos = contador_exitosos + 1
            else:
                contador_errores = contador_errores + 1
        
        i = i + 1
    
    # Mostrar resumen de carga
    print(f"\n=== RESUMEN DE CARGA ===")
    print(f"✓ Países cargados correctamente: {contador_exitosos}")
    if contador_errores > 0:
        print(f"⚠ Líneas con errores (ignoradas): {contador_errores}")
    
    return paises


def abrir_archivo(nombre_archivo):
    """
    Intenta abrir un archivo para lectura.
    
    Parámetros:
    - nombre_archivo: nombre del archivo a abrir
    
    Retorna:
    - objeto archivo si existe, None si no existe
    """
    resultado = None
    
    if os.path.exists(nombre_archivo):
        resultado = open(nombre_archivo, 'r', encoding='utf-8')
    
    return resultado


def validar_encabezado(encabezado):
    """
    Valida que el encabezado tenga el formato correcto.
    
    Parámetros:
    - encabezado: primera línea del CSV
    
    Retorna:
    - True si es válido, False si no
    """
    encabezado_esperado = "PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE"
    
    encabezado_normalizado = encabezado.strip().upper()
    
    return encabezado_normalizado == encabezado_esperado


def procesar_linea(linea, numero_linea):
    """
    Procesa una línea del CSV y crea un diccionario de país.
    Valida todos los campos.
    
    Parámetros:
    - linea: línea del CSV
    - numero_linea: número de línea para mensajes de error
    
    Retorna:
    - diccionario con datos del país o None si hay error
    """
    partes = linea.split(',')
    
    if len(partes) != 4:
        print(f"⚠ Línea {numero_linea}: Formato incorrecto. Se esperan 4 campos, se encontraron {len(partes)}.")
        return None
    
    nombre = partes[0].strip()
    poblacion_str = partes[1].strip()
    superficie_str = partes[2].strip()
    continente = partes[3].strip()
    
    if nombre == "":
        print(f"⚠ Línea {numero_linea}: El nombre del país está vacío.")
        return None
    
    if poblacion_str == "":
        print(f"⚠ Línea {numero_linea}: La población está vacía.")
        return None
    
    if superficie_str == "":
        print(f"⚠ Línea {numero_linea}: La superficie está vacía.")
        return None
    
    if continente == "":
        print(f"⚠ Línea {numero_linea}: El continente está vacío.")
        return None
    
    poblacion = convertir_a_entero(poblacion_str)
    if poblacion == None or poblacion <= 0:
        print(f"⚠ Línea {numero_linea}: La población '{poblacion_str}' no es un número entero positivo válido.")
        return None
    
    superficie = convertir_a_entero(superficie_str)
    if superficie == None or superficie <= 0:
        print(f"⚠ Línea {numero_linea}: La superficie '{superficie_str}' no es un número entero positivo válido.")
        return None
    
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    return pais


def convertir_a_entero(texto):
    """
    Convierte un texto a entero.
    
    Parámetros:
    - texto: cadena a convertir
    
    Retorna:
    - número entero si es válido, None si no se puede convertir
    """
    if not texto.isdigit():
        return None
    
    return int(texto)


def guardar_paises_en_csv(paises, nombre_archivo):
    """
    Guarda la lista de países en un archivo CSV.
    
    Parámetros:
    - paises: lista de diccionarios
    - nombre_archivo: nombre del archivo
    
    Retorna:
    - True si se guardó correctamente
    """
    archivo = open(nombre_archivo, 'w', encoding='utf-8')
    
    archivo.write("PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE\n")
    
    for pais in paises:
        linea = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n"
        archivo.write(linea)
    
    archivo.close()
    return True


def agregar_pais(paises, nombre_archivo):
    """
    Agrega un nuevo país a la lista.
    Solicita todos los datos, los valida y guarda en CSV.
    
    Parámetros:
    - paises: lista de diccionarios con los países
    - nombre_archivo: nombre del archivo CSV para guardar
    
    Retorna:
    - True si se agregó correctamente, False si hubo error
    """
    print("\n=== AGREGAR NUEVO PAÍS ===")
    
    nombre = input("Ingrese el nombre del país: ").strip()
    
    if nombre == "":
        print("❌ Error: El nombre no puede estar vacío.")
        return False
    
    if verificar_pais_existe(paises, nombre):
        print(f"❌ Error: El país '{nombre}' ya existe en el sistema.")
        return False
    
    continente = input("Ingrese el continente: ").strip()
    
    if continente == "":
        print("❌ Error: El continente no puede estar vacío.")
        return False
    
    poblacion_str = input("Ingrese la población: ").strip()
    
    if poblacion_str == "":
        print("❌ Error: La población no puede estar vacía.")
        return False
    
    poblacion = convertir_a_entero(poblacion_str)
    if poblacion == None:
        print(f"❌ Error: La población '{poblacion_str}' debe ser un número entero.")
        return False
    
    if poblacion <= 0:
        print("❌ Error: La población debe ser un número positivo.")
        return False
    
    superficie_str = input("Ingrese la superficie en km²: ").strip()
    
    if superficie_str == "":
        print("❌ Error: La superficie no puede estar vacía.")
        return False
    
    superficie = convertir_a_entero(superficie_str)
    if superficie == None:
        print(f"❌ Error: La superficie '{superficie_str}' debe ser un número entero.")
        return False
    
    if superficie <= 0:
        print("❌ Error: La superficie debe ser un número positivo.")
        return False
    
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(nuevo_pais)
    
    guardar_paises_en_csv(paises, nombre_archivo)
    
    print(f"✓ País '{nombre}' agregado exitosamente.")
    print(f"  - Continente: {continente}")
    print(f"  - Población: {poblacion:,}")
    print(f"  - Superficie: {superficie:,} km²")
    
    return True


def verificar_pais_existe(paises, nombre):
    """
    Verifica si un país ya existe en la lista.
    Comparación no sensible a mayúsculas/minúsculas.
    
    Parámetros:
    - paises: lista de diccionarios
    - nombre: nombre del país a verificar
    
    Retorna:
    - True si existe, False si no existe
    """
    if type(paises) != list:
        return False
    
    if len(paises) == 0:
        return False
    
    nombre_lower = nombre.lower()
    
    i = 0
    while i < len(paises):
        if type(paises[i]) == dict:
            if "nombre" in paises[i]:
                if paises[i]["nombre"].lower() == nombre_lower:
                    return True
        i = i + 1
    
    return False

def actualizar_datos_poblacion_superficie(paises, nombre_archivo):
    """
    Actualiza los datos de población y/o superficie de un país.
    
    Parámetros:
    - paises: lista de diccionarios con los países
    - nombre_archivo: nombre del archivo CSV para guardar
    
    Retorna:
    - True si se actualizó correctamente, False si hubo error
    """
    print("\n=== ACTUALIZAR DATOS DE PAÍS ===")
    
    # 4.1. Solicitar nombre del país
    nombre_buscar = input("Ingrese el nombre del país a actualizar: ").strip()
    
    if nombre_buscar == "":
        print("❌ Error: Debe ingresar un nombre.")
        return False
    
    # 4.2. Buscar coincidencia exacta o parcial
    paises_encontrados = buscar_pais_por_nombre(paises, nombre_buscar)
    
    # 4.3. Si no se encuentra, mostrar error
    if len(paises_encontrados) == 0:
        print(f"❌ No se encontró ningún país con el nombre '{nombre_buscar}'.")
        return False
    
    # Si hay múltiples coincidencias, mostrar opciones
    pais_seleccionado = None
    
    if len(paises_encontrados) == 1:
        pais_seleccionado = paises_encontrados[0]
        print(f"\n✓ País encontrado: {pais_seleccionado['nombre']}")
    else:
        print(f"\n✓ Se encontraron {len(paises_encontrados)} países:")
        i = 0
        while i < len(paises_encontrados):
            print(f"{i + 1}. {paises_encontrados[i]['nombre']}")
            i = i + 1
        
        opcion_str = input("\nSeleccione el número del país a actualizar: ").strip()
        
        if not opcion_str.isdigit():
            print("❌ Error: Debe ingresar un número válido.")
            return False
        
        opcion = int(opcion_str)
        
        if opcion < 1 or opcion > len(paises_encontrados):
            print("❌ Error: Opción inválida.")
            return False
        
        pais_seleccionado = paises_encontrados[opcion - 1]
    
    # Mostrar datos actuales
    print(f"\nDatos actuales de {pais_seleccionado['nombre']}:")
    print(f"  - Población: {pais_seleccionado['poblacion']:,}")
    print(f"  - Superficie: {pais_seleccionado['superficie']:,} km²")
    print(f"  - Continente: {pais_seleccionado['continente']}")
    
    # 4.4. Solicitar nuevos valores
    print("\n(Presione Enter para mantener el valor actual)")
    
    # Actualizar población
    nueva_poblacion_str = input(f"Nueva población [{pais_seleccionado['poblacion']:,}]: ").strip()
    
    nueva_poblacion = None
    
    if nueva_poblacion_str != "":
        # 4.5. Validar que sea numérico
        nueva_poblacion = convertir_a_entero(nueva_poblacion_str)
        
        if nueva_poblacion == None:
            print(f"❌ Error: La población '{nueva_poblacion_str}' debe ser un número entero.")
            return False
        
        if nueva_poblacion <= 0:
            print("❌ Error: La población debe ser un número positivo.")
            return False
    
    # Actualizar superficie
    nueva_superficie_str = input(f"Nueva superficie en km² [{pais_seleccionado['superficie']:,}]: ").strip()
    
    nueva_superficie = None
    
    if nueva_superficie_str != "":
        # 4.5. Validar que sea numérico
        nueva_superficie = convertir_a_entero(nueva_superficie_str)
        
        if nueva_superficie == None:
            print(f"❌ Error: La superficie '{nueva_superficie_str}' debe ser un número entero.")
            return False
        
        if nueva_superficie <= 0:
            print("❌ Error: La superficie debe ser un número positivo.")
            return False
    
    # Verificar si hubo cambios
    if nueva_poblacion == None and nueva_superficie == None:
        print("⚠ No se realizaron cambios.")
        return False
    
    # 4.6. Actualizar en el diccionario
    if nueva_poblacion != None:
        pais_seleccionado["poblacion"] = nueva_poblacion
    
    if nueva_superficie != None:
        pais_seleccionado["superficie"] = nueva_superficie
    
    # 4.7. Guardar en CSV
    guardar_paises_en_csv(paises, nombre_archivo)
    
    # 4.8. Confirmar actualización
    print(f"\n✓ País '{pais_seleccionado['nombre']}' actualizado exitosamente.")
    print(f"\nDatos actualizados:")
    print(f"  - Población: {pais_seleccionado['poblacion']:,}")
    print(f"  - Superficie: {pais_seleccionado['superficie']:,} km²")
    print(f"  - Continente: {pais_seleccionado['continente']}")
    
    return True


def buscar_pais_por_nombre(paises, nombre_buscar):
    """
    Busca países por coincidencia exacta o parcial del nombre.
    
    Parámetros:
    - paises: lista de diccionarios
    - nombre_buscar: nombre o parte del nombre a buscar
    
    Retorna:
    - lista de países que coinciden con la búsqueda
    """
    resultados = []
    nombre_buscar_lower = nombre_buscar.lower()
    
    i = 0
    while i < len(paises):
        nombre_pais_lower = paises[i]["nombre"].lower()
        
        # Buscar coincidencia exacta o parcial
        if nombre_buscar_lower in nombre_pais_lower:
            resultados.append(paises[i])
        
        i = i + 1
    
    return resultados



def mostrar_menu():
    # Cargar países al inicio
    paises = cargar_paises_desde_csv("paises.csv")
    
    while True:
        print("\n" + "*" * 40)
        print("1. Agregar un país")
        print("2. Actualizar datos de población y superficie")
        print("3. Buscar un país por nombre")
        print("4. Filtrar países por rango")
        print("5. Mostrar países ordenados por categoría")
        print("6. Mostrar estadísticas de países")
        print("7. Salir")
        print("*" * 40)
        opcion = input("Ingrese opción: ").strip()

        match opcion:
            case "1":
                agregar_pais(paises, "paises.csv")
            case "2":
                actualizar_datos_poblacion_superficie(paises, "paises.csv")
            case "3":
                print("Buscar un país por nombre")
            case "4":
                print("Filtrar países (seleccionar rango)")
            case "5":
                print("Mostrar lista de países ordenados por rango")
            case "6":
                print("Mostrar estadísticas por país")
            case "7":
                print("Gracias por utilizar nuestra aplicación :)")
                break
            case _:
                print("La opción ingresada es inválida")


mostrar_menu()


