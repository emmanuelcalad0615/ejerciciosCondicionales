#Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par

num1=int(input("Ingrese el primer número entero de dos dígitos: "))
num2=int(input("Ingrese el segundo número enterod de dos dígitos: "))

if(num1<10 or num1>99):
    print("El primer número no es de dos dígitos")
    
elif(num2<10 or num2>99):
    print("El segundo número no es de dos dígitos")
    
else:
    suma=num1+num2
    if(suma%2==0):
        print("El resultado de la suma de los números en par")
    else:
        print("El resultado de la suma de los números es impar")        
