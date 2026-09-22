#EJERCICIO 15
#Entrada
#Uno o varios números

#Proceso
#Probar divisores
#Para comprobar si es perfecto
#Guardar resultados

#Salida
#Tupla, True/False y diccionario

#BOSQUEJO
#12:

#1 divide a 12 ✓
#2 divide a 12 ✓
#3 divide a 12 ✓
#4 divide a 12 ✓
#5 ✗
#6 ✓
#12 ✓

#Divisores:
#(1,2,3,4,6,12)

class DivisorFinder:

    def encontrar_divisores(self, numero):

        divisores = ()

        for i in range(1, numero + 1):

            if numero % i == 0:
                divisores = divisores + (i,)

        return divisores

    def es_perfecto(self, numero):

        suma = 0

        # No incluimos el mismo número
        for i in range(1, numero):

            if numero % i == 0:
                suma = suma + i

        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):

        resultado = {}

        for numero in numeros:

            resultado[numero] = self.encontrar_divisores(numero)

        return resultado
# PROGRAMA PRINCIPAL
df = DivisorFinder()

print(df.encontrar_divisores(12))

print(df.es_perfecto(6))

print(df.encontrar_multiples_divisores(6, 12, 10))

# VERIFICACIÓN
# Divisores de 12:
# (1, 2, 3, 4, 6, 12)

# 6 es perfecto porque:
# 1 + 2 + 3 = 6

# Resultado:
# True

#ejercicio 15.1

class CalculadorMultiplos:

  def obtener_multiplos(self, numero, limite):
    multiplos = []
    m = numero
    while m <= limite:
      multiplos.append(m)
      m += numero
    return tuple(multiplos)

  def es_multiplo_de(self, numero, base):
    if base == 0:
      return False
    return numero % base == 0

  def multiplos_de_varios(self, limite, *numeros):
    resultado = {}
    for n in numeros:
      resultado[n] = self.obtener_multiplos(n, limite)
    return resultado


# Ejemplo de uso:
cm = CalculadorMultiplos()
print(cm.obtener_multiplos(5, 22))  # (5, 10, 15, 20)
print(cm.multiplos_de_varios(15, 3, 4))  # {3: (3, 6, 9, 12, 15), 4: (4, 8, 12)}