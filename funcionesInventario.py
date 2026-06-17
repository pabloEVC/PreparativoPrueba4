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

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_stock(stock):
    try:
        return float(stock) >=0
    except:
        return False
def validar_precio(precio):
    try:
        return int(precio) >0
    except:
        return False

def agregar_producto(lista):
    nombre=input("nombre del producto: ")
    precio=float(input("precio: $"))
    stock=int(input("stock"))

    if not validar_nombre(nombre):
        print("nombre invalido")
        return
    if not validar_precio(precio):
        print("precio invalido")
        return
    if not validar_stock(stock):
        print("stock invalido")
        return
    producto = {
        "nombre": nombre.strip(),
        "precio": float(precio),
        "stock" : int(stock)
    }
    lista.append(producto)
    print(" producto agregado correctamente ")

def buscar_producto(lista,nombre):
    for i,prod in enumerate(lista):
        if prod["nombre"].lower() == nombre.lower():
            return i
    return -1

def eliminar_producto(lista):
    nombre=input("nombre del producto a eliminar: ")
    pos=buscar_producto(lista, nombre)
    if pos != -1:
        lista.pop(pos)
        print(f"producto {nombre} eliminado")
    else: 
        print(f"no se encuentra el producto {nombre}")

def actualizar_disponibilidad(lista):
    for prod in lista:
        prod["disponible"] = prod["stock"] >0

def mostrar_producto(lista):
    actualizar_disponibilidad(lista)
    print("\n=== LISTA DE PRODUCTOS ===")
    for prod in lista:
        estado="DISPONIBLE" if prod["disponible"] else "sinstock"
        print(f"Nombre: {prod['nombre']}")
        print(f"Precio: ${prod['precio']}")
        print(f"Stock: {prod['stock']}")
        print(f"Estado: {estado}\n")
        
        
