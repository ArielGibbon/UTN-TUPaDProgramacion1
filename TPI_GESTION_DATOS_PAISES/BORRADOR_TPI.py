import csv
import os


def cargar_paises_desde_csv(nombre_archivo):
    
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
    print(f"=== RESUMEN DE CARGA ===")
    print(f" Países cargados correctamente: {contador_exitosos}")
    if contador_errores > 0:
        print(f" Líneas con errores (ignoradas): {contador_errores}")
    
    return paises


def abrir_archivo(nombre_archivo):
    
    resultado = None
    
    if os.path.exists(nombre_archivo):
        resultado = open(nombre_archivo, 'r', encoding='utf-8')
    
    return resultado


def validar_encabezado(encabezado):
    
    encabezado_esperado = "PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE"
    
    encabezado_normalizado = encabezado.strip().upper()
    
    return encabezado_normalizado == encabezado_esperado


def procesar_linea(linea, numero_linea):
    
    partes = linea.split(',')
    
    if len(partes) != 4:
        print(f"⚠ Línea {numero_linea}: Formato incorrecto. Se esperan 4 campos, se encontraron {len(partes)}.")
        return None
    
    nombre = partes[0].strip()
    poblacion_str = partes[1].strip()
    superficie_str = partes[2].strip()
    continente = partes[3].strip()
    
    if nombre == "":
        print(f"Línea {numero_linea}: El nombre del país está vacío.")
        return None
    
    if poblacion_str == "":
        print(f"Línea {numero_linea}: La población está vacía.")
        return None
    
    if superficie_str == "":
        print(f" Línea {numero_linea}: La superficie está vacía.")
        return None
    
    if continente == "":
        print(f" Línea {numero_linea}: El continente está vacío.")
        return None
    
    poblacion = convertir_a_entero(poblacion_str)
    if poblacion == None or poblacion <= 0:
        print(f" Línea {numero_linea}: La población '{poblacion_str}' no es un número entero positivo válido.")
        return None
    
    superficie = convertir_a_entero(superficie_str)
    if superficie == None or superficie <= 0:
        print(f" Línea {numero_linea}: La superficie '{superficie_str}' no es un número entero positivo válido.")
        return None
    
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    return pais


def convertir_a_entero(texto):
    
    if not texto.isdigit():
        return None
    
    return int(texto)


def guardar_paises_en_csv(paises, nombre_archivo):
    
    archivo = open(nombre_archivo, 'w', encoding='utf-8')
    
    archivo.write("PAIS,POBLACION,SUPERFICIE EN KILOMETROS CUADRADOS,CONTINENTE\n")
    
    for pais in paises:
        linea = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n"
        archivo.write(linea)
    
    archivo.close()
    return True
###################################################################################################################

def agregar_pais(paises, nombre_archivo):   #Agregar paises
   
    print("=== AGREGAR NUEVO PAÍS ===")
    
    nombre = input("Ingrese el nombre del país: ").strip()
    
    if nombre == "": #ver que no este vacio
        print(" Error: El nombre no puede estar vacío.")
        return False
    
    if verificar_pais_existe(paises, nombre): #ver que no este repetido
        print(f" Error: El país '{nombre}' ya existe en el sistema.")
        return False
    
    continente = input("Ingrese el continente: ").strip()
    
    if continente == "": #ver que tenga un continente, que no este vacio
        print(" Error: El continente no puede estar vacío.")
        return False
    
    poblacion_str = input("Ingrese la población: ").strip()
    
    if poblacion_str == "": #validar la poblacion ingresada
        print(" Error: La población no puede estar vacía.")
        return False
    
    poblacion = convertir_a_entero(poblacion_str)
    if poblacion == None:
        print(f" Error: La población '{poblacion_str}' debe ser un número entero.")
        return False
    
    if poblacion <= 0:
        print("Error: La población debe ser un número positivo.")
        return False
    
    superficie_str = input("Ingrese la superficie en km²: ").strip() #validar la ponblacion ingresada
    
    if superficie_str == "":
        print(" Error: La superficie no puede estar vacía.")
        return False
    
    superficie = convertir_a_entero(superficie_str)
    if superficie == None:
        print(f" Error: La superficie '{superficie_str}' debe ser un número entero.")
        return False
    
    if superficie <= 0:
        print(" Error: La superficie debe ser un número positivo.")
        return False
    
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(nuevo_pais)
    
    guardar_paises_en_csv(paises, nombre_archivo)
    
    print(f" País '{nombre}' agregado exitosamente.")
    print(f"  - Continente: {continente}")
    print(f"  - Población: {poblacion:,}")
    print(f"  - Superficie: {superficie:,} km²")
    
    return True


