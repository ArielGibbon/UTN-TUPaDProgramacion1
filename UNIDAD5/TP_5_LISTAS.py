# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# notas = [8, 6, 7, 10, 5.5, 9.5, 8.5, 7.5, 6.5, 9]
# print (notas)
# acu = 0
# prom = 0
# mejor_nota = float ("-inf")
# peor_nota = float ("inf")
# for x in range (10):
#     if notas[x] > mejor_nota:
#         mejor_nota = notas[x]
#     if notas[x] < peor_nota:
#         peor_nota = notas[x]
#     acu += notas[x]
# print ("El promedio de notas es: ", acu/10)
# print ("La nota mas alta es: ", mejor_nota)
# print ("La nota mas baja es: ", peor_nota)
#----------------------------------------------------------------------------------
# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
 
# productos = ['prod1', 'prod2', 'prod3', 'prod4', 'prod5']
# prod1 = input("Ingrese un producto: "  )
# prod2 = input("Ingrese otro producto: "  )
# prod3 = input("Ingrese otro producto: "  )
# prod4 = input("Ingrese otro producto: "  )
# prod5 = input("Ingrese otro producto: "  )
    
# productos[0] = prod1
# productos[1] = prod2
# productos[2] = prod3
# productos[3] = prod4
# productos[4] = prod5
# productos_ordenados = sorted(productos, key=str.lower)
# print (productos_ordenados)
# eliminar = input("Que producto desea eliminar  "  )
# productos_ordenados.remove(eliminar)
# print (productos_ordenados)

#==============================================================================================
#
#  3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

# list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# pares_list = []
# impares_list = []
# cont_pares = 0
# cont_impares = 0
# for x in range (15):
#     import random
#     list_num [x] = random.randint(0,100)
#     if list_num[x]%2 == 0:
#         pares_list.append (list_num [x])
#         cont_pares += 1
#     else:
#         impares_list.append (list_num [x])
#         cont_impares += 1
# print (list_num)
# print ("La lista de números pares es: " ,pares_list, " y son ", cont_pares)
# print ( "La lista de números impares es: " ,impares_list, " y son ", cont_impares)
#
#===================================================================================================================
#
#  4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# print (datos)
# nueva_lista = list(set(datos))
# print(nueva_lista)

#=========================================================================================================
#
#     5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
# 
# lista_clase = ['Ana', 'Laura', 'María', 'Gabriela', 'Juan', 'Martín', 'Pablo', 'Pedro']
# modif_lista = input("Si desea ingresar o eliminar un estudiante ingrese SI, sino ingrese NO " )
# if modif_lista == 'SI':
#     ingresar_o_eliminar = input("Si desea Ingresar, coloque 'I', si desea eliminar, coloque 'E' " )
#     if ingresar_o_eliminar == 'I':
#         ingresado = input("Ingrese el nombre del estudiante a incorporar en la lista " )
#         lista_clase.append(ingresado)
#     else:
#         eliminado = input("Ingrese el nombre del estudiante a eliminar de la lista " )
#         lista_clase.remove (eliminado)    
# print(lista_clase)
# print ("Fin del programa")
#=========================================================================================================
# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

# nueva_lista = [1, 2, 3, 4, 5, 6, 7]
# for x in range (6):
#     num1 = nueva_lista[0]
#     nueva_lista.remove(nueva_lista[0])
#     nueva_lista.append (num1)
# print(nueva_lista)
#==============================================================================================
# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

# temp_max = float ("-inf")
# temp_min = float ("inf")
# acu_tem_max = 0
# acu_tem_min = 0
# ampl_term = 0
# dia_semana = 1
# temp_sem = [
#     [10, 20],
#     [9 , 22],
#     [11, 21],
#     [12, 23],
#     [13, 33],
#     [15, 28],
#     [18, 30]
# ]
# for x in range (7):
#     acu_tem_min += temp_sem[x][0]
#     acu_tem_max += temp_sem[x][1]
    
