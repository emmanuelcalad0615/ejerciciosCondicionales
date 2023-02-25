#1. Leer un número entero y determinar si es un número terminado en 4.
numEntero=int(input("Ingrese el número entero: "))
if(numEntero %10==4):
    print(f"El número {numEntero} termina en 4")
else:
    print(f"El número {numEntero} no termina en 4")    