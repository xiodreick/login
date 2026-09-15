def login(lista_usuarios):
    print("\n--- INICIO DE SESIÓN ---")
    try:
        u_ing = input("Usuario: ").strip()
        if u_ing.isdigit(): raise ValueError("El usuario no puede ser solo números.")
        
        c_ing = input("Contraseña: ")
        u = next((u for u in lista_usuarios if u["usuario"].lower() == u_ing.lower() and u["contrasena"] == c_ing), None)
        return u["rol"] if u else "incorrecto"
    except ValueError as e:
        print(f"\n Error: {e}")
        return "incorrecto"

def registrar_usuario(lista_usuarios):
    print("\n--- REGISTRAR NUEVO USUARIO ---")
    try:
        name = input("Nombre de usuario: ").strip()
        if name.isdigit(): raise ValueError("El nombre de usuario no puede ser un número.")
        if any(u["usuario"].lower() == name.lower() for u in lista_usuarios):
            print(f" El usuario \"{name}\" ya existe."); return

        c_registrada = input("Contraseña: ")
        
        lista_usuarios.append({"usuario": name, "contrasena": c_registrada, "rol": "usuario"})
        print(f" Usuario \"{name}\" registrado con éxito.")
    except ValueError as e:
        print(f"\n Error de formato: {e}")

def mostrar_usuarios(lista_usuarios):
    print("\n--- LISTA DE USUARIOS ---")
    if not lista_usuarios: print("No hay usuarios registrados.")
    for i, u in enumerate(lista_usuarios, 1):
        print(f"{i}. {u['usuario']} | Rol: {u['rol']}")

def buscar_usuario(lista_usuarios):
    print("\n--- BUSCAR USUARIO ---")
    try:
        name = input("Nombre a buscar: ").strip()
        if name.isdigit(): raise ValueError("Los nombres de usuario no contienen solo números.")
        u = next((u for u in lista_usuarios if u["usuario"].lower() == name.lower()), None)
        print(f" Encontrado -> {u['usuario']} | Rol: {u['rol']}" if u else " No encontrado.")
        return u
    except ValueError as e:
        print(f"\n Error: {e}")
        return None

def modificar_usuario(lista_usuarios):
    u = buscar_usuario(lista_usuarios)
    if u:
        try:
            pwd = input("Nueva contraseña (en blanco para mantener): ")
            if pwd: u["contrasena"] = pwd
            print(f" Usuario \"{u['usuario']}\" modificado.")
        except ValueError as e:
            print(f"\n Error: {e}")

def eliminar_usuario(lista_usuarios):
    print("\n--- ELIMINAR USUARIO ---")
    try:
        name = input("Nombre a eliminar: ").strip()
        if name.isdigit(): raise ValueError("Nombre inválido, se esperaban letras.")
        u = next((u for u in lista_usuarios if u["usuario"].lower() == name.lower()), None)
        if u:
            lista_usuarios.remove(u)
            print(f" Usuario \"{u['usuario']}\" eliminado.")
        else:
            print(" No se encontró el usuario.")
    except ValueError as e:
        print(f"\n Error: {e}")
