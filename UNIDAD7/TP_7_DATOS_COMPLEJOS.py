# # Dado el diccionario precios_frutas 
# #precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# #Añadir las siguientes frutas con sus respectivos precios: 
# #● Naranja = 1200 
# #● Manzana = 1500 
# #● Pera = 2300 

# precios_frutas = {"Banana": "1200", "Anana": "2500", "Melon": "3000", "Uva": "1450"}
# #Añadir
# precios_frutas["Naranja"] = "1200"
# precios_frutas["Manzana"] = "1500"
# precios_frutas["Pera"] = "2300"

################################################################################################################

# # Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# #desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# #● Banana = 1330 
# #● Manzana = 1700 
# #● Melón = 2800

# #Actualizar precios
# precios_frutas["Banana"] = '1330'
# precios_frutas["Manzana"] = '1700'
# precios_frutas["Melon"] = '2800'
# print (precios_frutas)

##########################################################################################################

# #3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# #desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# #precios.

# lista_frutas = list(precios_frutas.keys())
# print (lista_frutas)

###########################################################################################################

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

# agenda_telefonos = {}
# for i in range (3):
#     agenda_telefonos[input ("Ingrese el nombre de contacto ")] = input ("Ingrese el número del contacto ")

# print(agenda_telefonos[input("Consultar: ")])

#print (agenda_telefonos)

########################################################################################################

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.

# palabras_set = ()
# cantidad_diccionario = {}

# frase = (input("Ingrese una frase "))
# palabras = frase.split()
# palabras_set = set(frase.split())

# for palabra in palabras:
#     if palabra in cantidad_diccionario:
#         cantidad_diccionario[palabra] += 1
#     else:
#         cantidad_diccionario[palabra] = 1

# print (frase)
# print (palabras_set)
# print (cantidad_diccionario)

###############################################################################################################

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

# alumnos = {}   #diccionario

# for i in range(3):
#     nombre = input(f"Ingrese el nombre del alumno {i + 1} ")  #nombre de alumnos

#     nota_1 = float(input(f"Ingrese la primera nota de {nombre}: "))     #notas de alumnos
#     nota_2 = float(input(f"Ingrese la segunda nota de {nombre}: "))
#     nota_3 = float(input(f"Ingrese la tercera nota de {nombre}: "))

#     notas = (nota_1, nota_2, nota_3) #tupla
#     alumnos[nombre] = notas

# print("\n=== PROMEDIOS ===")        #promedios
# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{nombre}: {promedio:.2f}")

# print (alumnos)

#########################################################################################################

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# orden_de_alumnos_aprobados_parcial1 = {2,3,4,7,8,9}
# orden_de_alumnos_aprobados_parcial2 = {1,2,4,7,9,10,11}
# ambos_parciales = orden_de_alumnos_aprobados_parcial1 & orden_de_alumnos_aprobados_parcial2
# un_solo_parcial = orden_de_alumnos_aprobados_parcial2 ^ orden_de_alumnos_aprobados_parcial1
# al_menso_uno = orden_de_alumnos_aprobados_parcial1 | orden_de_alumnos_aprobados_parcial2
# print (f"Los alumnos que aprobaron ambos parciales son: {ambos_parciales} ")
# print (f"Los alumnos que aprobaron un solo parcial son: {un_solo_parcial} ")
# print (f"Los alumnos que aprobaron al menos un parcial son: {al_menso_uno}")

############################################################################################################

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

inventario_ferreteria = {"martillo":"8", "pinza": "4", "francesa": "3", "llave": "6", "tenaza": "1"}

##################################################################################################################

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

# Agenda con tuplas (día, hora) como claves
agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Lunes", "14:00"): "Presentación proyecto",
    ("Martes", "10:00"): "Clase de Python",
    ("Martes", "16:00"): "Dentista",
    ("Miércoles", "11:00"): "Almuerzo con cliente",
    ("Jueves", "09:00"): "Revisión de código",
    ("Jueves", "15:00"): "Gimnasio",
    ("Viernes", "10:00"): "Videoconferencia",
    ("Viernes", "18:00"): "Cena con amigos"
}

