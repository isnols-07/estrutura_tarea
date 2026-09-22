#EJERCICIO 12
#Entrada
#Pares (inicio, fin)

#Proceso
#Crear rangos y unirlos sin repetidos

#Salida
#Lista de elementos únicos

#Bosquejo
#Rango 1 = (1,3)
#→ 1,2,3

#Rango 2 = (2,4)
#→ 2,3,4

#Conjunto:
#{1,2,3,4}

#Lista:
#[1,2,3,4]

class SelectorRango:

    def crear_rango(self, inicio, fin):

        resultado = ()

        for numero in range(inicio, fin + 1):

            resultado = resultado + (numero,)

        return resultado

    def elementos_en_multiples_rangos(self, *rangos):

        elementos = set()

        for rango in rangos:

            inicio = rango[0]
            fin = rango[1]

            for numero in range(inicio, fin + 1):
                elementos.add(numero)

        return list(elementos)
# PROGRAMA PRINCIPAL
sr = SelectorRango()

print(sr.crear_rango(1, 3))

print(sr.elementos_en_multiples_rangos(
    (1, 3),
    (2, 4)
))

# VERIFICACIÓN
# Rango 1 = (1, 2, 3)
# Rango 2 = (2, 3, 4)
#
# Sin duplicados:
# [1, 2, 3, 4]

#ejercicio 12.1

class GeneradorRangoPares:

  def generar_pares(self, inicio, fin):
    pares = []
    for n in range(inicio, fin + 1):
      if n % 2 == 0:
        pares.append(n)
    return tuple(pares)

  def unir_pares_rangos(self, *rangos):
    conjunto_pares = set()
    for inicio, fin in rangos:
      sub_pares = self.generar_pares(inicio, fin)
      conjunto_pares.update(sub_pares)
    return sorted(list(conjunto_pares))


# Ejemplo de uso:
grp = GeneradorRangoPares()
print(grp.generar_pares(1, 7))  # (2, 4, 6)
print(grp.unir_pares_rangos((1, 5), (4, 10)))  # [2, 4, 6, 8, 10]