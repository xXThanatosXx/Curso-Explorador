import Operaciones as op

class Calculadora:
    def __init__(self):
        pass
    
    def menu(self):
        while True:
            try:
                opc1 = int(input("Introduce el primer número: "))
                opc2 = int(input("Introduce el segundo número: "))
                operacion = input("Introduce la operación a realizar (Suma, Resta, Multiplicación, División): ").lower()
                return opc1, opc2, operacion
                break
            except ValueError:
                print("Debes ingresar un número válido.")
    
    def realizar_operacion(self, opc1, opc2, operacion):
        if operacion == "suma":
            print(op.suma(opc1, opc2))
        elif operacion == "resta":
            print(op.resta(opc1, opc2))
        elif operacion == "multiplicacion":
            print(op.multiplicacion(opc1, opc2))
        elif operacion == "division":
            print(op.division(opc1, opc2))
        else:
            print("Operación no reconocida.")
    
    def ejecutar_calculadora(self):
        while True:
            try:
                print("Programa calculadora:")
                respuesta = input("¿Desea realizar una operación? (Y/N): ").lower()
                if respuesta == "y":
                    opc1, opc2, operacion = self.menu()
                    self.realizar_operacion(opc1, opc2, operacion)
                else:
                    break
            except Exception as e:
                print("Error:", e)
        
        print("Programa finalizado.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.ejecutar_calculadora()
