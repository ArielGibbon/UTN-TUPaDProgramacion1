

def mostrar_menu():
    
    
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
                print("Agregar un pais")
            case "2":
                print("Actualizar datos de población y superficie")
            case "3":
                print("Buscar un país por nombre")
            case "4":
                print("Filtrar países (seleccionar rango)")
            case "5":
                print("Mostrar lista de países ordenados por rango")
            case "6":
                print("Mostrar estadísticas por país")
            case "7":
                print("Gracias por utilizar nuestra aplicación :)")
                break
            case _:
                print("La opción ingresada es inválida")


mostrar_menu()