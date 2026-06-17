#main
inventario=[]
import funcionesInventario as fn
while True:
    fn.mostrar_Menu()
    opcion=fn.leer_opcion()    

    match opcion:
        case 1:
            fn.agregar_producto(inventario)
        case 2:
            nombre=input("nombre del producto a buscar: ")
            pos=fn.buscar_producto(inventario, nombre)
            if pos != -1:
                print("producto encontrado")
            else:
                print("producto no encontrado")
            
        case 3:
            fn.eliminar_producto(inventario)
        case 4:
            fn.actualizar_disponibilidad(inventario)
            print("disponibilidad actualizada")
        case 5:
            print()#mostrar
        case 6:
            print("👋 Gracias por usar el sistema de inventario. Hasta pronto.")
            break
