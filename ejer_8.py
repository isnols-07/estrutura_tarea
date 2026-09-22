#EJERCICIO 8
#Entrada
#Equipos y jugadores

#Proceso
#Crear equipos, agregar jugadores y comparar cantidades

#Salida
#Equipo con más integrantes

#BOSQUEJO
#A → Juan, Pedro
#B → Luis, Ana, Carlos

#A = 2 jugadores
#B = 3 jugadores

#Mayor = B

class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_e(self, nombre_e):
        self.equipos[nombre_e]= []
    def agregar_j(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
    def mayor_jugador_e(self):
        mayor = ""
        cantidad = 0
        
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad:
                cantidad = len(jugadores)
                mayor = equipo
        return mayor
eq = Equipos()

eq.crear_e("a")
eq.crear_e("b")

eq.agregar_j("a", "pablo")
eq.agregar_j("b", "paul")
eq.agregar_j("b", "paco")

print(eq.equipos)
print(eq.mayor_jugador_e())

#ejercicio 8.1

class GestorDepartamentos:

  def __init__(self):
    self.departamentos = {}

  def crear_departamento(self, nombre_depto):
    
      self.departamentos[nombre_depto] = []

  def asignar_empleado(self, departamento, empleado):
    
      self.departamentos[departamento].append(empleado)

  def departamento_mas_poblado(self):
    mas_p = ""
    cantidad = 0
    for depertamento, empleado in self.departamentos.items():
        if len(empleado) > cantidad:
            cantidad = len(empleado)
            mas_p = depertamento
    return mas_p



# Ejemplo de uso:
gd = GestorDepartamentos()
gd.crear_departamento("Sistemas")
gd.crear_departamento("Ventas")
gd.asignar_empleado("Sistemas", "Ana")
gd.asignar_empleado("Sistemas", "Juan")
gd.asignar_empleado("Ventas", "Pedro")

print(f"Departamento con más gente: {gd.departamento_mas_poblado()}")  # Sistemas