def verificar_pais_existe(paises, nombre):
    
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

################################################################################################################

def actualizar_datos_poblacion_superficie(paises, nombre_archivo):
    
    print("=== ACTUALIZAR DATOS DE PAÍS ===")
    
    # Solicitar nombre del país
    nombre_buscar = input("Ingrese el nombre del país a actualizar: ").strip()
    
    if nombre_buscar == "":
        print(" Error: Debe ingresar un nombre.")
        return False
    
    # Buscar coincidencia exacta o parcial
    paises_encontrados = buscar_pais_por_nombre(paises, nombre_buscar)
    
    # Si no se encuentra, mostrar error
    if len(paises_encontrados) == 0:
        print(f" No se encontró ningún país con el nombre '{nombre_buscar}'.")
        return False
    
    # Si hay múltiples coincidencias, mostrar opciones
    pais_seleccionado = None
    
    if len(paises_encontrados) == 1:
        pais_seleccionado = paises_encontrados[0]
        print(f" País encontrado: {pais_seleccionado['nombre']}")
    else:
        print(f" Se encontraron {len(paises_encontrados)} países:")
        i = 0
        while i < len(paises_encontrados):
            print(f"{i + 1}. {paises_encontrados[i]['nombre']}")
            i = i + 1
        
        opcion_str = input("\nSeleccione el número del país a actualizar: ").strip()
        
        if not opcion_str.isdigit():
            print(" Error: Debe ingresar un número válido.")
            return False
        
        opcion = int(opcion_str)
        
        if opcion < 1 or opcion > len(paises_encontrados):
            print(" Error: Opción inválida.")
            return False
        
        pais_seleccionado = paises_encontrados[opcion - 1]
    
    # Mostrar datos actuales
    print(f" Datos actuales de {pais_seleccionado['nombre']}:")
    print(f"  - Población: {pais_seleccionado['poblacion']:,}")
    print(f"  - Superficie: {pais_seleccionado['superficie']:,} km²")
    print(f"  - Continente: {pais_seleccionado['continente']}")
    
    # Solicitar nuevos valores
    print("\n(Presione Enter para mantener el valor actual)")
    
    # Actualizar población
    nueva_poblacion_str = input(f"Nueva población [{pais_seleccionado['poblacion']:,}]: ").strip()
    
    nueva_poblacion = None
    
    if nueva_poblacion_str != "":
        # Validar que sea numérico
        nueva_poblacion = convertir_a_entero(nueva_poblacion_str)
        
        if nueva_poblacion == None:
            print(f" Error: La población '{nueva_poblacion_str}' debe ser un número entero.")
            return False
        
        if nueva_poblacion <= 0:
            print(" Error: La población debe ser un número positivo.")
            return False
    
    # Actualizar superficie
    nueva_superficie_str = input(f"Nueva superficie en km² [{pais_seleccionado['superficie']:,}]: ").strip()
    
    nueva_superficie = None
    
    if nueva_superficie_str != "":
        # Validar que sea numérico
        nueva_superficie = convertir_a_entero(nueva_superficie_str)
        
        if nueva_superficie == None:
            print(f" Error: La superficie '{nueva_superficie_str}' debe ser un número entero.")
            return False
        
        if nueva_superficie <= 0:
            print(" Error: La superficie debe ser un número positivo.")
            return False
    
    # Verificar si hubo cambios
    if nueva_poblacion == None and nueva_superficie == None:
        print(" No se realizaron cambios.")
        return False
    
    # Actualizar en el diccionario
    if nueva_poblacion != None:
        pais_seleccionado["poblacion"] = nueva_poblacion
    
    if nueva_superficie != None:
        pais_seleccionado["superficie"] = nueva_superficie
    
    # Guardar en CSV
    guardar_paises_en_csv(paises, nombre_archivo)
    
    # Confirmar actualización
    print(f" País '{pais_seleccionado['nombre']}' actualizado exitosamente.")
    print(f" Datos actualizados:")
    print(f"  - Población: {pais_seleccionado['poblacion']:,}")
    print(f"  - Superficie: {pais_seleccionado['superficie']:,} km²")
    print(f"  - Continente: {pais_seleccionado['continente']}")
    
    return True


