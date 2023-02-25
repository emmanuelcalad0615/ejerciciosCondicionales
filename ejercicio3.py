#Leer un número entero y determinar si es negativo

numEntero=int(input("Ingrese un número entero: "))

if(numEntero>0):
    print(f"el numero {numEntero} es pisitivo")
elif(numEntero<0):
    print(f"El numero {numEntero} es negativo")
else:
    print(f"El número no pertenece al cojunto negativo ni el positivo")        