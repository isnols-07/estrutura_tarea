#EJERCICIO 6
#Entrada
#Temperaturas

#Proceso
#Guardar temperaturas y calcular mínimo, máximo y promedio

#Salida
#Valores estadísticos

#BOSQUEJO
#20, 25, 18, 30

#Mínima = 18
#Máxima = 30

#Promedio:
#20 + 25 + 18 + 30 = 93
#93 / 4 = 23.25

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    def registrartemp(self, temp):
        self.temperaturas.append(temp)
    def registrodemultiples(self, *temps):
        for temp in temps:
            self.registrartemp(temp)
    def maxima(self):
        return max(self.temperaturas)
    def minima(self):
        return min(self.temperaturas)
    def promedio(self):
        suma = 0
        for temp in self.temperaturas:
            suma = suma + temp
        return suma/len(self.temperaturas)

gt = GestorTemperatura()

gt.registrodemultiples(20, 25, 18, 30)

print("Temperaturas:", gt.temperaturas)
print("Mínima:", gt.minima())
print("Máxima:", gt.maxima())
print("Promedio:", gt.promedio())

#ejercicio 6.1

class GestorVentas:

  def __init__(self):
    self.ventas = []

  def registrar_venta(self, monto):
    self.ventas.append(monto)

  def registrar_lote(self, *montos):
    for m in montos:
      self.registrar_venta(m)

  def venta_minima(self):
    return min(self.ventas) 

  def venta_maxima(self):
    return max(self.ventas) 

  def venta_promedio(self):
    suma = 0
    for v in self.ventas:
       suma = suma + v
    return suma/len(self.ventas)
  

# Ejemplo de uso:
gv = GestorVentas()
gv.registrar_lote(150.0, 45.5, 300.0, 89.9)
print(f"Mínima: ${gv.venta_minima()}")  # $45.5
print(f"Máxima: ${gv.venta_maxima()}")  # $300.0
print(f"Promedio: ${gv.venta_promedio():.2f}")  # $146.35