def buscar_pais_por_nombre(paises, nombre_buscar):
    
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

###############################################################################################################

def buscar_pais_nombre(paises):
    
    print("=== BUSCAR PAÍS POR NOMBRE ===")
    
    # Solicitar texto a buscar
    texto_buscar = input("Ingrese el nombre o parte del nombre del país: ").strip()
    
    if texto_buscar == "":
        print(" Error: Debe ingresar un texto para buscar.")
        return False
    
    # Recorrer lista y aplicar coincidencia parcial
    resultados = []
    texto_buscar_lower = texto_buscar.lower()
    
    i = 0
    while i < len(paises):
        nombre_pais_lower = paises[i]["nombre"].lower()
        
        # Verificar coincidencia parcial
        if texto_buscar_lower in nombre_pais_lower:
            resultados.append(paises[i])
        
        i = i + 1
    
    # Mostrar resultados o mensaje de "no encontrado"
    if len(resultados) == 0:
        print(f" No se encontraron países que coincidan con '{texto_buscar}'.")
        return False
    
    # Mostrar resultados
    print(f" Se encontraron {len(resultados)} país(es):\n")
    
    j = 0
    while j < len(resultados):
        pais = resultados[j]
        print("=" * 50)
        print(f"País: {pais['nombre']}")
        print(f"Continente: {pais['continente']}")
        print(f"Población: {pais['poblacion']:,} habitantes")
        print(f"Superficie: {pais['superficie']:,} km²")
        
        # Calcular densidad poblacional
        densidad = calcular_densidad_poblacional(pais['poblacion'], pais['superficie'])
        print(f"Densidad poblacional: {densidad:.2f} hab/km²")
        print("=" * 50)
        
        j = j + 1
    
    return True


def calcular_densidad_poblacional(poblacion, superficie):
    
    if superficie == 0:
        return 0
    
    densidad = poblacion / superficie
    return densidad

####################################################################################################################

def filtrar_paises_por_rango(paises):
   
    print("\n=== FILTRAR PAÍSES ===")
    
    # Submenú
    print("Seleccione el tipo de filtro:")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    print("4. Volver al menú principal")
    
    opcion = input("Ingrese opción: ").strip()
    
    match opcion:
        case "1":
            filtrar_por_continente(paises)
        case "2":
            filtrar_por_rango_poblacion(paises)
        case "3":
            filtrar_por_rango_superficie(paises)
        case "4":
            return True
        case _:
            print("Opción inválida.")
            return False
    
    return True


def filtrar_por_continente(paises):
   
    print("=== FILTRAR POR CONTINENTE ===")
    
    # Validar filtros ingresados
    continente = input("Ingrese el continente a buscar: ").strip()
    
    if continente == "":
        print("Error: Debe ingresar un continente.")
        return
    
    # Recorrer la lista aplicando condiciones
    resultados = []
    continente_lower = continente.lower()
    
    i = 0
    while i < len(paises):
        continente_pais_lower = paises[i]["continente"].lower()
        
        # Coincidencia parcial
        if continente_lower in continente_pais_lower:
            resultados.append(paises[i])
        
        i = i + 1
    
    # Mostrar lista filtrada o mensaje de error
    mostrar_resultados_filtro(resultados, f"continente '{continente}'")


