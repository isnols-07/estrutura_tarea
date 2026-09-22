#EJERCICIO 16
#Entrada
#Palabra y desplazamiento

#Proceso
#Convertir cada letra a código, desplazarla y volver a convertirla

#Salida
#Palabra codificada

#Bosquejo
#a → +3 → d
#b → +3 → e
#c → +3 → f

#"abc" → "def"

class CodificadorCesar:

    def __init__(self):
        # Diccionario para guardar historial
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):

        # Convertimos la letra a código ASCII
        codigo = ord(letra)

        # Desplazamos la letra
        nuevo_codigo = ((codigo - ord('a') + desplazamiento) % 26) + ord('a')

        # Convertimos nuevamente a letra
        return chr(nuevo_codigo)

    def codificar_palabra(self, palabra, desplazamiento):

        resultado = ""

        for letra in palabra:

            resultado = resultado + self.codificar_letra(
                letra,
                desplazamiento
            )

        # Guardamos en el historial
        self.historial[palabra] = resultado

        return resultado
# PROGRAMA PRINCIPAL
cc = CodificadorCesar()

print(cc.codificar_palabra("hola", 3))

print(cc.historial)

# VERIFICACIÓN
# h → k
# o → r
# l → o
# a → d
#
# hola → krok

#ejercicio 16.1

class CifradorInverso:

  def __init__(self):
    self.historial = {}

  def cifrar_caracter(self, caracter):
    reemplazos = {
        'a': '@',
        'e': '3',
        'i': '1',
        'o': '0',
        'u': '#',
        'A': '@',
        'E': '3',
        'I': '1',
        'O': '0',
        'U': '#',
    }
    return reemplazos.get(caracter, caracter)

  def cifrar_texto(self, texto):
    cifrado = ''.join([self.cifrar_caracter(c) for c in texto])
    self.historial[texto] = cifrado
    return cifrado


# Ejemplo de uso:
ci = CifradorInverso()
print(ci.cifrar_texto("Hola Mundo"))  # H0l@ M#nd0
print(f"Historial: {ci.historial}")  # {'Hola Mundo': 'H0l@ M#nd0'}