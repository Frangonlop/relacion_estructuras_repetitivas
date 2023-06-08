print("Tablas de multiplicar del 1 al 10: ")
cont=1
while cont<=10:
    num=1
    print("")
    print("Tabla del "+str(cont))
    print("")
    while num<=10:
     print(str(cont) + " x "+str(num)+" = "+str(cont*num))
     num=num+1
    cont=cont+10