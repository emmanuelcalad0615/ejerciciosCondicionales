#13. Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.
numInt=int(input("Ingrese un número entero"))
mayor= numInt
numInt=int(input("Ingrese el segundo número entero"))
if(numInt>mayor):
    mayor=numInt
numInt=int(input("Ingrese el tercer número entero"))
if(numInt>mayor):
    mayor=numInt
print(f"El número mayor es: {mayor}")        