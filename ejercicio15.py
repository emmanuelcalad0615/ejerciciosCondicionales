#Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
digMayor=0
numInt=int(input("Ingrese un número entero"))
dig1=numInt//10
dig2=numInt%10
numUbi=numInt
if(numInt>9 and numInt<100):
    if(dig1>digMayor or dig2>digMayor):
     if(dig1>dig2):
         digMayor=dig1
         numUbi=numInt
     else:
         digMayor=dig2 
         numUbi=numInt  
 
numInt=int(input("Ingrese un número entero"))
dig1=numInt//10
dig2=numInt%10
if(numInt>9 and numInt<100):
    if(dig1>digMayor or dig2>digMayor):
     if(dig1>dig2):
         digMayor=dig1
         numUbi=numInt
     else:
         digMayor=dig2 
         numUbi=numInt  
numInt=int(input("Ingrese un número entero"))
dig1=numInt//10
dig2=numInt%10
if(numInt>9 and numInt<100):
    if(dig1>digMayor or dig2>digMayor):
     if(dig1>dig2):
         digMayor=dig1
         numUbi=numInt
     else:
         digMayor=dig2 
         numUbi=numInt   
        

print(f"El dígito mayor está ubicado en {numUbi} y es {digMayor}")

   

