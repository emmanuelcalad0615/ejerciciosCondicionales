#Leer tres números enteros y mostrarlos ascendentemente.

numInt1=int(input("Ingrese el primer número entero: "))
numInt2=int(input("Ingrese el segundo número entero: "))
numInt3=int(input("Ingrese el tercer número entero: "))

if(numInt1>numInt2 and numInt2>numInt3):
    mayor=numInt1
    medio=numInt2
    menor=numInt3
elif(numInt1>numInt3 and numInt3>numInt2):
    mayor=numInt1
    medio=numInt3
    menor=numInt2
elif(numInt2>numInt1 and numInt1>numInt3):
    mayor=numInt2
    medio=numInt1
    menor=numInt3    
elif(numInt2>numInt3 and numInt3>numInt1):
    mayor=numInt2
    medio=numInt3
    menor=numInt1
elif(numInt3>numInt2 and numInt2>numInt1):
    mayor=numInt3
    medio=numInt2
    menor=numInt1
elif(numInt3>numInt1 and numInt1>numInt2):
    mayor=numInt3
    medio=numInt1
    menor=numInt2
print(f"1. {menor}")
print(f"2. {medio}")    
print(f"3. {mayor}")
        
