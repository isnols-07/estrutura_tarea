#EJERCICIO 7
#Entrada
#Nombres y edades

#Proceso
#Guardar, filtrar mayores y calcular promedio

#Salida
#Lista de personas y promedio

#BOSQUEJO
#Ana → 28
#Bob → 17
#Luis → 20

#Mayores de 18:
#Ana
#Luis

class GestorPersonas:
    def __init__(self):
        self.persona = {}
    def registro_p(self, nombre, edad):
        self.persona[nombre]= edad
    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.persona.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado
    def promedio_edades(self):
        suma = 0
        for edad in self.persona.values():
            suma = suma + edad
        return suma/len(self.persona)

gp = GestorPersonas()

gp.registro_p("Ana", 28)
gp.registro_p("Bob", 17)
gp.registro_p("Luis", 20)

print(gp.persona)

print(gp.personas_mayores(18))

print(gp.promedio_edades())

#ejercicio 7.1
class CatalogoProductos:

  def __init__(self):
    self.productos = {}

  def agregar_producto(self, nombre, precio):
    self.productos[nombre] = precio

  def productos_costosos(self, precio_limite):
    resultado = []
    for nombre, precio in self.productos.items():
       if precio > precio_limite:
          resultado.append(nombre)
    return resultado

  def precio_promedio(self):
    if not self.productos:
      return 0.0
    return sum(self.productos.values()) / len(self.productos)


# Ejemplo de uso:
cp = CatalogoProductos()
cp.agregar_producto("Laptop", 1200)
cp.agregar_producto("Mouse", 25)
cp.agregar_producto("Teclado", 45)

print(cp.productos_costosos(30))  # ['Laptop', 'Teclado']
print(f"Precio promedio: ${cp.precio_promedio():.2f}")  # $423.33