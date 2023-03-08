#Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene.
cont=0
numInt=int(input("Ingrese un número entero de 4 dígitos"))

if(numInt>999 and numInt<10000):
    dig1= numInt//1000
    dig2=(numInt%1000)//100
    dig3=(numInt%100)//10
    dig4=numInt%10

    if(dig1%2==0):
        cont=cont+1
    if(dig2%2==0):
        cont=cont+1
    if(dig3%2==0):
        cont=cont+1
    if(dig4%2==0):
        cont=cont+1
    print(f"El número tiene {cont} dígitos pares")                

    