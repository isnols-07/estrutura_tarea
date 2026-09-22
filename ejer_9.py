#EJERCICIO 9
#Entrada
#Un texto

#Proceso
#Recorrer carácter por carácter y clasificar

#Salida
#Diccionario con cantidades

#BOSQUEJO
#H → consonante
#o → vocal
#l → consonante
#a → vocal
#1 → dígito
#2 → dígito
#3 → dígito

#Vocales = 2
#Consonantes = 2
#Dígitos = 3

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):

        if letra in "aeiouAEIOU":
            return True
        else:
            return False

    def contar_por_tipo(self, texto):

        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:

            if self.solo_vocales(letra):
                vocales = vocales + 1

            elif letra.isdigit():
                digitos = digitos + 1

            elif letra.isalpha():
                consonantes = consonantes + 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }
# PROGRAMA PRINCIPAL
astr = AnalizadorString()

print(astr.contar_por_tipo("Hola123"))

print("Texto más largo:")
print(astr.texto_mas_largo)

# VERIFICACIÓN
# Hola123
#
# Vocales = 2
# Consonantes = 2
# Dígitos = 3

#ejercico 9.1

class AnalizadorCaracteres:

  def __init__(self):
    self.cadena_mas_larga = ""

  def es_mayuscula(self, caracter):
    return caracter.isupper()

  def analizar_cadena(self, cadena):
    if len(cadena) > len(self.cadena_mas_larga):
      self.cadena_mas_larga = cadena

    res = {"mayusculas": 0, "minusculas": 0, "simbolos": 0}
    for char in cadena:
      if char.isupper():
        res["mayusculas"] += 1
      elif char.islower():
        res["minusculas"] += 1
      else:
        res["simbolos"] += 1
    return res


# Ejemplo de uso:
ac = AnalizadorCaracteres()
print(
    ac.analizar_cadena("Hola Mundo!! 123")
)  # {'mayusculas': 2, 'minusculas': 7, 'simbolos': 7}
ac.analizar_cadena("Corta")
print(f"Cadena más larga: '{ac.cadena_mas_larga}'")  # 'Hola Mundo!! 123'