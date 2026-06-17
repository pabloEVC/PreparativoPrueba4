def mostrar_Menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
def leer_opcion():
    while True:
        try:
            op=int(input("ingrese opcion: "))
            if 1<= op <=6:
                return op
            else:
                print("opcion invalida")
        except ValueError:
            print("debe ingresar un numero")

def validar_nombre():
    return nombre.strip() != ""

def validar_stock(productos):
    nombre=input("ingrese nombre del producto")