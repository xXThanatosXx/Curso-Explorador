#Encapsulamiento
class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre      # Atributo público
        self.__edad = edad        # Atributo privado (encapsulado)

    def mostrar_info(self):
        return f"{self.nombre} tiene {self.__edad} años."

# Intentar acceder directamente a un atributo privado genera un error
mi_gato = Gato("Luna", 4)
print(mi_gato.mostrar_info())  # Correcto
# print(mi_gato.__edad)        # Esto causaría un error
