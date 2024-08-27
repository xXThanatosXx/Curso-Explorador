# Protección o Control de Acceso
class Gato:
    def __init__(self, nombre):
        self._nombre = nombre  # Atributo protegido

class GatoPersa(Gato):
    def mostrar_nombre(self):
        return f"El nombre del gato es {self._nombre}"

gato_persa = GatoPersa("Canela")
print(gato_persa.mostrar_nombre())  # Accede al atributo protegido
