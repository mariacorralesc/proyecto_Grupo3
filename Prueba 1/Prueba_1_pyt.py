# Clase Artículo
class Artículo:
    def __init__(self, nombre, descripción, cantidad):
        self.nombre = nombre
        self.descripción = descripción
        self.cantidad = cantidad

# Clase Bodega
class Bodega:
    def __init__(self, nombre):
        self.nombre = nombre
        self.artículos = {}

    def agregar_artículo(self, artículo, cantidad):
        if artículo.nombre in self.artículos:
            self.artículos[artículo.nombre] += cantidad
        else:
            self.artículos[artículo.nombre] = cantidad

    def remover_artículo(self, artículo, cantidad):
        if artículo.nombre in self.artículos:
            if self.artículos[artículo.nombre] >= cantidad:
                self.artículos[artículo.nombre] -= cantidad
                return True
            else:
                print(
                    "La cantidad a remover es mayor a la cantidad disponible en la bodega.")
                return False
        else:
            print("El artículo no está en la bodega.")
            return False

# Clase Distribuidor
class Distribuidor:
    def __init__(self, nombre, dirección, teléfono):
        self.nombre = nombre
        self.dirección = dirección
        self.teléfono = teléfono
        self.artículos_entregados = {}

    def agregar_artículo_entregado(self, artículo, cantidad):
        if artículo.nombre in self.artículos_entregados:
            self.artículos_entregados[artículo.nombre] += cantidad
        else:
            self.artículos_entregados[artículo.nombre] = cantidad

# Función para generar el reporte en formato TXT
def generar_reporte(distribuidor):
    reporte = "Reporte de inventario entregado a " + distribuidor.nombre + ":\n"
    for artículo, cantidad in distribuidor.artículos_entregados.items():
        reporte += "Artículo: " + artículo + \
            " - Cantidad: " + str(cantidad) + "\n"
    return reporte


# Ejemplo
artículo1 = Artículo("Laptop", "Laptop HP modelo X", 5)
artículo2 = Artículo("Impresora", "Impresora Canon modelo Y", 10)

bodega1 = Bodega("Bodega 1")
bodega1.agregar_artículo(artículo1, 3)
bodega1.agregar_artículo(artículo2, 8)

distribuidor1 = Distribuidor("Distribuidor local", "Calle 123, Ciudad", "555-1234")
distribuidor1.agregar_artículo_entregado(artículo1, 2)
distribuidor1.agregar_artículo_entregado(artículo2, 5)

print(generar_reporte(distribuidor1))
