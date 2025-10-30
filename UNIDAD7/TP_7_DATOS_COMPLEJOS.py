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

inventario_ferreteria = {       #inventario
    "martillo":8,
    "pinza": 4,
    "francesa": 3,
    "llave": 6,
    "tenaza": 1}



while True:         #opciones
    print("\n1. Consultar stock")
    print("2. Agregar/Modificar producto")
    print("3. Salir")
    
    opcion = input("Elegí una opción: ")
    
    if opcion == "1":           #ver si existe el producto
        producto = input("Ingresá el producto: ")
        if producto in inventario_ferreteria:
            print(f"Stock de {producto}: {inventario_ferreteria[producto]}")
        else:
            print("Producto no encontrado")
    
    elif opcion == "2":         #agregar unidades
        producto = input("Ingresá el producto: ")
        cantidad = int(input("Ingresá la cantidad: "))
        
        if producto in inventario_ferreteria:
            inventario_ferreteria[producto] += cantidad
            print(f"Stock actualizado. Nuevo stock: {inventario_ferreteria[producto]}")
        else:
            inventario_ferreteria[producto] = cantidad
            print(f"Producto agregado con stock: {cantidad}")
    
    elif opcion == "3":             
        break

##################################################################################################################

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

# Agenda con tuplas (día, hora) como claves
#agenda = (lunes)





 