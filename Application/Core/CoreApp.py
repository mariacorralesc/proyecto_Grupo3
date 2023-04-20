class Persistencia:
    ListaProductos = []
    
    @classmethod
    def agregarProducto(self,objeto):
        self.ListaProductos.append(objeto)
    
    @classmethod    
    def obtenerProducto(self):
        return self.ListaProductos