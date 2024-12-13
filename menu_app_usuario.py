from service.user_service import UserService

print('  *** Laboratorio Usuarios ***  '.center(80,'-'))

service = UserService()
opcion_menu = 0

while True:
    print(f''' MENU
     Opciones:
     1 - Agregar usuario
     2 - Listar usuarios
     3 - Actualizar usuario
     4 - Eliminar usuario
     5 - Salir
    ''')

    opcion_menu = int(input('Seleccione una opción del menu (1 - 5): '))

    if opcion_menu == 1:
        username = input('Ingrese el username: ')
        password = input('Ingrese el password: ')
        service.add_user(username, password)
    elif opcion_menu == 2:
        users = service.get_all_user()
        for user in users:
            print(user)
    elif opcion_menu == 3:
        id = input('Ingrese el user_id para editar: ')
        username = input('Ingrese el username: ')
        password = input('Ingrese el password: ')
        counter = service.update_user(id, username, password)
        if counter == 0:
            print('Usuario no actualizado')
        elif counter == 1:
            print('Usuario actualizado')
    elif opcion_menu == 4:
        id = input('Ingrese el user_id para eliminar: ')
        counter = service.delete_user(id)
        if counter == 0:
            print('Usuario no eliminado')
        elif counter == 1:
            print('Usuario eliminado')
    elif opcion_menu == 5:
        break