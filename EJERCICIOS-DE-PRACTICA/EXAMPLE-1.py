# print ("Hola")
# cont = 1
# while cont <= 5:
#     print (cont,"Debo aprender ciclos")
#     cont+=1
# print ("Chau")

# 
# 

# for x in range (1,5):
#     for i in range(1,11):
#         print(f"{x} X {i} = {x * i}")
#     print("-------------")    


# notas = [9.1, 8.5, 7.3]
# notas.append(7.3)
# notas.append(8.0)
# notas.append(7.6)
# notas[2] = 9
# print(notas)
# print(notas[0:2])
# #print(type(notas))


# Inicializar tablero 3x3 con guiones
tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

# Mostrar tablero inicial
for fila in tablero:
    print(" ".join(fila))
print()

# Turnos alternados (máx. 9 jugadas)
jugador = "X"
for turno in range(9):
    print("Turno del jugador", jugador)
    
    fila = int(input("Ingresa fila (0-2): "))
    columna = int(input("Ingresa columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, intenta de nuevo")
        continue  # no cambia de jugador, repite turno
    
    # Mostrar tablero después de la jugada
    for f in tablero:
        print(" ".join(f))
    print()
    
    # Cambiar jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"
print ("Fin del programa")

