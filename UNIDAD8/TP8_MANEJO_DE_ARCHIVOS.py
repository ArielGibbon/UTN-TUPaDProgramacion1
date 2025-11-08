#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
print ("1. Creando archivo") 
archivo = open("productos.txt", "w")
archivo.write("cuchillo, 3000, 250\n")
archivo.write("tenedor, 1500, 200\n")
archivo.write("cuchara, 2000, 300\n")
archivo.close()

##############################################################################################################3
#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato: 
#   Producto: Lapicera | Precio: $120.5 | Cantidad: 30
archivo = open('productos.txt', 'r')

print("2. Leer y mostrar productos")

for linea in archivo:
    linea = linea.strip()
    datos = linea.split(",")
    
    nombre = datos[0]      
    precio = datos[1]      
    cantidad = datos[2]    
    
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


archivo.close() 


##################################################################################################################

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente. 


print ("3. Agregar productos")
archivo = open('productos.txt', 'r')



for linea in archivo:
    
    linea = linea.strip()
    datos = linea.split(",")
    nombre = datos[0]      
    precio = datos[1]      
    cantidad = datos[2]    
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

archivo.close()

print("Ingrese los datos del nuevo producto:\n")
nombre_nuevo = input("Nombre del producto: ")
precio_nuevo = input("Precio: ")
cantidad_nueva = input("Cantidad: ")

archivo = open('productos.txt', 'a')

archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

archivo.close()

print(f"\n Producto '{nombre_nuevo}' agregado")


###################################################################################################################3
#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.

print ("4. DICCIONARIO")

archivo = open('productos.txt', 'r')

productos = []


for linea in archivo:
    linea = linea.strip()
    datos = linea.split(",")
    producto = {
        'nombre': datos[0],
        'precio': datos[1],
        'cantidad': datos[2]
    }
    
    productos.append(producto)

archivo.close()

for producto in productos:
    print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")


##################################################################################################################
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error.

print ("5. BUSCAR PRODUCTO POR NOMBRE")
archivo = open('productos.txt', 'r')


producto_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for producto in productos:
    if producto['nombre'].lower() == producto_buscar.lower():
        encontrado = True
        print("\n Producto encontrado:")
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Precio: ${producto['precio']}")
        print(f"  Cantidad: {producto['cantidad']}")
        break 

if not encontrado:
    print(f"\n El producto '{producto_buscar}' no está.")

####################################################################################################
#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista.
#
print("Guardar productos actualizados\n")

archivo = open('productos.txt', 'w')

for producto in productos:
    linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
    archivo.write(linea)


archivo.close()

print("Archivo 'productos.txt' actualizado exitosamente")



