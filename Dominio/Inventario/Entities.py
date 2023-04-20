class Bodega:
    def __init__(self) -> None:
        self.registroBoedegas = None
        self.nombre = None
        self.codigo = None
        self.ubicacion = None
        self.producto = None
        
    def almacenarProductos(self):
        self.registroBoedegas = (self.nombre, self.codigo, self.ubicacion, self.producto)
        return self.registroBoedegas
    

class Distribuidores:
    def __init__(self) -> None:
        self.registroDistribuidores = None
        self.nombre = None
        self.codigo = None
        self.perfil = None
        self.direccion = None
        
    def registraDistribuidores(self):
        self.registroDistribuidores = (self.nombre, self.codigo, self.perfil, self.direccion)
        return self.registroDistribuidores
    

class Productos:
    def __init__(self) -> None:
        self.registroProducto = None
        self.codigo = None
        self.cantidad = None
        self.producto = None
        self.precio = None
        
    def registraProductos(self):
        self.registroProducto = (self.cantidad, self.codigo, self.producto, self.precio)
        return self.registroProducto
    