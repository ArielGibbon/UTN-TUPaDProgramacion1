# nombre = input("Escribe tu nombre ")
# print (f"Hola {nombre}!")
# print (f"Tu nombre tiene {len (nombre)}  letras")

#definir funcion
# def obtener_resto (num1, num2):
#     return num1 - num2 * (num1 // num2)

# def es_multiplo (x, y):
#     return obtener_resto(x, y) == 0


# a = int(input("Ingrese el primer número "))
# b = int(input("Ingrese el segundo número "))

# resto = obtener_resto(a, b)

# print (f"El resto entre {a} y {b} , es {resto}.")
# if es_multiplo(a,b):
#     print (a, " es multiplo de ", b)
# else:
#     print(f"{a} no es multiplo de {b}")

# def obtener_resto (a, b):
#     return a % b

# def multiplo (x,y):
#     return obtener_resto(x,y)==0


# num1 = int(input("Ingrese el primer número "))
# num2 = int(input("Ingrese el segundo número "))
# resto = obtener_resto (num1, num2)
# print (f"El resto de dividir {num1} por {num2} es:  {resto} ")
# if multiplo(num1,num2):
#     print (f"El número {num1} es múltiplo de {num2}")

# def funcion_resto (num1 , num2):
#     return num1 - num2 * (num1 // num2)

# def es_multiplo (x,y):
#     return funcion_resto (x ,y) == 0


# a = int(input ("ingrese un número " ))
# b = int(input("Ingrese el otro " ))
# resto = funcion_resto(a,b)
# print (f"El resto de dividir {a} por {b} es: {resto}")
# if es_multiplo(a , b):
#     print (f"{a} es múltilo de {b}")
#########################################################################################################3


#LISTA CREACION 

# frutas = ["banana", "manzana", "pera", "naranja"]
# frutas.append("kiwi")
# print (frutas)

#DICCIONARIO CREACION

# mi_diccionario = {"nombre": "Syd", "Edad":"26 ", "profesion": "Ingeniero" }
# print (mi_diccionario["nombre"])
# print (mi_diccionario["profesion"])


#buscar elemento
# t = (1,2,3,4,5)
# if 2 in t:
#     print ("Está")
# else:
#     print("No está")

#desempaquetar

# t = (1,2,3,4,5)
# a,b,c,d,e  = t
# print (f"el {a}, el {b}, el {c}, y el {d} el {e}")

# #buscar elemento y armar nueva tupla
# t = (1,2,3,4,5)
# a, *t2 = t
# print (f"El valor de a es: {a} , y la tupla 2 es: {t2} " )

# t = (1, 2, 3, 2, 4, 4, 5, 6, 2, 2, 7)
# print (f"La totalidad de elementos de la tupla es: { len(t)}")
# print (f"La cantidad de números 2 que hay es: {t.count(2)}")
# print (f"El número 6 aparece en el índice {t.index(6)}")
# #print (f"El número 9 aparece en el indice {t.index(9)}")

#Crear conjunto (set)
#  #Creae un set desde una lista (omite los valores repetidos)

# lis = [1, 2, 3, 2, 3, 4, 5]
# c = set(lis)
# print (c)

#Operaciones 
# lis = [1, 2, 3, 2, 3, 4, 5]
# print (f"La cantidad de elementos en el set es: {len(lis)}")
# if 8 in lis:
#     print ("Está")
# else:
#     print("No está")

# c = set()
# c.add ("Vero")
# c.add("Syd")
# c.add("Mel")
# c.add("Ariel")
# c.add("Vero")
# for f in c:
#     print(f)

#Operaciones de conjuntos

# a = {1,2,3,4}
# b = {3,4,5,6}
# resul1 = a | b
# resul2 = a & b
# resul3 = a - b
# resul4 = a ^ b
# resul5 = a < b
# resul6 = a > b
# print (resul1)
# print (resul2)
# print (resul3)
# print (resul4)
# print (resul5)
# print (resul6)

# letras = ("A","B","C")
# letras [3] = "D"
# print (letras)
    
# quim = {"manz":"3", "banana":"2", "naranja": "6"}

