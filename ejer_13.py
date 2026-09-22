#EJERCICIO 13
#Entrada
#Dos o más listas

#Proceso
#Tomar primero de una, después de otra

#Salida
#Lista intercalada

#Bosquejo
#Lista 1 = [1,2]
#Lista 2 = [3,4]

#1 → 3 → 2 → 4

#Resultado:
#[1,3,2,4]

class CombinadorListas:

    def intercalar(self, lista1, lista2):

        resultado = []

        i = 0

        while i < len(lista1) or i < len(lista2):

            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

            i = i + 1

        return resultado

    def intercalar_multiples(self, *listas):

        if len(listas) == 0:
            return []

        resultado = list(listas[0])

        i = 1

        while i < len(listas):

            resultado = self.intercalar(resultado, listas[i])

            i = i + 1

        return resultado
# PROGRAMA PRINCIPAL
cl = CombinadorListas()

print(cl.intercalar([1, 2], [3, 4]))

print(cl.intercalar_multiples(
    [1, 2],
    [3, 4],
    [5, 6]
))

# VERIFICACIÓN
# [1,2] + [3,4]
# Resultado:
# [1,3,2,4]

#ejercico 13.1 

class MezcladorListas:

  def fusionar_por_bloques(self, lista1, lista2):
    resultado = []
    max_len = max(len(lista1), len(lista2))
    for i in range(max_len):
      if i < len(lista1):
        resultado.append(lista1[i])
      if i < len(lista2):
        resultado.append(lista2[i])
    return resultado

  def concatenar_sin_repetir(self, *listas):
    resultado = []
    vistos = set()
    for l in listas:
      for elem in l:
        if elem not in vistos:
          vistos.add(elem)
          resultado.append(elem)
    return resultado


# Ejemplo de uso:
ml = MezcladorListas()
print(ml.fusionar_por_bloques([1, 2, 3], ["a", "b"]))  # [1, 'a', 2, 'b', 3]
print(ml.concatenar_sin_repetir([1, 2], [2, 3, 4], [4, 5]))  # [1, 2, 3, 4, 5]