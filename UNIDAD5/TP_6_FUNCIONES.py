#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal
 
##Definicion de funcion
#def imprimir_hola_mundo():
#    return "Hola mundo!"
##Programa principal
#saludar = imprimir_hola_mundo()
#print (f"{saludar}")

######################################################################################

#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
#  “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#Definir función
#def saludar_usuario(nombre):
#  return f"Hola {nombre} !"

##Programa principal
#nom = input("Ingrese su nombre ")
#saludar = saludar_usuario(nom)
#print ("", saludar)

#########################################################################################

#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#  Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#Definir función
#def informacion_personal (nombre, apellido, edad, residencia):
#    return f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {residencia} "

#Programa principal
#a = input ("Ingrese su nombre ")
#b = input ("Ingrese su apellido ")
#c = input ("Indique su edad ")
#d = input ("Indique su lugar de residencia ")

#informacion = informacion_personal(a,b,c,d)
#print ("", informacion)

###################################################################################

#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo.
#  calcular_perimetro_circulo(radio) que reciba el radio como parámetro
#  y devuelva el perímetro del círculo.
#  Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#definir funciones
# from math import pi
# def calcular_area_circulo (radio):
#     return pi * (radio * radio)
# def calcular_perimetro_circulo (radio):
#     return 2 * pi * radio

#Programa principal

# r = int(input ("Ingrese el radio: "))
# area = calcular_area_circulo(r)
# perim = calcular_perimetro_circulo(r)

# print (f"El area del circulo es {area} y el perímetro es: {perim} ")

##################################################################################################
#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos 
# y mostrar el resultado usando esta función.
#Definir funciones
# def segundos_a_horas (segundos):
#     return segundos/3600
# #Programa principal
# seg = int(input("Ingrese la cantidad de segundos "))
# horas = segundos_a_horas(seg)
# print (f"{seg } segundos equivalen a {horas} horas")

##############################################################################################
#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Definir la función
def tabla_de_multiplicar (numero):
    for i in range (11):
        print (f"{numero} * {i} = {numero*i}")

#Programa principal
num1 = int(input("Ingrese un número "))
tabla = tabla_de_multiplicar(num1)
print (f"Tabla de multiplicar de {num1}. ")


