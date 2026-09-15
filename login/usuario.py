def menu_usuario():
    while True:
        print("\n***** MENU DE USUARIO *****\n1. Ver información\n2. Consultar datos\n3. Realizar operación\n4. Cerrar sesión")
        try:
            opcion = int(input("Opción (1-4): "))
            if opcion == 1: print("\n Sistema modular en Python.")
            elif opcion == 2: print("\n No hay métricas adicionales.")
            elif opcion == 3: print("\n Operación estándar realizada.")
            elif opcion == 4: print("\nCerrando sesión..."); break
            else: print("\n Opción inválida.")
        except ValueError:
            print("\n Error: Debes ingresar un número del 1 al 4, no letras.")
