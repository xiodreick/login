import funciones
from administrador import menu_administrador
from usuario import menu_usuario

def main():
    base_usuarios = [
        {"usuario": "admin", "contrasena": "abcd", "rol": "administrador"},
        {"usuario": "usuario", "contrasena": "1234", "rol": "usuario"}
    ]
    print("*** BIENVENIDO AL SISTEMA LOGIN ***")
    
    while True:
        print("\n1. Iniciar Sesión\n2. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                tipo = funciones.login(base_usuarios)
                if tipo == "administrador": menu_administrador(base_usuarios)
                elif tipo == "usuario": menu_usuario()
                else: print("\n❌ Credenciales incorrectas.")
            elif opcion == 2:
                print("\n¡Hasta luego!"); break
            else: print("\n❌ Opción no válida.")
        except ValueError:
            print("\n❌ Error: Debes ingresar un número entero (ej. 1 o 2), no letras.")

main()
