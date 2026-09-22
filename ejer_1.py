# EJERCICIO 1
# ENTRADA:
# Recibimos varias notas.

# PROCESO:
# Verificamos si cada nota esta entre 0 y 100.
# Si es valida, la guardamos en una lista.
# Despues calculamos el promedio.

# SALIDA:
# Lista de notas validas y promedio.

#BOSQUEJO
#Notas:
#85 → valida → guardar
#92 → valida → guardar
#110 → invalida → no guardar
#78 → valida → guardar
#-5 → invalida → no guardar
#88 → valida → guardar
#Lista = [85, 92, 78, 88]
#Promedio = 343 / 4
#Promedio = 85.75


class calificador:
    def __init__(self):
        self.notas =[]

    def validar_nota(self, nota):
        if nota >0 and nota<=100:
            return True
        else:
            return False

    def guardar_nota(self, *args):

        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def c_promedio(self):
        if len(self.notas) == 0:
            return 0
        suma = 0
        for nota in self.notas:
            suma = suma + nota
        return suma/len(self.notas)

c = calificador()

print(c.guardar_nota(85, 92, 110, 78, -5, 88))

print(c.c_promedio())

#ejercicio1.1


class ControlHoras:

  def __init__(self):
    self.jornadas = []

  def validar_horas(self, horas):
    return 0 <= horas <= 24

  def cargar_jornadas(self, *args):
    for h in args:
      if self.validar_horas(h):
        self.jornadas.append(h)
    return self.jornadas

  def total_horas(self):
    return sum(self.jornadas)

  def promedio_diario(self):
    if len(self.jornadas) == 0:
      return 0
    suma = 0
    for j in self.jornadas:
       suma = suma + j
    return suma/len(self.jornadas)


# Ejemplo de uso:
ch = ControlHoras()
print(ch.cargar_jornadas(8, 10, -2, 12, 30, 6))  # [8, 10, 12, 6]
print(f"Total: {ch.total_horas()} horas")  # 36 horas
print(f"Promedio: {ch.promedio_diario()} horas/día")  # 9.0 horas/día