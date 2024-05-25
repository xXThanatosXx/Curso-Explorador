# from Calculadora import suma
import Calculadora as cd
#import Calculadora


while(True):
    try:
        opc1 = float(input("Numero uno: "))
        opc2 = float(input("Numero dos: "))
        break
    except ValueError:
        print("debes ingresar un numero: ")

operacion = input("Introduce la operacion a realizar (suma,resta,multiplicacion, division)")

operacion.lower()

if operacion == "suma":
    print(cd.suma(opc1,opc2))
elif operacion == "resta":
    print(cd.resta(opc1,opc2))
elif operacion == "multiplicacion":
    print(cd.multiplicacion(opc1,opc2))
elif operacion == "division":
    print(cd.division(opc1,opc2))
else:
    print("Operacion no completada")

print("Programa Finalizado")


