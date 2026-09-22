#EJERCICIO 19
#Entrada
#Producto y cantidad

#Proceso
#Agregar stock
#Comprobar si existe suficiente
#Restar
#Buscar bajo stock

#Salida
#True/False y lista

#Bosquejo
#pan → 50
#restar 30
#50 - 30 = 20
#Si mínimo = 25:
#20 < 25
#pan → bajo stock

class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):

        if producto in self.productos:

            self.productos[producto] = (
                self.productos[producto] + cantidad
            )

        else:

            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):

        if producto in self.productos:

            if self.productos[producto] >= cantidad:

                self.productos[producto] = (
                    self.productos[producto] - cantidad
                )

                return True

        return False

    def productos_bajo_stock(self, minimo):

        resultado = []

        for producto, cantidad in self.productos.items():

            if cantidad < minimo:
                resultado.append(producto)

        return resultado
# PROGRAMA PRINCIPAL
inv = Inventario()

inv.agregar_stock("pan", 50)

print(inv.restar_stock("pan", 30))

print(inv.productos)

print(inv.productos_bajo_stock(25))

# VERIFICACIÓN
# Stock inicial:
# pan = 50

# Restamos:
# 50 - 30 = 20

# 20 < 25
#
# Resultado:
# ["pan"]

#ejercicio19.1

class GestionBiblioteca:

  def __init__(self):
    self.libros = {}

  def agregar_ejemplares(self, libro, cantidad):
    self.libros[libro] = self.libros.get(libro, 0) + cantidad

  def prestar_libro(self, libro, cantidad):
    if self.libros.get(libro, 0) >= cantidad:
      self.libros[libro] -= cantidad
      return True
    return False

  def libros_criticos(self, limite_minimo):
    return [
        libro
        for libro, cantidad in self.libros.items()
        if cantidad <= limite_minimo
    ]


# Ejemplo de uso:
gb = GestionBiblioteca()
gb.agregar_ejemplares("Cien Años de Soledad", 5)
gb.agregar_ejemplares("El Principito", 2)

print(gb.prestar_libro("El Principito", 2))  # True
print(f"Stock crítico (<=1): {gb.libros_criticos(1)}")  # ['El Principito']