def filtrar_por_rango_poblacion(paises):
    
    print("=== FILTRAR POR RANGO DE POBLACIÓN ===")
    
    # Validar filtros ingresados
    poblacion_min_str = input("Ingrese población mínima: ").strip()
    
    if poblacion_min_str == "":
        print("Error: Debe ingresar la población mínima.")
        return
    
    poblacion_min = convertir_a_entero(poblacion_min_str)
    
    if poblacion_min == None or poblacion_min < 0:
        print(f"Error: '{poblacion_min_str}' no es un número válido.")
        return
    
    poblacion_max_str = input("Ingrese población máxima: ").strip()
    
    if poblacion_max_str == "":
        print("Error: Debe ingresar la población máxima.")
        return
    
    poblacion_max = convertir_a_entero(poblacion_max_str)
    
    if poblacion_max == None or poblacion_max < 0:
        print(f"Error: '{poblacion_max_str}' no es un número válido.")
        return
    
    if poblacion_min > poblacion_max:
        print("Error: La población mínima no puede ser mayor que la máxima.")
        return
    
    # Recorrer la lista aplicando condiciones
    resultados = []
    
    i = 0
    while i < len(paises):
        poblacion = paises[i]["poblacion"]
        
        if poblacion >= poblacion_min and poblacion <= poblacion_max:
            resultados.append(paises[i])
        
        i = i + 1
    
    # Mostrar lista filtrada o mensaje de error
    mensaje = f"población entre {poblacion_min:,} y {poblacion_max:,}"
    mostrar_resultados_filtro(resultados, mensaje)


def filtrar_por_rango_superficie(paises):
    
    print("=== FILTRAR POR RANGO DE SUPERFICIE ===")
    
    # Validar filtros ingresados
    superficie_min_str = input("Ingrese superficie mínima (km²): ").strip()
    
    if superficie_min_str == "":
        print(" Error: Debe ingresar la superficie mínima.")
        return
    
    superficie_min = convertir_a_entero(superficie_min_str)
    
    if superficie_min == None or superficie_min < 0:
        print(f" Error: '{superficie_min_str}' no es un número válido.")
        return
    
    superficie_max_str = input("Ingrese superficie máxima (km²): ").strip()
    
    if superficie_max_str == "":
        print(" Error: Debe ingresar la superficie máxima.")
        return
    
    superficie_max = convertir_a_entero(superficie_max_str)
    
    if superficie_max == None or superficie_max < 0:
        print(f" Error: '{superficie_max_str}' no es un número válido.")
        return
    
    if superficie_min > superficie_max:
        print(" Error: La superficie mínima no puede ser mayor que la máxima.")
        return
    
    # Recorrer la lista aplicando condiciones
    resultados = []
    
    i = 0
    while i < len(paises):
        superficie = paises[i]["superficie"]
        
        if superficie >= superficie_min and superficie <= superficie_max:
            resultados.append(paises[i])
        
        i = i + 1
    
    # Mostrar lista filtrada o mensaje de error
    mensaje = f"superficie entre {superficie_min:,} y {superficie_max:,} km²"
    mostrar_resultados_filtro(resultados, mensaje)


def mostrar_resultados_filtro(resultados, criterio):
    
    if len(resultados) == 0:
        print(f" No se encontraron países con {criterio}.")
        return
    
    print(f" Se encontraron {len(resultados)} país(es) con {criterio}:\n")
    
    i = 0
    while i < len(resultados):
        pais = resultados[i]
        print("=" * 40)
        print(f"País: {pais['nombre']}")
        print(f"Continente: {pais['continente']}")
        print(f"Población: {pais['poblacion']:,} habitantes")
        print(f"Superficie: {pais['superficie']:,} km²")
        print("=" * 40)
        
        i = i + 1

###############################################################################################################

def paises_ordenados_por_rango(paises):
   
    print("=== ORDENAR PAÍSES ===")
    
    # Submenú
    print(" Seleccione el criterio de ordenamiento:")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    print("4. Volver al menú principal")
    
    opcion = input("Ingrese opción: ").strip()
    
    match opcion:
        case "1":
            ordenar_por_nombre(paises)
        case "2":
            ordenar_por_poblacion(paises)
        case "3":
            ordenar_por_superficie(paises)
        case "4":
            return True
        case _:
            print("Opción inválida.")
            return False
    
    return True


def ordenar_por_nombre(paises):
    print("=== ORDENAR POR NOMBRE ===")
    
    if len(paises) == 0:
        print("No hay países para ordenar.")
        return
    
    # Ordenar usando burbuja
    paises_ordenados = ordenar_por_campo_texto(paises, "nombre")
    
    # Mostrar resultado
    mostrar_paises_ordenados(paises_ordenados, "nombre (A-Z)")


