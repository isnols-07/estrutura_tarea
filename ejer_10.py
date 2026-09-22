#EJERCICIO 10
#Entrada
#Descripción y prioridad

#Proceso
#Guardar tareas, buscar las de prioridad alta y eliminar una completada

#Salida
#Lista de tareas prioritarias

#BOSQUEJO
#("Estudiar", "alta")
#("Leer", "baja")
#("Tarea", "alta")

#Prioritarias:
#Estudiar
#Tarea

class Tareas:

    def __init__(self):
        # Lista de tuplas
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):

        tarea = (descripcion, prioridad)

        self.tareas.append(tarea)

    def tareas_prioritarias(self):

        resultado = []

        for tarea in self.tareas:

            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):

        for tarea in self.tareas:

            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False
# PROGRAMA PRINCIPAL
t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Hacer tarea", "alta")

print("Tareas:", t.tareas)

print("Prioritarias:")
print(t.tareas_prioritarias())

t.eliminar_completada("Estudiar")

print("Después de eliminar:")
print(t.tareas)

# VERIFICACIÓN
# Prioritarias:
# ("Estudiar", "alta")
# ("Hacer tarea", "alta")

#ejercicio 10.1

class GestorAtencion:

  def __init__(self):
    self.pacientes = []

  def registrar_paciente(self, nombre, nivel_urgencia):
    paciente = (nombre, nivel_urgencia.lower())
    self.pacientes.append(paciente)

  def pacientes_urgentes(self):
    resultado = []
    for paciente in self.pacientes:
       if paciente[1] == "critico":
          resultado.append(paciente)   
    return resultado

  def atender_paciente(self, nombre):
    for paciente in self.pacientes:
       if paciente[0] == nombre:
          self.pacientes.remove(paciente)
          return True
    return False

# Ejemplo de uso:
ga = GestorAtencion()
ga.registrar_paciente("Laura", "moderado")
ga.registrar_paciente("Roberto", "critico")
ga.registrar_paciente("Sofia", "critico")

print(f"Urgentes: {ga.pacientes_urgentes()}")
# [('Roberto', 'critico'), ('Sofia', 'critico')]

ga.atender_paciente("Roberto")
print(f"Pacientes restantes: {ga.pacientes}")
# [('Laura', 'moderado'), ('Sofia', 'critico')]