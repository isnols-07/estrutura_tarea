#EJERCICIO 18
#Entrada
#Dos puntos (x,y).

#Proceso
#Aplicar:
#√((x2-x1)² + (y2-y1)²)

#Salida
#Distancia y punto más cercano.

#Bosquejo
#P1 = (0,0)
#P2 = (3,4)
#√((3-0)² + (4-0)²)
#√(9 + 16)
#√25
#5

class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):

        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):

        punto_cercano = None
        distancia_menor = None

        for punto in puntos:

            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )

            if distancia_menor is None or distancia < distancia_menor:

                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano
# PROGRAMA PRINCIPAL
cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

print(
    cd.punto_mas_cercano(
        (0, 0),
        (3, 4),
        (1, 1),
        (5, 5)
    )
)

print(cd.distancias)

# VERIFICACIÓN
# Distancia entre (0,0) y (3,4):
# 5.0

# Punto más cercano:
# (1,1)

#ejercicio 18.1

class GeometriaPuntos:

  def __init__(self):
    self.historial_distancias = []

  def distancia_manhattan(self, p1, p2):
    d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    self.historial_distancias.append(d)
    return d

  def punto_mas_lejano(self, referencia, *puntos):
    if not puntos:
      return None
    mas_lejano = None
    max_d = -1
    for p in puntos:
      d = self.distancia_manhattan(referencia, p)
      if d > max_d:
        max_d = d
        mas_lejano = p
    return mas_lejano


# Ejemplo de uso:
gp = GeometriaPuntos()
p_ref = (0, 0)
p_far = gp.punto_mas_lejano(p_ref, (2, 3), (5, 1), (1, 1))
print(f"Punto más lejano: {p_far}")  # (5, 1)
print(f"Historial distancias: {gp.historial_distancias}")  # [5, 6, 2]