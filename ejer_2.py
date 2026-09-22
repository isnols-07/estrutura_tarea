# EJERCICIO 2
# ENTRADA:
# Recibimos varias palabras.

# PROCESO:
# Guardamos las palabras en una lista.
# Tambien las guardamos en un conjunto.
# El conjunto elimina los duplicados.

# SALIDA:
# Cantidad de palabras unicas.

#BOSQUEJO
#hola
#mundo
#hola

#Lista:
#[hola, mundo, hola]

#Conjunto:
#{hola, mundo}

#Cantidad = 2

class a_palabras:
    def __init__(self):
        self.palabra = []
        self.palabraset = set()

    def aggword(self, palabra):
        self.palabra.append(palabra)
        self.palabraset.add(palabra)

    def c_palabras(self):
        return len(self.palabraset)

    def agg_palabrasm(self, *args):
        for palabra in args:
            self.aggword(palabra)

at = a_palabras()

at.agg_palabrasm("hola", "mundo", "hola")

print(at.palabra)
print(at.palabraset)
print(at.c_palabras())


#ejercico2.1

class ControlAsistencia:

  def __init__(self):
    self.asistentes_unicos = set()
    self.historial_ingresos = []

  def registrar_asistente(self, nombre):
    self.asistentes_unicos.add(nombre)
    self.historial_ingresos.append(nombre)

  def contar_unicos(self):
    return len(self.asistentes_unicos)

  def registrar_grupo(self, *args):
    for nombre in args:
      self.registrar_asistente(nombre)


# Ejemplo de uso:
ca = ControlAsistencia()
ca.registrar_grupo("Ana", "Carlos", "Ana", "Beatriz", "Carlos")
print(f"Total únicos: {ca.contar_unicos()}")  # 3
print(f"Historial completo: {ca.historial_ingresos}")  # ['Ana', 'Carlos', 'Ana', 'Beatriz', 'Carlos']