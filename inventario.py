#main

import funcionesInventario as fn
while True:
    fn.mostrar_Menu()
    opcion=fn.leer_opcion()    

    match opcion:
        case 1:
            print()#agregar
        case 2:
            print()#buscar
        case 3:
            print()#eliminar
        case 4:
            print()#actualizar
        case 5:
            print()#mostrar
        case 6:
            break
