import funciones

def menu_administrador(lista_usuarios):
    opciones = [
        funciones.registrar_usuario,  
        funciones.mostrar_usuarios,   
        funciones.buscar_usuario,     
        funciones.modificar_usuario,  
        funciones.eliminar_usuario    
    ]
    
    while True:
        print("\n*** MENU ADMINISTRADOR ***\n1. Registrar\n2. Mostrar\n3. Buscar\n4. Modificar\n5. Eliminar\n6. Cerrar sesión")
        try:
            opcion = int(input("Opción (1-6): "))
            
            if opcion == 6: 
                print("\nCerrando sesión..."); break
            elif 1 <= opcion <= 5: 
                opciones[opcion - 1](lista_usuarios)
            else: 
                print("\n Opción inválida.")
        except ValueError:
            print("\n Error: Debes ingresar un número del 1 al 6, no letras.")
