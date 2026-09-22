#EJERCICIO 14
#Entrada
#Estudiante y nota

#Proceso
#Guardar, filtrar aprobados y comparar notas

#Salida
#Lista de aprobados y tupla con mejor estudiante

#Bosquejo
#Ana → 95
#Bob → 70
#Luis → 88

#Aprobados desde 70:
#Ana
#Bob
#Luis

#Mayor:
#Ana → 95

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):

        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):

        aprobados = []

        for estudiante, nota in self.notas.items():

            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):

        mejor_nombre = ""
        mejor_nota = 0

        for estudiante, nota in self.notas.items():

            if nota > mejor_nota:

                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)
# PROGRAMA PRINCIPAL
rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Luis", 88)

print(rn.notas)

print(rn.estudiantes_aprobados(70))

print(rn.mejor_estudiante())

# VERIFICACIÓN
# Ana = 95
# Bob = 70
# Luis = 88
#
# Mejor:
# ("Ana", 95)

#ejercicio 14.1

class RegistroAtletas:

  def __init__(self):
    self.tiempos = {}

  def registrar(self, atleta, tiempo):
    self.tiempos[atleta] = tiempo

  def clasificados(self, tiempo_maximo):
    return [atl for atl, t in self.tiempos.items() if t <= tiempo_maximo]

  def mejor_atleta(self):
    if not self.tiempos:
      return None
    mejor = None
    menor_tiempo = float("inf")
    for atl, t in self.tiempos.items():
      if t < menor_tiempo:
        menor_tiempo = t
        mejor = atl
    return (mejor, menor_tiempo)


# Ejemplo de uso:
ra = RegistroAtletas()
ra.registrar("Mateo", 10.5)
ra.registrar("Valeria", 9.8)
ra.registrar("Lucas", 11.2)

print(f"Clasificados (<=10.5s): {ra.clasificados(10.5)}")  # ['Mateo', 'Valeria']
print(f"Mejor marca: {ra.mejor_atleta()}")  # ('Valeria', 9.8)