def ordenar_por_poblacion(paises):
    
    print("=== ORDENAR POR POBLACIÓN ===")
    
    if len(paises) == 0:
        print("No hay países para ordenar.")
        return
    
    # Solicitar orden ascendente/descendente
    print(" Seleccione el orden:")
    print("1. Ascendente (menor a mayor)")
    print("2. Descendente (mayor a menor)")
    
    orden = input("\nIngrese opción: ").strip()
    
    if orden != "1" and orden != "2":
        print("Opción inválida.")
        return
    
    ascendente = True
    descripcion = "población (menor a mayor)"
    
    if orden == "2":
        ascendente = False
        descripcion = "población (mayor a menor)"
    
    # Ordenar
    paises_ordenados = ordenar_por_campo_numerico(paises, "poblacion", ascendente)
    
    # Mostrar resultado
    mostrar_paises_ordenados(paises_ordenados, descripcion)


def ordenar_por_superficie(paises):
    
    print("=== ORDENAR POR SUPERFICIE ===")
    
    if len(paises) == 0:
        print("No hay países para ordenar.")
        return
    
    # Solicitar orden ascendente/descendente
    print(" Seleccione el orden:")
    print("1. Ascendente (menor a mayor)")
    print("2. Descendente (mayor a menor)")
    
    orden = input("\nIngrese opción: ").strip()
    
    if orden != "1" and orden != "2":
        print("Opción inválida.")
        return
    
    ascendente = True
    descripcion = "superficie (menor a mayor)"
    
    if orden == "2":
        ascendente = False
        descripcion = "superficie (mayor a menor)"
    
    # Ordenar
    paises_ordenados = ordenar_por_campo_numerico(paises, "superficie", ascendente)
    
    # Mostrar resultado
    mostrar_paises_ordenados(paises_ordenados, descripcion)


