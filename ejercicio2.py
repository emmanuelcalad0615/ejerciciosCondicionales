#. Leer un número entero y determinar si tiene 3 dígitos.

numEntero=int(input("Ingrese el número entero: "))

if(numEntero>99 and numEntero<1000):
    print(f"El número {numEntero} tiene 3 dígitos")
else:
    print(f"El número {numEntero} no tiene 3 dígitos")    