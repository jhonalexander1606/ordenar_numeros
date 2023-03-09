# programa para ordenar 3 numeros de manera ascendente

print("----------------------------")
print("----------ordenar numeros---")
print("----------------------------")

#input

n1 = int(input("inserte el primer numero: "))
n2 = int(input("inserte el segundo numero: "))
n3 = int(input("inserte el tercer numero: "))

#processing
if n1 > n2:
    if n1 > n3:
       if n2 > n3:
           rta = "los numeros en orden ascendente son" , n3, n2, n1
       else:
           rta = "los numeros en orden ascendente son" , n2, n3, n1
    else:
        rta = "los numeros en orden ascendente son" , n2, n1, n3
else:
    if n1 > n3:
        rta = "los numeros en orden ascendente son" , n3, n1, n2
    else:
        if n2 > n3:
            rta = "los numeros en orden ascendente son" , n1, n3, n2
        else:
            rta = "los numeros en orden ascendente son" , n1, n3, n3
            
#output