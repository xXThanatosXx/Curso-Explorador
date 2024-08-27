class Coche:

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            chequeo = self.chequeo()
            if chequeo:
                return "El coche está en marcha"
            else:
                return "El coche está mal"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene:", self.__ruedas, "ruedas, un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def chequeo(self):
        print("Realizando chequeo...")

        self.gasolina = "ok"
        self.aceite = 'ok'
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

miCoche = Coche()

# Descomenta las siguientes líneas para probar los métodos
print(miCoche.arrancar(True))
miCoche.estado()

