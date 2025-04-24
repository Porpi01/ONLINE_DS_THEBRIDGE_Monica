lista_nombres_usuarios = []

max_nombres = 0

while max_nombres < 10:
    nombre = input("Introduce un nombre de usuario: ").strip()  
    

    if len(nombre) >= 3 and nombre.isalpha(): 
        nombre_mayuscula = nombre.title()  
        lista_nombres_usuarios.append(nombre_mayuscula)  
        print(f"El nombre {nombre_mayuscula} es correcto")
        max_nombres += 1  
    else:
        print(f"El nombre {nombre} es inválido, debe contener al menos 3 letras y ningún número")


print(f"Usuarios registrados correctamente en el sistema: {lista_nombres_usuarios}")
