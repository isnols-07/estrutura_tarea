#EJERCICIO 20
#Entrada
#Texto y patrón

#Proceso
#Separar texto con split()
#Buscar palabras que comiencen con el patrón
#Agrupar por longitud
#Eliminar duplicados con set

#Salida
#Lista, diccionario y conjunto

#Bosquejo
#Texto:
#"el gato está aquí"
#split():
#["el", "gato", "está", "aquí"]
#Longitud:
#"el" → 2
#"gato" → 4
#"está" → 4
#"aquí" → 4
#Patrón "ga":
#gato → empieza con "ga"

class AnalizadorPatrones:

    def __init__(self):
        # Conjunto para guardar palabras únicas
        self.palabras = set()

    def encontrar_palabras(self, texto, patron):

        resultado = []

        palabras = texto.split()

        for palabra in palabras:

            if palabra.startswith(patron):
                resultado.append(palabra)

            # Guardamos todas las palabras
            self.palabras.add(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):

        resultado = {}

        palabras = texto.split()

        for palabra in palabras:

            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

            # Guardamos la palabra en el conjunto
            self.palabras.add(palabra)

        return resultado

    def palabras_unicas(self):

        return self.palabras
# PROGRAMA PRINCIPAL
ap = AnalizadorPatrones()

texto = "el gato está aquí gato"

print("Palabras que empiezan con ga:")
print(ap.encontrar_palabras(texto, "ga"))

print("Agrupadas por longitud:")
print(ap.agrupar_por_longitud(texto))

print("Palabras únicas:")
print(ap.palabras_unicas())

# VERIFICACIÓN
# Texto:
# el gato está aquí gato

# Patrón "ga":
# ["gato", "gato"]

# Palabras únicas:
# {"el", "gato", "está", "aquí"}

#ejercicio20.1

class AnalizadorVocabulario:

  def palabras_que_terminan_en(self, texto, sufijo):
    palabras = texto.split()
    res = []
    for p in palabras:
       if p.lower().endswith(sufijo.lower()):
          res.append(p)
    return res

  def agrupar_por_inicial(self, texto):
    palabras = texto.split()
    agrupado = {}
    for p in palabras:
      inicial = p[0].lower()
      if inicial not in agrupado:
        agrupado[inicial] = []
      agrupado[inicial].append(p)
    return agrupado

  def extraer_conjunto_palabras(self, texto):
    palabras = texto.lower().split()
    return set(palabras)


# Ejemplo de uso:
av = AnalizadorVocabulario()
oracion = "El gato y el perro corren rápido por el parque"

print(av.palabras_que_terminan_en(oracion, "o"))
# ['gato', 'perro', 'rápido']

print(av.agrupar_por_inicial("Sol Sombra Luna"))
# {'s': ['Sol', 'Sombra'], 'l': ['Luna']}

print(av.extraer_conjunto_palabras(oracion))
# {'el', 'gato', 'y', 'perro', 'corren', 'rápido', 'por', 'parque'}