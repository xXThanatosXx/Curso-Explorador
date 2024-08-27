class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha= False


    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            return "EL coche esta en marcha"
        else:
            return "El coche esta parado"
        

    def estado(self):
        print("El coche tiene:",self.__ruedas,"Un ancho de",self.__anchoChasis, "y un largo de",self.__largoChasis)
        

miCoche = Coche()

print("El largo del coche es:",miCoche.largoChasis)
print("El coche tiene",miCoche.ruedas,"ruedas")
miCoche.arrancar()

print(miCoche.estado())

miCoche2 = Coche()

print("El largo del coche es:",miCoche2.largoChasis)
print("El coche tiene",miCoche2.ruedas,"ruedas")
#miCoche2.arrancar()
print(miCoche2.estado())