def ordenar_por_campo_texto(paises, campo):
    
    # Crear copia para no modificar la lista original
    paises_copia = []
    i = 0
    while i < len(paises):
        paises_copia.append(paises[i])
        i = i + 1
    
    # Burbuja
    n = len(paises_copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            valor1 = paises_copia[j][campo].lower()
            valor2 = paises_copia[j + 1][campo].lower()
            
            if valor1 > valor2:
                # Intercambiar
                temp = paises_copia[j]
                paises_copia[j] = paises_copia[j + 1]
                paises_copia[j + 1] = temp
            
            j = j + 1
        i = i + 1
    
    return paises_copia


def ordenar_por_campo_numerico(paises, campo, ascendente):
    
    # Crear copia para no modificar la lista original
    paises_copia = []
    i = 0
    while i < len(paises):
        paises_copia.append(paises[i])
        i = i + 1
    
    # burbuja
    n = len(paises_copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            valor1 = paises_copia[j][campo]
            valor2 = paises_copia[j + 1][campo]
            
            debe_intercambiar = False
            
            if ascendente:
                if valor1 > valor2:
                    debe_intercambiar = True
            else:
                if valor1 < valor2:
                    debe_intercambiar = True
            
            if debe_intercambiar:
                # Intercambiar
                temp = paises_copia[j]
                paises_copia[j] = paises_copia[j + 1]
                paises_copia[j + 1] = temp
            
            j = j + 1
        i = i + 1
    
    return paises_copia


def mostrar_paises_ordenados(paises, criterio):
    
    print(f" Países ordenados por {criterio}:")
    print(f"Total: {len(paises)} país(es)\n")
    
    i = 0
    while i < len(paises):
        pais = paises[i]
        print("=" * 50)
        print(f"{i + 1}. {pais['nombre']}")
        print(f"   Continente: {pais['continente']}")
        print(f"   Población: {pais['poblacion']:,} habitantes")
        print(f"   Superficie: {pais['superficie']:,} km²")
        print("=" * 50)
        
        i = i + 1

#################################################################################################################

def estadistica_paises_cargados(paises):
    
    print("=== ESTADÍSTICAS DE PAÍSES ===")
    
    if len(paises) == 0:
        print(" No hay países cargados para mostrar estadísticas.")
        return False
    
    print(f"Total de países: {len(paises)}")
    print("\n" + "=" * 40)
    
    # País con mayor población
    pais_mayor_poblacion = obtener_pais_mayor_poblacion(paises)
    print(f" País con MAYOR población:")
    print(f"   {pais_mayor_poblacion['nombre']}")
    print(f"   Población: {pais_mayor_poblacion['poblacion']:,} habitantes")
    
    # País con menor población
    pais_menor_poblacion = obtener_pais_menor_poblacion(paises)
    print(f"País con MENOR población:")
    print(f"   {pais_menor_poblacion['nombre']}")
    print(f"   Población: {pais_menor_poblacion['poblacion']:,} habitantes")
    
    # Promedio de población
    promedio_poblacion = calcular_promedio_poblacion(paises)
    print(f"Promedio de población:")
    print(f"   {promedio_poblacion:,.2f} habitantes")
    
    # Promedio de superficie
    promedio_superficie = calcular_promedio_superficie(paises)
    print(f"Promedio de superficie:")
    print(f"   {promedio_superficie:,.2f} km²")
    
    # Cantidad de países por continente
    print(f"Cantidad de países por continente:")
    paises_por_continente = contar_paises_por_continente(paises)
    mostrar_paises_por_continente(paises_por_continente)
    
    print("\n" + "=" * 40)
    
    return True


def obtener_pais_mayor_poblacion(paises):
    
    pais_mayor = paises[0]
    
    i = 1
    while i < len(paises):
        if paises[i]["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = paises[i]
        i = i + 1
    
    return pais_mayor


def obtener_pais_menor_poblacion(paises):
    
    pais_menor = paises[0]
    
    i = 1
    while i < len(paises):
        if paises[i]["poblacion"] < pais_menor["poblacion"]:
            pais_menor = paises[i]
        i = i + 1
    
    return pais_menor


def calcular_promedio_poblacion(paises):
   
    suma_poblacion = 0
    
    i = 0
    while i < len(paises):
        suma_poblacion = suma_poblacion + paises[i]["poblacion"]
        i = i + 1
    
    promedio = suma_poblacion / len(paises)
    
    return promedio


def calcular_promedio_superficie(paises):
   
    suma_superficie = 0
    
    i = 0
    while i < len(paises):
        suma_superficie = suma_superficie + paises[i]["superficie"]
        i = i + 1
    
    promedio = suma_superficie / len(paises)
    
    return promedio


def contar_paises_por_continente(paises):
   
    conteo = {}
    
    i = 0
    while i < len(paises):
        continente = paises[i]["continente"]
        
        # Si el continente ya existe, incrementar contador
        if continente in conteo:
            conteo[continente] = conteo[continente] + 1
        else:
            # Si no existe, inicializar en 1
            conteo[continente] = 1
        
        i = i + 1
    
    return conteo


def mostrar_paises_por_continente(paises_por_continente):
    
    # Obtener lista de continentes
    continentes = []
    for continente in paises_por_continente:
        continentes.append(continente)
    
    # Ordenar continentes alfabéticamente
    continentes_ordenados = ordenar_lista_texto(continentes)
    
    # Mostrar cada continente con su conteo
    i = 0
    while i < len(continentes_ordenados):
        continente = continentes_ordenados[i]
        cantidad = paises_por_continente[continente]
        print(f"   • {continente}: {cantidad} país(es)")
        i = i + 1


def ordenar_lista_texto(lista):
    
    # Crear copia
    lista_copia = []
    i = 0
    while i < len(lista):
        lista_copia.append(lista[i])
        i = i + 1
    
    # Burbuja
    n = len(lista_copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if lista_copia[j].lower() > lista_copia[j + 1].lower():
                # Intercambiar
                temp = lista_copia[j]
                lista_copia[j] = lista_copia[j + 1]
                lista_copia[j + 1] = temp
            j = j + 1
        i = i + 1
    
    return lista_copia

################################################################################################################

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
                buscar_pais_nombre(paises)
            case "4":
                filtrar_paises_por_rango(paises)
            case "5":
                paises_ordenados_por_rango(paises)
            case "6":
                estadistica_paises_cargados(paises)
            case "7":
                print("Gracias por utilizar nuestra aplicación :)")
                break
            case _:
                print("La opción ingresada es inválida")


mostrar_menu()


