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