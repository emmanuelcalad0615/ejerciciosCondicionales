#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares

numInt=int(input("Ingrese un número de dos dígitos: "))

while numInt!="":
    if(numInt>9 and numInt<100):
        dig1=numInt//10
        dig2=numInt%10
        
        if(dig1%2==0 and dig2%2==0):
            print(f"Ambos dígitos son pares")
            
        elif(dig1%2==0 and dig2%2!=0):
            print(f"El dígito 1 es par y el dígito 2 es impar")

        elif(dig1%2!=0 and dig2%2==0):
            print(f"El dígito 1 es impar y el dígito 2 es par")  
        elif(dig1%2!=0 and dig2%2!=0 ):
            print(f"Ambos dígitos son impares ") 
        else:
            print("Ingrese un número de 2 dígitos")  
    else:
       numInt=int(input("Ingrese un número de dos dígitos: "))
       
    
    