# quim["pera"] = quim.get["pera": "8"]
# del quim["naranja"]

# print (quim)

# inventario = {
#     "Manzanas": 50,
#     "Naranjas": 30,
#     "Bananas": 45,
#     "Peras": 25
# }

# def mostrar_menu():
#     print("\n" + "="*40)
#     print("   SISTEMA DE GESTIÓN DE STOCK")
#     print("="*40)
#     print("1. Consultar stock de un producto")
#     print("2. Agregar unidades al stock")
#     print("3. Agregar nuevo producto")
#     print("4. Mostrar todo el inventario")
#     print("5. Salir")
#     print("="*40)

# def consultar_stock():
#     producto = input("\nIngrese el nombre del producto: ").strip()
    
#     if producto in inventario:
#         print(f"✓ Stock de '{producto}': {inventario[producto]} unidades")
#     else:
#         print(f"✗ El producto '{producto}' no existe en el inventario")

# def agregar_unidades():
#     producto = input("\nIngrese el nombre del producto: ").strip()
    
#     if producto in inventario:
#         try:
#             cantidad = int(input(f"Stock actual: {inventario[producto]} unidades\nIngrese cantidad a agregar: "))
#             if cantidad > 0:
#                 inventario[producto] += cantidad
#                 print(f"✓ Stock actualizado. Nuevo stock de '{producto}': {inventario[producto]} unidades")
#             else:
#                 print("✗ La cantidad debe ser mayor a 0")
#         except ValueError:
#             print("✗ Error: Debe ingresar un número entero")
#     else:
#         print(f"✗ El producto '{producto}' no existe en el inventario")
#         print("   Use la opción 3 para agregar un nuevo producto")

# def agregar_producto():
#     producto = input("\nIngrese el nombre del nuevo producto: ").strip()
    
#     if producto in inventario:
#         print(f"✗ El producto '{producto}' ya existe con stock: {inventario[producto]} unidades")
#         print("   Use la opción 2 para agregar unidades")
#     else:
#         try:
#             cantidad = int(input("Ingrese la cantidad inicial en stock: "))
#             if cantidad >= 0:
#                 inventario[producto] = cantidad
#                 print(f"✓ Producto '{producto}' agregado con {cantidad} unidades")
#             else:
#                 print("✗ La cantidad no puede ser negativa")
#         except ValueError:
#             print("✗ Error: Debe ingresar un número entero")

# def mostrar_inventario():
#     print("\n" + "="*40)
#     print("   INVENTARIO COMPLETO")
#     print("="*40)
#     if inventario:
#         for producto, stock in inventario.items():
#             print(f"{producto:.<30} {stock:>5} unidades")
#     else:
#         print("El inventario está vacío")
#     print("="*40)

# # Programa principal
# while True:
#     mostrar_menu()
#     opcion = input("\nSeleccione una opción (1-5): ").strip()
    
#     if opcion == "1":
#         consultar_stock()
#     elif opcion == "2":
#         agregar_unidades()
#     elif opcion == "3":
#         agregar_producto()
#     elif opcion == "4":
#         mostrar_inventario()
#     elif opcion == "5":
#         print("\n¡Gracias por usar el sistema de gestión de stock!")
#         break
#     else:
#         print("\n✗ Opción inválida. Por favor seleccione una opción del 1 al 5")
    
#     input("\nPresione Enter para continuar...")


# with open("registros.csv", "w") as archivo:
#     encabezado = archivo.writelines().strip()
#     print("Encabezado:", encabezado)
#     linea1 = archivo.readline().strip()
#     print("Primera línea:", linea1)
#     linea2 = archivo.readline().strip()
#     print("Segunda línea:", linea2)

print("1. Escribiendo archivo")
archivo_nuevo = open("productos.txt","w")
archivo_nuevo.write("escoba\n")
archivo_nuevo.write("palita\n")
archivo_nuevo.write("trapeador\n")
archivo_nuevo.close()

archivo_nuevo = open("productos.txt","r")
contenido = archivo_nuevo.read()
print (contenido)
archivo_nuevo.close()



    
