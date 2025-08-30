# Ejercicio1
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Por favor, ingrese su edad: "))
# if edad >= 18:
#     print("Es mayor de edad")

# Ejercicio2
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = float(input("Ingrese su calificación "))
# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")



# Ejercicio3
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# num1 = int(input("Ingrese un número "))
# if num1 % 2 == 1:
#     print("Por favor ingrese un número par")
# else:
#     print("Ha ingresado un número par")

# Ejercicio4
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
# edad = int(input("Ingrese su edad "))
# if edad < 12:
#     print ("Niño/a")
# elif edad > 12 and edad < 18:
#     print ("Adoslescente")
# elif edad > 18 and edad < 30:
#     print ("Adulto joven")
# elif edad > 30:
#     print ("Adulto")


# Ejercicio5
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# clave = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
# cantCar = len(clave)

# if cantCar >= 8 and cantCar <= 14:
#      print ("Ha ingresado una contraseña correcta")
# else:
#      print ("Por favor ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio6
# 6) Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


# import random 
# numeros_aleatorios = [random.randint(1,100) for i in range (50)]
# print ("Los números son: ", numeros_aleatorios)
# import statistics
# media = statistics.mean (numeros_aleatorios)
# mediana = statistics.median(numeros_aleatorios)
# moda = statistics.mode(numeros_aleatorios)
# print("La media es: ", media)
# print("La mediana es: ",mediana)
# print("La moda es: ",moda)
# if media > mediana and mediana > moda:
#     print("Hay sesgo positivo")
# if media < mediana and mediana < moda:
#     print("Hay sesgo negativo")
# if media == mediana and media == moda:
#     print("No hay sesgo")


# Ejercicio7
# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# frase = input("Ingrese una frase o palabra ")
# ultima = frase[-1]
# if ultima == "a" or ultima == "e" or ultima == "i" or ultima =="o" or ultima == "u":
#     print (frase,"!")
# else:
#     print ("",frase)


# Ejercicio8
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre ")
# print ("Si quiere su nombre en mayúsculas, ingrese 1")
# print ("Si quiere su nombre en minúsculas, ingrese 2")
# print ("Si quiere su nombre con la primera letra en mayúsculas, ingrese 3")
# opcion = input("Ingrese una opción ")
# if opcion == "1":
#     print ("",nombre.upper())
# elif opcion == "2":
#     print("",nombre.lower())
# elif opcion == "3":
#     print("",nombre.title())



# Ejercicio9
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud = float(input("Ingrese la magnitud en la escala de Richter "))
# if magnitud <3:
#     print ("Muy leve (imperceptible).")
# elif magnitud >= 3 and magnitud <= 4:
#     print ("Leve (ligeramente perceptible).")
# elif magnitud >=4 and magnitud <=5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños).")
# elif magnitud >=5 and magnitud <=6:
#     print("Fuerte (puede causar daños en estructuras débiles).")
# elif magnitud >=6 and magnitud <=7:
#     print ("Muy Fuerte (puede causar daños significativos).")
# elif magnitud >7:
#     print ("Extremo (puede causar graves daños a gran escala).")

# Ejercicio10
# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print ("Si se encuentra en el hemisferio Norte, ingrese 1")
print ("Si se encuentra en el hemisferio Sur, ingrese 2")
hemisferio = input("Ingrese en que hemisferio se encuentra ")
mes = input("Ingrese el número del mes en el que se encuentra ")
dia = input("Ingrese el número del día de hoy ")
if hemisferio == "1":
    if mes == "1" or mes == "2":
        print ("Usted está en invierno")
    elif mes == "3":
        if dia <= "20":
             print ("Usted está en invierno")
        else:
             print ("Usted está en primavera")
    elif mes == "4" or mes == "5":
         print ("Usted está en primavera")
    elif mes == "6":
        if dia <= "20":
             print ("Usted está en primavera")
        else:
             print ("Usted está en verano")
    elif mes == "7" or mes == "8":
         print ("Usted está en verano")
    elif mes == "9":
        if dia <= "20":
               print ("Usted está en verano")
        else:
              print ("Usted está en otoño")
    elif mes == "10" or mes == "11":
         print ("Usted está en otoño")
    elif mes == "12":
        if dia <= "20":
              print ("Usted está en otoño")
        else:
             print ("Usted está en invierno") 
    else:
         print("los datos ingresados no son válidos")  
         
         
elif hemisferio == "2":
    if mes == "1" or mes == "2":
        print ("Usted está en verano")
    elif mes == "3":
        if dia <= "20":
             print ("Usted está en verano")
        else:
             print ("Usted está en otoño")
    elif mes == "4" or mes == "5":
         print ("Usted está en otoño")
    elif mes == "6":
        if dia <= "20":
             print ("Usted está en otoño")
        else:
             print ("Usted está en invierno")
    elif mes == "7" or mes == "8":
         print ("Usted está en invierno")
    elif mes == "9":
        if dia <= "20":
               print ("Usted está en invierno")
        else:
              print ("Usted está en primavera")
    elif mes == "10" or mes == "11":
         print ("Usted está en primavera")
    elif mes == 12:
        if dia <= "20":
              print ("Usted está en primavera")
        else:
             print ("Usted está en verano")
    else:
         print("los datos ingresados no son válidos")  



else: 
    print("los datos ingresados no son válidos")    

