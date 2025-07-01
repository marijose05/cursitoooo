cesta_de_compra = []

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Ver Cesta")
    print("3. Eliminar")
    print("4. Salir")
    
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == '1':
        agregar= input("¿Qué quieres agregar?: ")
        cesta_de_compra.append(agregar)
        print(f"'{agregar}' añadido.")
    elif opcion == '2':
        if not cesta_de_compra:
            print("La cesta está vacía.")
        else:
            print("\n--- TU CESTA ---")
            for i, agregar in enumerate(cesta_de_compra, 1):
                print(f"{i}. {agregar}")
        
    elif opcion == '3': #
        if not cesta_de_compra:
            print("La cesta está vacía. No hay nada que eliminar.")
        else:
            print("\n--- ELIMINAR DE LA CESTA ---")
            for i, agregar in enumerate(cesta_de_compra, 1):
                print(f"{i}. {agregar}")
            
            try:
                eliminar = int(input("Introduce el número del elemento a eliminar: "))
                if 1 <= eliminar <= len(cesta_de_compra):
                    eliminar = cesta_de_compra.pop(eliminar - 1)
                    print(f"'{eliminar}' ha sido eliminado.")
                else:
                    print("Número no válido. Por favor, elige un número de la lista.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.")
    elif opcion == '4':
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")