#     if temp_sem[x][1] > temp_max:
#         temp_max = temp_sem[x][1]
#     if temp_sem[x][0] < temp_min:
#         temp_min = temp_sem[x][0]
#     if temp_sem[x][1]-temp_sem[x][0] > ampl_term:
#         ampl_term = temp_sem[x][1]-temp_sem[x][0]
#         dia_semana = temp_sem[x]
# prom_temp_max = acu_tem_max / 7
# prom_temp_min = acu_tem_min/ 7
# print ("El promedio de las temperaturas mínimas de la semana es: " ,prom_temp_max)
# print("El promedio de las temperaturas mínimas de la semana es: " ,prom_temp_min)
# print("La temperatura máxima de la semana es: " ,temp_max)
# print("La temperatura mínima de la semana es: " , temp_min)
# print("La mayor amplitud térmica de la semana fue: " , ampl_term, " que se registraron temperaturas de " ,  dia_semana, " grados")
#===================================================================================================================================

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia

# prom_est = [1,2,3,4,5]
# acu_1 = 0
# acu_2 = 0
# acu_3 = 0

# notas_materias = [
#     [8, 6, 7],
#     [10, 9, 10],
#     [6, 7, 8],
#     [9, 8, 7],
#     [5, 6, 9]
# ]
# for x in range(5):
#     prom_est[x]= (notas_materias[x][0]+notas_materias[x][1]+notas_materias[x][2]) / 3
#     acu_1 += notas_materias[x][0]
#     acu_2 += notas_materias[x][1]
#     acu_3 += notas_materias[x][2]

# prom_mat1 = acu_1 / 5
# prom_mat2 = acu_2 / 5
# prom_mat3 = acu_3 / 5

# print ("El promedio del estudiante 1 es: " ,prom_est[0])
# print ("El promedio del estudiante 2 es: " ,prom_est[1])
# print ("El promedio del estudiante 3 es: " ,prom_est[2])
# print ("El promedio del estudiante 4 es: " ,prom_est[3])
# print ("El promedio del estudiante 5 es: " ,prom_est[4])
# print ("El promedio de la materia 1 es: ", prom_mat1)
# print ("El promedio de la materia 2 es: ", prom_mat2)
# print ("El promedio de la materia 3 es: ", prom_mat3)
#=============================================================================================
# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

# ta_te_ti =  [
#      ['_', '_', '_'], 
#      ['_', '_', '_'], 
#      ['_', '_', '_'] ]

# for filas in ta_te_ti:
#     print("  ".join(filas))
#     print()

# jugador = "X"
# for turno in range(9):
#     print ("Turno del jugador  " ,jugador)
#     fila = int(input("Ingrese el número de fila (de 0 a 2): "))
#     columna = int(input("Ingrese el número de columna (de 0 a 2) :  "))
#     if  ta_te_ti[fila][columna] == "-":
#         ta_te_ti[fila][columna] = jugador
#     for f in ta_te_ti:
#         print(" ".join(filas))
#     print()
#     if jugador == "X":
#         jugador = "O"
#     else:
#         jugador = "X"

# print ("Fin del programa")
#=================================================================================================

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    ['dia1','dia2', 'dia3', 'dia4', 'dia5', 'dia6', 'dia7'],        
    ['dia1','dia2', 'dia3', 'dia4', 'dia5', 'dia6', 'dia7'],        
    ['dia1','dia2', 'dia3', 'dia4', 'dia5', 'dia6', 'dia7'],    
    ['dia1','dia2', 'dia3', 'dia4', 'dia5', 'dia6', 'dia7']
]
cant_filas = len(ventas)
for x in range(cant_filas):
    print(ventas[x])

for i in range(7):
    prod1 = int(input("Ingrese la cantidad vendida del producto 1 "))
    prod2 = int(input("Ingrese la cantidad vendida del producto 2 "))
    prod3 = int(input("Ingrese la cantidad vendida del producto 3 "))
    prod4 = int(input("Ingrese la cantidad vendida del producto 4 "))
    ventas[0].pop(0)
    ventas[0].append(prod1)
    ventas[1].pop(0)
    ventas[1].append(prod2)
    ventas[2].pop(0)
    ventas[2].append(prod3)
    ventas[3].pop(0)
    ventas[3].append(prod4)
cant_filas = len(ventas)
for x in range(cant_filas):
    print(ventas[x])





    

