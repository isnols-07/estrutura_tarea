#EJERCICIO 17
#Entrada
#Edades

#Proceso
#Clasificar cada edad y guardar en un diccionario

#Salida
#Diccionario de categorías y promedio

#Bosquejo
#5 → niño
#15 → adolescente
#30 → adulto
#70 → mayor

class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):

        if edad < 12:
            return "niño"

        elif edad < 18:
            return "adolescente"

        elif edad < 65:
            return "adulto"

        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):

        for edad in edades:

            categoria = self.clasificar_edad(edad)

            if categoria not in self.grupos:
                self.grupos[categoria] = []

            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):

        if categoria not in self.grupos:
            return 0

        edades = self.grupos[categoria]

        suma = 0

        for edad in edades:
            suma = suma + edad

        return suma / len(edades)
# PROGRAMA PRINCIPAL
ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 15, 30, 70))

print(ae.edad_promedio_categoria("adulto"))

# VERIFICACIÓN
# 5 → niño
# 15 → adolescente
# 30 → adulto
# 70 → mayor
#
# Resultado:
# {
#   'niño': [5],
#   'adolescente': [15],
#   'adulto': [30],
#   'mayor': [70]
# }

#ejercicio 17.1

class ClasificadorPrecios:

  def __init__(self):
    self.agrupado = {"Económico": [], "Estándar": [], "Premium": []}

  def clasificar_precio(self, precio):
    if precio < 20:
      return "Económico"
    elif precio <= 100:
      return "Estándar"
    else:
      return "Premium"

  def agrupar_productos(self, *precios):
    for p in precios:
      cat = self.clasificar_precio(p)
      self.agrupado[cat].append(p)
    return self.agrupado

  def promedio_por_categoria(self, categoria):
    precios = self.agrupado.get(categoria, [])
    return sum(precios) / len(precios)


# Ejemplo de uso:
cp = ClasificadorPrecios()
cp.agrupar_productos(12.5, 45.0, 150.0, 85.0, 8.0)
print(f"Categorías: {cp.agrupado}")
# {'Económico': [12.5, 8.0], 'Estándar': [45.0, 85.0], 'Premium': [150.0]}
print(f"Promedio Estándar: ${cp.promedio_por_categoria('Estándar')}")  # $65.0