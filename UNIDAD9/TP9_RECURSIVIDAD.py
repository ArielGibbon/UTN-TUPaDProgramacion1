#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(n):
     return 1 if n == 0 else n * factorial(n-1)

numero = int(input("Ingresa un número: "))

if numero < 1:
    print("Por favor, ingresa un número mayor o igual a 1")
else:
    print(f"\nFactoriales de 1 hasta {numero}:")

    
   
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")

############################################################################################################3

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("Que posición de Fibonacci querés ver?: "))

if posicion < 0:
    print("Dato inválida: el número debe ser mayor a 0")
else:
    print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
    
    for i in range(posicion + 1):
        valor = fibonacci(i)
        print(f"Posición {i}: {valor}")

################################################################################################################
# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general.


def potencia(base, exponente):
    if exponente == 0:
        return 1
    
    else:
        return base * potencia(base, exponente - 1)
    

base = int(input("Ingresa el número base: "))
exponente = int(input("Ingresa el exponente: "))

if exponente < 0:
    print("Dato inválido. Ingresar un numero mayor o igual a 0")
else:
    resultado = potencia(base, exponente)
    print(f"Resultado: {base}^{exponente} = {resultado}")
   
    for i in range(exponente + 1):
        print(f"{base}^{i} = {potencia(base, i)}")

##################################################################################################
#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    
    else:
        return decimal_binario(n // 2) + str(n % 2)

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Dato inválido. Ingresar un número positivo")
else:
    binario = decimal_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
    
    # Mostrar conversiones adicionales como ejemplo
    print(f"\nConversiones de 0 hasta {numero}:")
    
    for i in range(numero + 1):
        print(f"{i} en decimal = {decimal_binario(i)} en binario")

###############################################################################################################3

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
#     Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
       
    return es_palindromo(palabra[1:-1])


texto = input("Ingresa una palabra (sin espacios ni tildes): ")

if es_palindromo(texto):
    print(f" '{texto}' Es un palíndromo")
else:
    print(f"'{texto}' No es un palíndromo")

##########################################################################################################3
#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
 #    Restricciones: 
#No se puede convertir el número a string. #
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

num1 = int(input("Ingresa un número entero positivo: "))

if num1 < 0:
    print("Por favor, ingresa un número positivo")
else:
    resultado = suma_digitos(num1)
    print(f"La suma de los dígitos de {num1} es: {resultado}")

#####################################################################################################################
#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
 
      #Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

def contar_bloques(n):
      
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques_base = int(input("¿Cuántos bloques hay en el nivel más bajo?: "))

if bloques_base < 1:
    print("Por favor, ingresa un número mayor o igual a 1")
else:
    total = contar_bloques(bloques_base)
    print(f"se necesitan en total: {total} bloques")

###########################################################################################################
#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
      #Ejemplos: 
#contar_digito(12233421, 2)   → 3   
#contar_digito(5555, 5)       → 4 
#contar_digito(123456, 7)     → 0   
    
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("¿Qué dígito quieres contar? (0-9): "))

if numero < 0:
    print("Por favor, ingresa un número positivo")
elif digito < 0 or digito > 9:
    print("El dígito debe estar entre 0 y 9")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces ")
    
   
    
    





        


