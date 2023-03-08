#. Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene

cont=0
numInt=int(input("ingrese un número entero de tres dígitos: "))

if(numInt>99 and numInt<1000):
    dig1=numInt//100
    dig2=(numInt%100)//10
    dig3=(numInt%100)%10
    if(dig1%2==0):
        cont=cont+1
    if(dig2%2==0):
        cont=cont+1
    if(dig3%2==0):
        cont=cont+1        




    print(f"Hay {cont} dígitos pares")   
       

    