def mostrar_menu():
    print("\n" + "="*50)
    print("           AGENDA DE EVENTOS")
    print("="*50)
    print("1. Consultar evento en día y hora específicos")
    print("2. Ver todos los eventos de un día")
    print("3. Agregar nuevo evento")
    print("4. Eliminar evento")
    print("5. Mostrar agenda completa")
    print("6. Salir")
    print("="*50)

def consultar_evento():
    dia = input("\nIngrese el día (ej: Lunes, Martes, etc.): ").strip().capitalize()
    hora = input("Ingrese la hora (formato HH:MM, ej: 09:00): ").strip()
    
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"\n✓ {dia} a las {hora}: {agenda[clave]}")
    else:
        print(f"\n✗ No hay eventos programados para {dia} a las {hora}")

def ver_eventos_dia():
    dia = input("\nIngrese el día a consultar: ").strip().capitalize()
    
    eventos_del_dia = [(hora, evento) for (d, hora), evento in agenda.items() if d == dia]
    
    if eventos_del_dia:
        print(f"\n{'='*50}")
        print(f"   EVENTOS DEL {dia.upper()}")
        print(f"{'='*50}")
        eventos_del_dia.sort()  # Ordena por hora
        for hora, evento in eventos_del_dia:
            print(f"{hora} - {evento}")
        print(f"{'='*50}")
    else:
        print(f"\n✗ No hay eventos programados para {dia}")

def agregar_evento():
    dia = input("\nIngrese el día: ").strip().capitalize()
    hora = input("Ingrese la hora (formato HH:MM): ").strip()
    
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"\n✗ Ya existe un evento en {dia} a las {hora}: {agenda[clave]}")
        respuesta = input("¿Desea reemplazarlo? (s/n): ").strip().lower()
        if respuesta == 's':
            evento = input("Ingrese el nuevo evento: ").strip()
            agenda[clave] = evento
            print(f"✓ Evento actualizado para {dia} a las {hora}")
        else:
            print("Operación cancelada")
    else:
        evento = input("Ingrese el evento: ").strip()
        agenda[clave] = evento
        print(f"✓ Evento agregado: {dia} a las {hora} - {evento}")

def eliminar_evento():
    dia = input("\nIngrese el día: ").strip().capitalize()
    hora = input("Ingrese la hora (formato HH:MM): ").strip()
    
    clave = (dia, hora)
    
    if clave in agenda:
        evento = agenda[clave]
        print(f"\nEvento a eliminar: {dia} a las {hora} - {evento}")
        confirmacion = input("¿Confirma la eliminación? (s/n): ").strip().lower()
        if confirmacion == 's':
            del agenda[clave]
            print("✓ Evento eliminado exitosamente")
        else:
            print("Operación cancelada")
    else:
        print(f"\n✗ No hay eventos programados para {dia} a las {hora}")

def mostrar_agenda_completa():
    if not agenda:
        print("\n✗ La agenda está vacía")
        return
    
    print(f"\n{'='*50}")
    print("          AGENDA COMPLETA")
    print(f"{'='*50}")
    
    # Ordenar por día y hora
    dias_orden = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    eventos_ordenados = sorted(agenda.items(), 
                               key=lambda x: (dias_orden.index(x[0][0]) if x[0][0] in dias_orden else 999, x[0][1]))
    
    dia_actual = None
    for (dia, hora), evento in eventos_ordenados:
        if dia != dia_actual:
            if dia_actual is not None:
                print()
            print(f"{dia}:")
            dia_actual = dia
        print(f"  {hora} - {evento}")
    print(f"{'='*50}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-6): ").strip()
    
    if opcion == "1":
        consultar_evento()
    elif opcion == "2":
        ver_eventos_dia()
    elif opcion == "3":
        agregar_evento()
    elif opcion == "4":
        eliminar_evento()
    elif opcion == "5":
        mostrar_agenda_completa()
    elif opcion == "6":
        print("\n¡Hasta luego!")
        break
    else:
        print("\n✗ Opción inválida. Por favor seleccione una opción del 1 al 6")
    
    input("\nPresione Enter para continuar...")




 