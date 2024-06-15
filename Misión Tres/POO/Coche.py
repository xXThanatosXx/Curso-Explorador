class coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha= False


    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        

miCoche = coche()

print("El largo del coche es:",miCoche.largoChasis)
print("El coche tiene",miCoche.ruedas,"ruedas")
miCoche.arrancar()

print(miCoche.estado())

miCoche2 = coche()

print("El largo del coche es:",miCoche2.largoChasis)
print("El coche tiene",miCoche2.ruedas,"ruedas")
#miCoche2.arrancar()
print(miCoche2.estado())
