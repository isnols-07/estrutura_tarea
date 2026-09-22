#EJERCICIO 4
#Entrada
#Una o varias listas

#Proceso
#Recorrer la lista desde el último elemento hasta el primero

#Salida
#Lista invertida

#BOSQUEJO
#Lista:
#[1, 2, 3]

#Último → 3
#Luego → 2
#Luego → 1

#Resultado:
#[3, 2, 1]

class InversorSecuencia:
    def invertir_lista (self, lista):
        invertida = []

        i = len(lista) - 1
        while i >=0:
            invertida.append(lista[i])
            i = i -1
        return invertida
    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            original = tuple(lista)
            resultado[original] = self.invertir_lista(lista)
        return resultado

inv = InversorSecuencia()

print(inv.invertir_lista([1, 2, 3]))

print(inv.invertir_multiples(
    [1, 2, 3],
    [4, 5, 6]
))

#ejercicio4.1

class TransformadorSecuencia:

  def duplicar_elementos(self, lista):
    resultado = []
    for elem in lista:
      resultado.append(elem)
      resultado.append(elem)
    return resultado

  def procesar_multiples(self, *listas):
    resultado_dict = {}
    for idx, l in enumerate(listas, 1):
      resultado_dict[f"lista_{idx}"] = self.duplicar_elementos(l)
    return resultado_dict


# Ejemplo de uso:
ts = TransformadorSecuencia()
print(ts.duplicar_elementos([1, 2, 3]))  # [1, 1, 2, 2, 3, 3]
print(
    ts.procesar_multiples(["a", "b"], [10, 20])
)  # {'lista_1': ['a', 'a', 'b', 'b'], 'lista_2': [10, 10, 20, 20]}