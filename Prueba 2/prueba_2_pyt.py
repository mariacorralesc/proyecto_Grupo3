
class Articulo:
    def __init__(self, nombre, descripcion, cantidad_disponible):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad_disponible = cantidad_disponible

class Bodega:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

class Distribuidor:
    def __init__(self, nombre, direccion, perfil):
        self.nombre = nombre
        self.direccion = direccion
        self.perfil = perfil

class Asignacion:
    def __init__(self, articulo, bodega, cantidad_disponible):
        self.articulo = articulo
        self.bodega = bodega
        self.cantidad_disponible = cantidad_disponible

class Entrega:
    def __init__(self, articulo, distribuidor, cantidad_entregada):
        self.articulo = articulo
        self.distribuidor = distribuidor
        self.cantidad_entregada = cantidad_entregada


lista_articulos = []
lista_bodegas = []
lista_distribuidores = []
lista_asignaciones = []
lista_entregas = []


def menu():
    while True:
        print("Bienvenido al sistema de gestión de inventario.\n")
        print("1. Crear artículo")
        print("2. Crear bodega")
        print("3. Crear distribuidor")
        print("4. Asignar artículo a bodega")
        print("5. Entregar artículo a distribuidor")
        print("6. Mostrar lista de artículos")
        print("7. Mostrar lista de bodegas")
        print("8. Mostrar lista de distribuidores")
        print("9. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            crear_articulo()
        elif opcion == "2":
            crear_bodega()
        elif opcion == "3":
            crear_distribuidor()
        elif opcion == "4":
            asignar_articulo()
        elif opcion == "5":
            entregar_articulo()
        elif opcion == "6":
            mostrar_articulos()
        elif opcion == "7":
            mostrar_bodegas()
        elif opcion == "8":
            mostrar_distribuidores()
        elif opcion == "9":
            break
        else:
            print("Opción inválida.")

def crear_articulo():
    nombre = input("Ingresar nombre del artículo: ")
    descripcion = input("Ingrese la descripción del artículo: ")
    cantidad = int(input("Ingrese la cantidad disponible del artículo: "))
    articulo = Articulo(nombre, descripcion, cantidad)
    lista_articulos.append(articulo)
    return articulo

def crear_bodega():
    nombre = input("Ingrese el nombre de la bodega: ")
    ubicacion = input("Ingrese la ubicación de la bodega: ")
    bodega = Bodega(nombre, ubicacion)
    lista_bodegas.append(bodega)
    return bodega

def crear_distribuidor():
    nombre = input("Ingrese el nombre del distribuidor: ")
    direccion = input("Ingrese la dirección del distribuidor: ")
    perfil = input("Ingrese el perfil del distribuidor: ")
    distribuidor = Distribuidor(nombre, direccion, perfil)
    lista_distribuidores.append(distribuidor)
    return distribuidor

def asignar_articulo():
    articulo = input("Ingrese el nombre del artículo a asignar: ")
    bodega = input(
        "Ingrese el nombre de la bodega a la que se asignará el artículo: ")
    cantidad = int(
        input("Ingrese la cantidad disponible del artículo en la bodega: "))
    articulo_obj = buscar_articulo(articulo)
    bodega_obj = buscar_bodega(bodega)
    if articulo_obj and bodega_obj:
        asignacion = Asignacion(articulo_obj, bodega_obj, cantidad)
        lista_asignaciones.append(asignacion)
        print("Artículo asignado correctamente")
    else:
        print("Artículo o bodega no existen")

def entregar_articulo():
    articulo = input("Ingrese el nombre del artículo a entregar: ")
    distribuidor = input(
        "Ingrese el nombre del distribuidor al que se entregará el artículo: ")
    cantidad = int(input("Ingrese la cantidad entregada del artículo: "))
    articulo_obj = buscar_articulo(articulo)
    distribuidor_obj = buscar_distribuidor(distribuidor)
    if articulo_obj and distribuidor_obj:
        entrega = Entrega(articulo_obj, distribuidor_obj, cantidad)
        lista_entregas.append(entrega)
        print("Artículo entregado exitosamente.")
    else:
        print("Artículo o distribuidor no encontrados.")

def buscar_articulo(nombre):
    for articulo in lista_articulos:
        if articulo.nombre == nombre:
            return articulo
    return None

def buscar_bodega(nombre):
    for bodega in lista_bodegas:
        if bodega.nombre == nombre:
            return bodega
    return None

def buscar_bodega(nombre):
    for bodega in lista_bodegas:
        if bodega.nombre == nombre:
            return bodega
    return None

def buscar_distribuidor(nombre):
    for distribuidor in lista_distribuidores:
        if distribuidor.nombre == nombre:
            return distribuidor
    return None

def mostrar_articulos():
    for articulo in lista_articulos:
        print(
            f"{articulo.nombre}: {articulo.descripcion} ({articulo.cantidad_disponible} disponibles)")

def mostrar_bodegas():
    for bodega in lista_bodegas:
        print(f"{bodega.nombre}: {bodega.ubicacion}")

def mostrar_distribuidores():
    for distribuidor in lista_distribuidores:
        print(
            f"{distribuidor.nombre}: {distribuidor.direccion} ({distribuidor.perfil}")
