#EJERCICIO 5
#Entrada
#Números

#Proceso
#Usar % 2

#Salida
#Diccionario de pares/impares y cantidades

#BOSQUEJO
#1 → impar
#2 → par
#3 → impar
#4 → par
#5 → impar
 
#Pares = [2,4]
#Impares = [1,3,5]

#Cantidad = (2,3)

class AnalizadorNumero:
    def __init__(self):
        self.par=[]
        self.impar=[]
    def espar(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False   

    def separar (self, *numeros):
        for numero in numeros:
            if self.espar(numero):
                self.par.append(numero)
            else:
                self.impar.append(numero)
        return {"par":self.par, 
                "impar":self.impar}
    def cantidad_pares_impares(self):
        return (len(self.par), len(self.impar))

an = AnalizadorNumero()

print(an.separar(1, 2, 3, 4, 5))

print(an.cantidad_pares_impares())

#ejercico 5.1

class ClasificadorSignos:

  def __init__(self):
    self.positivos = []
    self.negativos = []

  def es_positivo(self, numero):
    return numero > 0

  def separar_signos(self, *numeros):
    self.positivos = []
    self.negativos = []
    for n in numeros:
      if self.es_positivo(n):
        self.positivos.append(n)
      elif n < 0:
        self.negativos.append(n)
    return {"positivos": self.positivos, "negativos": self.negativos}

  def resumen_cantidades(self):
    return (len(self.positivos), len(self.negativos))


# Ejemplo de uso:
cs = ClasificadorSignos()
print(cs.separar_signos(12, -5, 8, -3, -1, 20))
# {'positivos': [12, 8, 20], 'negativos': [-5, -3, -1]}
print(f"Resumen (pos, neg): {cs.resumen_cantidades()}")  # (3, 3)