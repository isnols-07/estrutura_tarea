#EJERCICIO 11
#Entrada
#Elementos

#Proceso
#Cada vez que aparece un elemento, aumentar su contador

#Salida
#Elemento más frecuente y frecuencia

#BOSQUEJO
#a → 1
#b → 1
#a → 2
#a → 3

#a es el más frecuente

class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):

        if elemento in self.frecuencias:
            self.frecuencias[elemento] = self.frecuencias[elemento] + 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):

        mayor = None
        cantidad_mayor = 0

        for elemento, cantidad in self.frecuencias.items():

            if cantidad > cantidad_mayor:

                cantidad_mayor = cantidad
                mayor = elemento

        return mayor

    def frecuencia_elemento(self, elemento):

        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0
# PROGRAMA PRINCIPAL
cf = ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.agregar_elemento("a")
cf.agregar_elemento("b")

print(cf.frecuencias)

print("Más frecuente:")
print(cf.elemento_mas_frecuente())

print("Frecuencia de a:")
print(cf.frecuencia_elemento("a"))

# VERIFICACIÓN
# a = 3
# b = 2
#
# Más frecuente = a

#ejercicio 11.1

class ContadorVotos:

  def __init__(self):
    self.votos = {}

  def registrar_voto(self, candidato):
    self.votos[candidato] = self.votos.get(candidato, 0) + 1

  def candidato_ganador(self):
    if not self.votos:
      return None
    ganador = None
    max_votos = -1
    for cand, cant in self.votos.items():
      if cant > max_votos:
        max_votos = cant
        ganador = cand
    return ganador

  def votos_por_candidato(self, candidato):
    return self.votos.get(candidato, 0)


# Ejemplo de uso:
cv = ContadorVotos()
for voto in ["Candidato A", "Candidato B", "Candidato A", "Candidato C", "Candidato A"]:
  cv.registrar_voto(voto)

print(f"Ganador: {cv.candidato_ganador()}")  # Candidato A
print(f"Votos Candidato B: {cv.votos_por_candidato('Candidato B')}")  # 1