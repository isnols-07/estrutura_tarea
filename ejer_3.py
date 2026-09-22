# EJERCICIO 3
#Entrada
#Nombre y precio de artículos

#Proceso
#Guardar en diccionario
#Sumar precios.
#Buscar artículos dentro de un rango

#Salida
#Total y lista de artículos

#BOSQUEJO
#pan → 2.50
#leche → 3.00
#arroz → 4.00

#Total = 2.50 + 3.00 + 4.00
#Total = 9.50

#Rango 2.50 - 3.00:
#pan
#leche


class CarroCompras:
    def __init__(self):
        self.articulos = {}
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total = total + precio
        return total
    def articulos_por_rango(self, preciomin, preciomax):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio >= preciomin and precio <= preciomax:
                resultado.append(nombre)
        return resultado

c = CarroCompras()

c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 4.00)

print("Artículos:", c.articulos)

print("Total:", c.total_carrito())

print("Artículos entre 2.50 y 3.00:")
print(c.articulos_por_rango(2.50, 3.00))

#ejercico3.1

class Nomina:

  def __init__(self):
    self.empleados = {}

  def agregar_empleado(self, nombre, salario):
    self.empleados[nombre] = salario

  def total_nomina(self):
    total = 0
    for salario in self.empleados.values():
       total = total + salario
    return total

  def empleados_por_rango(self, salario_min, salario_max):
    return [
        nombre
        for nombre, salario in self.empleados.items()
        if salario_min <= salario <= salario_max
    ]


# Ejemplo de uso:
nom = Nomina()
nom.agregar_empleado("Luis", 450)
nom.agregar_empleado("María", 800)
nom.agregar_empleado("Pedro", 1200)

print(f"Total nómina: ${nom.total_nomina()}")  # $2450
print(
    f"Sueldos entre $400 y $900: {nom.empleados_por_rango(400, 900)}"
)  # ['Luis', 'María']