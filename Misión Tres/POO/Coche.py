class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False


    def arrancar(self,val):
        self.enmarcha = val

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        

miCoche = Coche()
print("Vehiculo Uno")
print("V1:", miCoche.enmarcha)
miCoche.arrancar(True)
print("V1:",miCoche.estado())
print("Vehiculo dos")
miCoche2 = Coche()
miCoche2.arrancar(False)
print("V2",miCoche2.estado())
print("Vehiculo Tres")



miCoche3 = Coche()
miCoche3.arrancar(True)
print("V3 ",miCoche3.estado())

# print("El largo del coche es:",miCoche.largoChasis)
# print("El coche tiene",miCoche.ruedas,"ruedas")
# print("El ancho del coche es:",miCoche.anchoChasis)
#print("El largo del coche es:",miCoche2.largoChasis)
# print("El coche tiene",miCoche2.ruedas,"ruedas")