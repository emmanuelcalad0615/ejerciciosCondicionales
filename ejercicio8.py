#8. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.

num1=int(input("Ingrese el segundo número entero de dos dígitos: "))
num2=int(input("Ingrese el segundo número entero de dos dígitos: "))

if(num1<10 or num1>99):
    print("El primer número no es de dos dígitos, volver a ejecutar")
   
elif(num2<10 or num2>99):
    print("El primer número no es de dos dígitos, volver a ejecutar")
    
else:
    dig1Num1=num1%10
    dig2Num1=num1//10
    dig1Num2=num2%10
    dig2Num2=num2//10
    if(dig1Num1==dig1Num2 or dig1Num1==dig2Num1 or dig2Num1==dig1Num2 or dig2Num1==dig2Num2):
        print("Los números tienen dígitos en común")
    else:
        print("Los números no tienen dígitos en común")    
            
