#Leer dos números enteros y determinar cuál es el mayor
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
if(num1>num2):
    print(f"El primer número {num1} es mayor al segundo número {num2}")
elif(num2>num1):
    print(f"El segundo número ingresado {num2} es mayor al primer número {num1}")
else:
    print("Los número son iguales")        